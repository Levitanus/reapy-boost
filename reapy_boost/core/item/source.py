from typing import Tuple, cast
import reapy_boost
from reapy_boost import reascript_api as RPR
from reapy_boost.core import ReapyObject


class Source(ReapyObject):

    def __init__(self, id: str) -> None:
        self.id = id

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Source) and self.id == other.id

    @property
    def _args(self) -> Tuple[str]:
        return self.id,

    def delete(self) -> None:
        """
        Delete source. Be sure that no references to source remains.
        """
        RPR.PCM_Source_Destroy(self.id)  # type:ignore

    @property
    def filename(self) -> str:
        """
        Return source file name.

        Returns
        -------
        filename : str
            Source file name.
        """
        _, filename, _ = RPR.GetMediaSourceFileName(  # type:ignore
            self.id, "", 10**5)
        return filename

    @property
    def has_valid_id(self) -> bool:
        """
        Whether ReaScript ID is still valid.

        For instance, if source has been deleted, ID will not be valid
        anymore.

        :type: bool
        """
        return self._has_valid_id_inside()

    @reapy_boost.inside_reaper()
    def _has_valid_id_inside(self) -> bool:
        pointer, name = self._get_pointer_and_name()
        return any(
            RPR.ValidatePtr2(project.id, pointer, name)  # type:ignore
            for project in reapy_boost.get_projects()
        )

    def length(self, unit: str = "seconds") -> float:
        """
        Return source length in `unit`.

        Parameters
        ----------
        unit : {"beats", "seconds"}

        Returns
        -------
        length : float
            Source length in `unit`.
        """
        length, _, is_quantized = RPR.GetMediaSourceLength(  # type:ignore
            self.id, 0)
        length = cast(float, length)
        if is_quantized:
            if unit == "beats":
                return length
            else:
                # elif unit == "seconds":
                raise NotImplementedError()
        else:
            if unit == "beats":
                raise NotImplementedError()
            else:
                # elif unit == "seconds":
                return length

    @property
    def n_channels(self) -> int:
        """
        Return number of channels in source media.

        Returns
        -------
        n_channels : int
            Number of channels in source media.
        """
        n_channels = RPR.GetMediaSourceNumChannels(self.id)  # type:ignore
        return n_channels

    @property
    def sample_rate(self) -> int:
        """
        Return source sample rate.

        Returns
        -------
        sample_rate : int
            Source sample rate.
        """
        sample_rate = RPR.GetMediaSourceSampleRate(self.id)  # type:ignore
        return sample_rate

    @property
    def type(self) -> str:
        """
        Return source type ("WAV, "MIDI", etc.).

        Returns
        -------
        type : str
            Source type.
        """
        _, type, _ = RPR.GetMediaSourceType(self.id, "", 10**5)  # type:ignore
        return type
