from typing import List, Tuple, Union, cast
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class Item(ReapyObject):

    _class_name = "Item"

    def __init__(self, id: str):
        self.id = id

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Item) and self.id == other.id

    @property
    def _args(self) -> Tuple[str]:
        return self.id,

    @property
    def active_take(self) -> 'reapy_boost.Take':
        """
        Return the active take of the item.

        Returns
        -------
        take : Take
            Active take of the item.
        """
        take = reapy_boost.Take(RPR.GetActiveTake(self.id))  # type:ignore
        return take

    def add_take(self) -> 'reapy_boost.Take':
        """
        Create and return a new take in item.

        Returns
        -------
        take : Take
            New take in item.
        """
        take_id = RPR.AddTakeToMediaItem(self.id)  # type:ignore
        take = reapy_boost.Take(take_id)
        return take

    @reapy_boost.inside_reaper()
    def delete(self) -> None:
        """Delete item."""
        RPR.DeleteTrackMediaItem(self.track.id, self.id)  # type:ignore

    def get_info_value(self, param_name: str) -> float:
        value = RPR.GetMediaItemInfo_Value(self.id, param_name)  # type:ignore
        return value

    def get_take(self, index: int) -> 'reapy_boost.Take':
        """
        Return index-th take of item.

        Parameters
        ----------
        index : int
            Take index.

        Returns
        -------
        take : Take
            index-th take of media item.
        """
        take_id = RPR.GetItemTake(self.id, index)  # type:ignore
        take = reapy_boost.Take(take_id)
        return take

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if item has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        return self._has_valid_id_inside()

    @reapy_boost.inside_reaper()
    def _has_valid_id_inside(self) -> bool:
        try:
            project_id = self.project.id
        except OSError:
            return False
        pointer, name = self._get_pointer_and_name()
        return bool(
            RPR.ValidatePtr2(  # type:ignore
                project_id, pointer, name
            )
        )

    @property
    def is_selected(self) -> bool:
        """
        Return whether item is selected.

        Returns
        -------
        is_selected : bool
            Whether item is selected.
        """
        is_selected = bool(RPR.IsMediaItemSelected(self.id))  # type:ignore
        return is_selected

    @is_selected.setter
    def is_selected(self, value: bool) -> None:
        self.set_info_value("B_UISEL", int(value))

    @property
    def length(self) -> float:
        """
        Return item length in seconds.

        Returns
        -------
        length : float
            Item length in seconds.
        """
        param_name = "D_LENGTH"
        length = self.get_info_value(param_name)
        return length

    @length.setter
    def length(self, length: float) -> None:
        """
        Set item length.

        Parameters
        ----------
        length : float
            New item length in seconds.
        """
        RPR.SetMediaItemLength(self.id, length, True)  # type:ignore

    @reapy_boost.inside_reaper()
    def make_only_selected_item(self) -> None:
        """
        Make track the only selected item in parent project.
        """
        self.project.select_all_items(False)
        self.is_selected = True

    @property
    def n_takes(self) -> int:
        """
        Return the number of takes of media item.

        Returns
        -------
        n_takes : int
            Number of takes of media item.
        """
        n_takes = cast(int, RPR.GetMediaItemNumTakes(self.id))  # type:ignore
        return n_takes

    @property
    def position(self) -> float:
        """
        Return item position in seconds.

        Returns
        -------
        position : float
            Item position in seconds.
        """
        position = self.get_info_value("D_POSITION")
        return position

    @position.setter
    def position(self, position: float) -> None:
        """
        Set media item position to `position`.

        Parameters
        ----------
        position : float
            New item position in seconds.
        """
        RPR.SetMediaItemPosition(self.id, position, False)  # type:ignore

    @property
    def project(self) -> 'reapy_boost.Project':
        """
        Item parent project.

        :type: reapy_boost.Project
        """
        return reapy_boost.Project(
            cast(
                str,
                RPR.GetItemProjectContext(  # type:ignore
                    self.id
                )
            )
        )

    def set_info_value(
        self, param_name: str, value: Union[bool, int, float]
    ) -> None:
        """
        Set raw item info value.

        Parameters
        ----------
        param_name : str
        value : float
        """
        RPR.SetMediaItemInfo_Value(self.id, param_name, value)  # type:ignore

    def split(self, position: float) -> Tuple['Item', 'Item']:
        """
        Split item and return left and right parts.

        Parameters
        ----------
        position : float
            Split position in seconds.

        Returns
        -------
        left, right : Item
            Left and right parts of the split.
        """
        right_id = RPR.SplitMediaItem(self.id, position)  # type:ignore
        left, right = self, Item(right_id)
        return left, right

    @property
    def takes(self) -> List['reapy_boost.Take']:
        """
        Return list of all takes of media item.

        Returns
        -------
        takes : list of Take
            List of all takes of media item.
        """
        return self._takes_inside()

    @reapy_boost.inside_reaper()
    def _takes_inside(self) -> List['reapy_boost.Take']:
        n_takes = RPR.GetMediaItemNumTakes(self.id)  # type:ignore
        take_ids = [
            RPR.GetMediaItemTake(  # type:ignore
                self.id, i
            ) for i in range(n_takes)
        ]
        takes = [reapy_boost.Take(take_id) for take_id in take_ids]
        return takes

    @property
    def track(self) -> 'reapy_boost.Track':
        """
        Parent track of item.

        Set it by passing a track, or a track index.

        :type: Track

        Examples
        --------
        >>> track0, track1 = project.tracks[0:2]
        >>> item = track0.items[0]
        >>> item.track == track0
        True
        >>> item.track = track1  # Move to track 1
        >>> item.track = 0  # Move to track 0
        """
        return self._track_inside()

    @reapy_boost.inside_reaper()
    def _track_inside(self) -> 'reapy_boost.Track':
        track_id = RPR.GetMediaItemTrack(self.id)  # type:ignore
        track = reapy_boost.Track(track_id)
        return track

    @track.setter
    def track(self, track: 'reapy_boost.Track') -> None:
        if isinstance(track, int):
            track = reapy_boost.Track(track, project=self.project)
        RPR.MoveMediaItemToTrack(self.id, track.id)  # type:ignore

    def update(self) -> None:
        """Update item in REAPER interface."""
        RPR.UpdateItemInProject(self.id)  # type:ignore
