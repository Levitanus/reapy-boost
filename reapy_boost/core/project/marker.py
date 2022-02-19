from typing import Dict, Optional, TypedDict, Union, cast
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class MarkerInfo(TypedDict):

    index: int
    enum_index: int
    project_id: str
    position: float
    name: str


class Marker(ReapyObject):

    _class_name = "Marker"

    def __init__(
        self,
        parent_project: Optional['reapy_boost.Project'] = None,
        index: Optional[int] = None,
        parent_project_id: Optional[str] = None,
        enum_index: Optional[int] = None
    ):
        if parent_project_id is None:
            message = (
                "One of `parent_project` or `parent_project_id` must be " +
                "specified."
            )
            assert parent_project is not None, message
            parent_project_id = parent_project.id
        self.project = reapy_boost.Project(parent_project_id)
        self.project_id = parent_project_id
        if index is None:
            index = self.project.n_markers
        self.index = index
        if enum_index is None:
            self.enum_index = None
            enum_index = self._get_enum_index()
        self.enum_index = enum_index

    def _get_enum_index(self) -> int:
        """
        Return marker index as needed by RPR.EnumProjectMarkers2.

        Raises
        ------
        reapy_boost.errors.UndefinedMarkerError
            Description
        """
        with reapy_boost.inside_reaper():
            for marker in self.project.markers:
                if marker.index == self.index:
                    return marker.enum_index
        raise reapy_boost.errors.UndefinedMarkerError(self.index)

    @property
    def _kwargs(self) -> Dict[str, object]:
        return {
            "index": self.index,
            "parent_project_id": self.project_id,
            'enum_index': self.enum_index
        }

    def delete(self) -> None:
        """
        Delete marker.
        """
        RPR.DeleteProjectMarker(  # type:ignore
            self.project_id, self.index, False)

    @property
    def infos(self) -> MarkerInfo:
        """Get all Region infos in one call.

        Returns
        -------
        MarkerInfo
            index: int
            enum_index: int
            project_id: str
            position: float
            name: str
        """
        return self._infos_inside()

    @reapy_boost.inside_reaper()
    def _infos_inside(self) -> 'MarkerInfo':
        enum_index = self._get_enum_index()
        args = self.project_id, enum_index, 0, 0, 0, 0, 0
        (_, _, _, _, position, _, _,
         index) = RPR.EnumProjectMarkers2(  # type:ignore
             *args
         )
        out: MarkerInfo = {
            'index': cast(int, index),
            'enum_index': enum_index,
            'project_id': self.project_id,
            'position': cast(float, position),
            'name': self.name,
        }
        return out

    @property
    def name(self) -> str:
        """
        Marker name.

        :type: str
        """
        with reapy_boost.inside_reaper():
            # index = self._get_enum_index()
            fs = RPR.SNM_CreateFastString('0' * 1024)  # type:ignore
            args = self.project_id, self.index, False, fs
            RPR.SNM_GetProjectMarkerName(*args)  # type:ignore
            result = RPR.SNM_GetFastString(fs)  # type:ignore
            RPR.SNM_DeleteFastString(fs)  # type:ignore
        return result

    @name.setter
    def name(self, name: str) -> None:
        """
        Set marker name.

        Parameters
        ----------
        name : str
        """
        args = self.project_id, self.index, False, self.position, 0, name
        RPR.SetProjectMarker2(*args)  # type:ignore

    @property
    def position(self) -> float:
        """
        Return marker position.

        Returns
        -------
        position : float
            Marker position in seconds.
        """
        return self._position_inside()

    @reapy_boost.inside_reaper()
    def _position_inside(self) -> float:
        index = self._get_enum_index()
        print(f'enum index in position: {index}')
        return RPR.EnumProjectMarkers2(  # type:ignore
            self.project_id, index, 0, 0, 0, 0, 0)[4]

    @position.setter
    def position(self, position: float) -> None:
        """
        Set marker position.

        Parameters
        ----------
        position : float
            Marker position in seconds.
        """
        RPR.SetProjectMarker2(  # type:ignore
            self.project_id, self.index, False, position, 0, self.name)
