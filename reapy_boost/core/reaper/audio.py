"""Audio handling functions."""

from enum import Enum
from typing import List, Tuple
import reapy_boost
import reapy_boost.reascript_api as RPR


def get_input_latency(unit: str = "second") -> float:
    """
    Return input latency.

    Parameters
    ----------
    unit : {"sample", "second"}
        Whether to return latency in samples or seconds
        (default="second").

    Returns
    -------
    latency : float
        Input latency.
    """
    latency, out_latency = RPR.GetInputOutputLatency(0, 0)  # type:ignore
    if unit == "second":
        # Small hack because RPR.GetInputLatency doesn't exist...
        latency *= RPR.GetOutputLatency() / out_latency  # type:ignore
    return latency


@reapy_boost.inside_reaper()
def get_input_names() -> Tuple[str, ...]:
    """
    Return names of all input channels.

    Returns
    -------
    names : list of str
        Names of input channels.
    """
    n_channels = reapy_boost.audio.get_n_inputs()
    return tuple(
        map(
            RPR.GetInputChannelName,  # type:ignore
            range(n_channels)
        )
    )


def get_n_inputs() -> int:
    """
    Return number of audio inputs.

    Returns
    -------
    n_inputs : int
        Number of audio inputs.
    """
    n_inputs = RPR.GetNumAudioInputs()  # type:ignore
    return n_inputs


def get_n_outputs() -> int:
    """
    Return number of audio outputs.

    Returns
    -------
    n_outputs : int
        Number of audio outputs.
    """
    n_outputs = RPR.GetNumAudioOutputs()  # type:ignore
    return n_outputs


def get_output_latency(unit: str = "second") -> float:
    """
    Return output latency.

    Parameters
    ----------
    unit : {"sample", "second"}
        Whether to return latency in samples or seconds
        (default="second").

    Returns
    -------
    latency : float
        Output latency.
    """
    latency, out_latency = RPR.GetInputOutputLatency(0, 0)  # type:ignore
    if unit == "second":
        latency = RPR.GetOutputLatency()  # type:ignore
    else:
        latency = RPR.GetInputOutputLatency(0, 0)[1]  # type:ignore
    return latency


@reapy_boost.inside_reaper()
def get_output_names() -> Tuple[str, ...]:
    """
    Return names of all output channels.

    Returns
    -------
    names : list of str
        Names of output channels.
    """
    n_channels = reapy_boost.audio.get_n_outputs()
    return tuple(
        map(
            RPR.GetOutputChannelName,  # type:ignore
            range(n_channels)
        )
    )


def init() -> None:
    """
    Open all audio and MIDI devices (if not opened).
    """
    RPR.Audio_Init()  # type:ignore


def is_prebuffer() -> bool:
    """
    Return whether audio is in pre-buffer (threadsafe).

    Returns
    -------
    is_prebuffer : bool
        Whether audio is in pre-buffer.
    """
    is_prebuffer = bool(RPR.Audio_IsPreBuffer())  # type:ignore
    return is_prebuffer


def is_running() -> bool:
    """
    Return whether audio is running (threadsafe).

    Returns
    -------
    is_running : bool
        Whether audio is running.
    """
    is_running = bool(RPR.Audio_IsRunning())  # type:ignore
    return is_running


def quit() -> None:
    """
    Close all audio and MIDI devices (if opened).
    """
    RPR.Audio_Quit()  # type:ignore
