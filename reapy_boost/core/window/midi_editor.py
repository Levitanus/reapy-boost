import reapy_boost
from reapy_boost.core.item.take import Take
import reapy_boost.reascript_api as RPR
from .window import Window


class MIDIEditor(Window):

    def _get_int_setting(self, setting: str) -> int:
        return RPR.MIDIEditor_GetSetting_int(self.id, setting)  # type:ignore

    def _get_str_setting(self, setting: str) -> str:
        return RPR.MIDIEditor_GetSetting_str(  # type:ignore
            self.id, setting, "", 2048)[3]

    @property
    def last_clicked_cc_lane(self) -> int:
        """
        Last clicked CC lane.

        :type: int
        """
        return self._get_int_setting("last_clicked_cc_lane")

    @property
    def last_clicked_cc_lane_name(self) -> str:
        """
        Last clicked CC lane name ("velocity", "pitch", etc.).

        :type: str
        """
        return self._get_str_setting("last_clicked_cc_lane")

    @property
    def active_note_row(self) -> int:
        """
        Active note row (between 0 and 127).

        :type: int
        """
        return self._get_int_setting("active_note_row")

    @property
    def default_channel(self) -> int:
        """
        Default note channel (between 0 and 15).

        :type: int
        """
        return self._get_int_setting("default_note_chan")

    @property
    def default_length(self) -> int:
        """
        Default note length in MIDI ticks.

        :type: int
        """
        return self._get_int_setting("default_note_len")

    @property
    def default_velocity(self) -> int:
        """
        Default note velocity (between 0 and 127).

        :type: int
        """
        return self._get_int_setting("default_note_vel")

    @property
    def is_scale_enabled(self) -> bool:
        """
        Whether scale is enabled in editor.

        :type: bool
        """
        return bool(self._get_int_setting("scale_enabled"))

    @property
    def is_snap_enabled(self) -> bool:
        """
        Whether snap is enabled in editor.

        :type: bool
        """
        return bool(self._get_int_setting("snap_enabled"))

    @property
    def mode(self) -> str:
        """
        Mode of MIDI editor.

        :type: {0: "piano roll", 1: "event list"}
        """
        modes = {0: "piano roll", 1: "event list"}
        return modes[RPR.MIDIEditor_GetMode(self.id)]  # type:ignore

    def perform_action(self, action_id: int) -> None:
        """
        Perform action (from MIDI Editor section).

        Parameters
        ----------
        action_id : int
            Action ID.
        """
        RPR.MIDIEditor_OnCommand(self.id, action_id)  # type:ignore

    @property
    def scale_type(self) -> str:
        """
        Scale type ID.

        :type: str
        """
        return self._get_str_setting("scale")

    @property
    def scale_root(self) -> int:
        """
        Scale root (between 0 and 12, 0=C).

        :type: int
        """
        return self._get_int_setting("scale_root")

    @property
    def take(self) -> Take:
        """
        Take currently edited.

        :type: Take
        """
        return reapy_boost.Take(RPR.MIDIEditor_GetTake(self.id))  # type:ignore
