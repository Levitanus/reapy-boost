from typing import List, Tuple
import reapy_boost
import reapy_boost.reascript_api as RPR
from reapy_boost.core import ReapyObject


class AudioAccessor(ReapyObject):

    def __init__(self, id: int) -> None:
        self.id = id

    @property
    def _args(self) -> Tuple[int]:
        return self.id,

    def delete(self) -> None:
        """Delete audio accessor."""
        RPR.DestroyAudioAccessor(self.id)  # type:ignore

    @property
    def end_time(self) -> float:
        """
        End time of audio that can be returned from this accessor.

        Return value is in seconds.

        :type: float
        """
        return RPR.GetAudioAccessorEndTime(self.id)  # type:ignore

    def get_samples(
        self,
        start: float,
        n_samples_per_channel: int,
        n_channels: int = 1,
        sample_rate: int = 44100
    ) -> List[float]:
        """
        Return audio samples.

        Parameters
        ----------
        start : float
            Start time in seconds.
        n_samples_per_channel : int
            Number of required samples per channel
        n_channels : int, optional
            Number of required channels (default=1).
        sample_rate : float, optional
            Required sample rate (default=44100).

        Returns
        -------
        samples : list
            List of length n_samples*n_channels.

        Examples
        --------
        To separate channels use:

        >>> samples = audio_accessor.get_samples(0, 1024, 2)
        >>> first_channel = samples[::2]
        >>> second_channel = samples[1::2]
        """
        buffer = [0] * n_channels * n_samples_per_channel
        samples = RPR.GetAudioAccessorSamples(  # type:ignore
            self.id, sample_rate, n_channels, start, n_samples_per_channel,
            buffer
        )[1]
        return samples

    @property
    def has_state_changed(self) -> float:
        """
        Whether underlying state has changed.

        :type: bool
        """
        return bool(RPR.AudioAccessorValidateState(self.id))  # type:ignore

    def hash(self) -> str:
        """
        String that changes only if the underlying samples change.

        :type: str
        """
        return RPR.GetAudioAccessorHash(self.id, "")[1]  # type:ignore

    @property
    def start_time(self) -> float:
        """
        Start time of audio that can be returned from this accessor.

        Return value is in seconds.

        :type: float
        """
        return RPR.GetAudioAccessorStartTime(self.id)  # type:ignore
