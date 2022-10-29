from typing_extensions import TypedDict
from typing import Dict, List, Optional, Union, cast
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class RegionInfo(TypedDict):
    index: int
    enum_index: int
    project_id: str
    name: str
    start: float
    end: float
    rendered_tracks: List['reapy_boost.Track']


class Region(ReapyObject):

    _class_name = "Region"
    project_id: str
    index: int
    enum_index: int

    def __init__(
        self,
        parent_project: Optional['reapy_boost.Project'] = None,
        index: Optional[int] = None,
        parent_project_id: Optional[str] = None,
        enum_index: Optional[int] = None
    ) -> None:
        if parent_project_id is None:
            message = (
                "One of `parent_project` or `parent_project_id` must be "
                "specified."
            )
            assert parent_project is not None, message
            parent_project_id = parent_project.id
        self.enum_index = enum_index
        self.project = reapy_boost.Project(parent_project_id)
        self.project_id = parent_project_id
        if index is None:
            if enum_index is None:
                index = self.project.n_regions
            else:
                index = cast(
                    int,
                    RPR.EnumProjectMarkers2(  # type:ignore
                        self.project_id, enum_index, 0, 0, 0, 0, 0
                    )[7]
                )
        self.index = index
        if enum_index is None:
            # self.enum_index = None
            enum_index = self._get_enum_index()
        self.enum_index = enum_index

    @reapy_boost.inside_reaper()
    def _get_enum_index(self) -> int:
        """
        Return region index as needed by RPR.EnumProjectMarkers2.

        Raises
        ------
        reapy_boost.errors.UndefinedRegionError
        """
        for region in self.project.regions:
            if region.index == self.index:
                return region.enum_index
        raise reapy_boost.errors.UndefinedRegionError(self.index)

    @property
    def _kwargs(self) -> Dict[str, Union[str, int]]:
        return {
            "index": self.index,
            "parent_project_id": self.project_id,
            "enum_index": self.enum_index
        }

    def add_rendered_track(self, track: 'reapy_boost.Track') -> None:
        """
        Add track to region render matrix for this region.

        Parameters
        ----------
        track : Track
            Track to add.

        See also
        --------
        Region.add_rendered_tracks
            Efficiently add several tracks to region render matrix.
        Region.remove_rendered_track
        Region.remove_rendered_tracks
        """
        RPR.SetRegionRenderMatrix(  # type:ignore
            self.project_id, self.index, track.id, 1)

    @reapy_boost.inside_reaper()
    def add_rendered_tracks(self, tracks: List['reapy_boost.Track']) -> None:
        """
        Efficiently add  several tracks to region render matrix.

        Parameters
        ----------
        tracks : list of Track
            Tracks to add.

        See also
        --------
        Region.remove_rendered_tracks
        """
        for track in tracks:
            self.add_rendered_track(track)

    @property
    def end(self) -> float:
        """
        Region end.

        :type: float
            Region end in seconds.
        """
        return self._end_inside()

    @reapy_boost.inside_reaper()
    def _end_inside(self) -> float:
        index = self._get_enum_index()
        args = self.project_id, index, 0, 0, 0, 0, 0
        return cast(float, RPR.EnumProjectMarkers2(*args)[5])  # type:ignore

    @end.setter
    def end(self, end: float) -> None:
        """
        Set region end.

        Parameters
        ----------
        end : float
            region end in seconds.
        """
        args = self.project_id, self.index, True, self.start, end, self.name
        RPR.SetProjectMarker2(*args)  # type:ignore

    def delete(self) -> None:
        """
        Delete region.
        """
        RPR.DeleteProjectMarker(  # type:ignore
            self.project_id, self.index, True)

    @property
    def name(self) -> str:
        """
        Region name.

        :type: str
        """
        return self._name_inside()

    @reapy_boost.inside_reaper()
    def _name_inside(self) -> str:
        # index = self._get_enum_index()
        fs = RPR.SNM_CreateFastString('0' * 1024)  # type:ignore
        args = self.project_id, self.index, True, fs
        RPR.SNM_GetProjectMarkerName(*args)  # type:ignore
        result = cast(str, RPR.SNM_GetFastString(fs))  # type:ignore
        RPR.SNM_DeleteFastString(fs)  # type:ignore
        return result

    @name.setter
    def name(self, name: str) -> None:
        """
        Set region name.

        Parameters
        ----------
        name : str
        """
        args = self.project_id, self.index, True, self.start, self.end, name
        RPR.SetProjectMarker2(*args)  # type:ignore

    def remove_rendered_track(self, track: 'reapy_boost.Track') -> None:
        """
        Remove track from region render matrix for this region.

        Parameters
        ----------
        track : Track
            Track to remove.

        See also
        --------
        Region.add_rendered_tracks
        Region.remove_rendered_track
        Region.remove_rendered_tracks
            Efficiently remove several tracks from render matrix.
        """
        RPR.SetRegionRenderMatrix(  # type:ignore
            self.project_id, self.index, track.id, -1)

    @reapy_boost.inside_reaper()
    def remove_rendered_tracks(
        self, tracks: List['reapy_boost.Track']
    ) -> None:
        """
        Efficiently remove  several tracks from region render matrix.

        Parameters
        ----------
        tracks : list of Track
            Tracks to remove.

        See also
        --------
        Region.add_rendered_tracks
        """
        for track in tracks:
            self.remove_rendered_track(track)

    @property
    def rendered_tracks(self) -> List['reapy_boost.Track']:
        """
        List of tracks for this region in region render matrix.

        :type: list of Track
        """
        return self._rendered_tracks_inside()

    @reapy_boost.inside_reaper()
    def _rendered_tracks_inside(self) -> List['reapy_boost.Track']:
        i = 0
        tracks = []
        while i == 0 or tracks[-1]._is_defined:
            track_id = RPR.EnumRegionRenderMatrix(  # type:ignore
                self.project_id, self.index, i
            )
            tracks.append(reapy_boost.Track(track_id))
            i += 1
        return tracks[:-1]

    @property
    def start(self) -> float:
        """
        Region start.

        :type: float
        """
        return self._start_inside()

    @reapy_boost.inside_reaper()
    def _start_inside(self) -> float:
        args = self.project_id, self._get_enum_index(), 0, 0, 0, 0, 0
        return RPR.EnumProjectMarkers2(*args)[4]  # type:ignore

    @start.setter
    def start(self, start: float) -> None:
        """
        Set region start.

        Parameters
        ----------
        start : float
            region start in seconds.
        """
        RPR.SetProjectMarker2(  # type:ignore
            self.project_id, self.index, 1, start, self.end, self.name
        )

    @property
    def infos(self) -> RegionInfo:
        """Get all Region infos in one call.

        Returns
        -------
        RegionInfo
            index: int
            enum_index: int
            project_id: str
            name: str
            start: float
            end: float
            rendered_tracks: List[reapy_boost.Track]
        """
        return self._infos_inside()

    @reapy_boost.inside_reaper()
    def _infos_inside(self) -> RegionInfo:
        enum_index = self._get_enum_index()
        args = self.project_id, enum_index, 0, 0, 0, 0, 0
        (_, _, _, _, start, end, _,
         index) = RPR.EnumProjectMarkers2(  # type:ignore
             *args
         )
        out: RegionInfo = {
            'index': index,
            'enum_index': enum_index,
            'project_id': self.project_id,
            'start': start,
            'end': end,
            'name': self.name,
            'rendered_tracks': self.rendered_tracks
        }
        return out
