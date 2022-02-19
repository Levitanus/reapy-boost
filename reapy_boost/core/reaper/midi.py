import reapy_boost
import reapy_boost.reascript_api as RPR
import typing as ty


def get_active_editor() -> ty.Optional[reapy_boost.MIDIEditor]:
    """
    Return active MIDI editor, or None if no editor is active.

    Returns
    -------
    editor : MIDIEditor or None
        Active MIDI editor, or None if no editor is active.
    """
    editor = reapy_boost.MIDIEditor(RPR.MIDIEditor_GetActive())  # type:ignore
    if not editor._is_defined:
        editor = None
    return editor


@reapy_boost.inside_reaper()
def get_input_names() -> ty.List[str]:
    """
    Return names of all input channels.

    Returns
    -------
    names : list of str
        Names of input channels.
    """
    n_channels = reapy_boost.midi.get_n_inputs()
    return [
        RPR.GetMIDIInputName(  # type:ignore
            i, "", 2048
        )[2] for i in range(n_channels)
    ]


def get_max_inputs() -> int:
    """
    Return maximum number of MIDI inputs.

    Returns
    -------
    max_inputs : int
        Maximum number of MIDI inputs.
    """
    max_inputs = RPR.GetMaxMidiInputs()  # type:ignore
    return max_inputs


def get_max_outputs() -> int:
    """
    Return maximum number of MIDI outputs.

    Returns
    -------
    max_outputs : int
        Maximum number of MIDI outputs.
    """
    max_outputs = RPR.GetMaxMidiOutputs()  # type:ignore
    return max_outputs


def get_n_inputs() -> int:
    """
    Return number of MIDI inputs.

    Returns
    -------
    n_inputs : int
        Number of MIDI inputs.
    """
    n_inputs = RPR.GetNumMIDIInputs()  # type:ignore
    return n_inputs


def get_n_outputs() -> int:
    """
    Return number of MIDI outputs.

    Returns
    -------
    n_outputs : int
        Number of MIDI outputs.
    """
    n_outputs = RPR.GetNumMIDIOutputs()  # type:ignore
    return n_outputs


@reapy_boost.inside_reaper()
def get_output_names() -> ty.List[str]:
    """
    Return names of all output channels.

    Returns
    -------
    names : list of str
        Names of output channels.
    """
    n_channels = reapy_boost.midi.get_n_outputs()
    return [
        RPR.GetMIDIOutputName(  # type:ignore
            i, "", 2048
        )[2] for i in range(n_channels)
    ]


def reinit() -> None:
    """Reset all MIDI devices."""
    RPR.midi_reinit()  # type:ignore
