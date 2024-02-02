"""
Plover Steno Engine Hooks Logger - A Plover GUI Tool to log out the contents of
steno engine hooks using Qt signals.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from plover import log
from plover.formatting import _Action
from plover.steno import Stroke
from plover.steno_dictionary import StenoDictionaryCollection


class StenoEngineHooksLogger(ABC):
    """
    Contains implementation code for logging out contents of Plover steno engine
    hooks.
    """

    _HOOKS = [
        "add_translation",
        "config_changed",
        "configure",
        "dictionaries_loaded",
        "focus",
        "lookup",
        "machine_state_changed",
        "output_changed",
        "quit",
        "send_backspaces",
        "send_key_combination",
        "send_string",
        "stroked",
        "suggestions",
        "translated",
    ]

    @abstractmethod
    def __init__(self) -> None:
        self._log_marker = "[STENO ENGINE HOOK]"

    def _add_translation(self) -> None:
        """
        The Add Translation command was activated – open the Add Translation
        tool.
        """
        log.info(f"{self._log_marker}: add_translation() called")

    def _config_changed(self, config: Dict[str, Any]) -> None:
        """
        The configuration was changed, or it was loaded for the first time.
        `config` is a dictionary containing only the changed fields.
        """
        log.info(
            f"{self._log_marker} "
            "config_changed(config: Dict[str, any]) called"
        )
        log.info(f"{self._log_marker}     config: {config}")

    def _configure(self) -> None:
        """
        The Configure command was activated – open the configuration window.
        """
        log.info(f"{self._log_marker} configure() called")

    def _dictionaries_loaded(
        self,
        dictionaries: StenoDictionaryCollection
    ) -> None:
        """
        The dictionaries were loaded, either when Plover starts up or the system
        is changed or when the engine is reset.
        """
        log.info(
            f"{self._log_marker} "
            "dictionaries_loaded(dictionaries: StenoDictionaryCollection) "
            "called"
        )
        log.info(f"{self._log_marker}     dictionaries: {dictionaries}")

    def _focus(self) -> None:
        """
        The Show command was activated – reopen Plover's main window and bring
        it to the front.
        """
        log.info(f"{self._log_marker} focus() called")

    def _lookup(self) -> None:
        """
        The Lookup command was activated – open the Lookup tool.
        """
        log.info(f"{self._log_marker} lookup() called")

    def _machine_state_changed(
        self,
        machine_type: str,
        machine_state: str
    ) -> None:
        """
        Either the machine type was changed by the user, or the connection state
        of the machine changed. `machine_type` is the name of the machine (e.g.
        Gemini PR), and `machine_state` is one of `stopped`, `initializing`,
        `connected` or `disconnected`.
        """
        log.info(
            f"{self._log_marker} "
            "machine_state_changed(machine_type: str, machine_state: str) "
            "called"
        )
        log.info(f"{self._log_marker}     machine_type: {machine_type}")
        log.info(f"{self._log_marker}     machine_state: {machine_state}")

    def _output_changed(self, enabled: bool) -> None:
        """
        The user requested to either enable or disable steno output. `enabled`
        is `True` if output is enabled, `False` otherwise.
        """
        log.info(f"{self._log_marker} output_changed(enabled: bool) called")
        log.info(f"{self._log_marker}     enabled: {enabled}")

    def _quit(self) -> None:
        """
        The Quit command was activated – wrap up any pending tasks and quit
        Plover.
        """
        log.info(f"{self._log_marker} quit() called")

    def _send_backspaces(self, b: int) -> None:
        """
        Plover just sent backspaces over keyboard output. `b` is the number of
        backspaces sent.
        """
        log.info(f"{self._log_marker} send_backspaces(b: int) called")
        log.info(f"{self._log_marker}     b: {b}")

    def _send_key_combination(self, c: str) -> None:
        """
        Plover just sent a keyboard combination over keyboard output. `c` is a
        string representing the keyboard combination, for example `Alt_L(Tab)`
        """
        log.info(f"{self._log_marker} send_key_combination(c: str) called")
        log.info(f"{self._log_marker}     c: {c}")

    def _send_string(self, s: str) -> None:
        """
        Plover just sent the string `s` over keyboard output.
        """
        log.info(f"{self._log_marker} send_string(s: str) called")
        log.info(f"{self._log_marker}     s: {s}")

    def _stroked(self, stroke: Stroke) -> None:
        """
        The user just sent a stroke.
        """
        log.info(f"{self._log_marker} stroked(stroke: Stroke) called")
        log.info(f"{self._log_marker}     stroke: {stroke}")

    def _suggestions(self) -> None:
        """
        The Suggestions command was activated – open the Suggestions tool.
        """
        log.info(f"{self._log_marker} suggestions() called")

    def _translated(self, old: List[_Action], new: List[_Action]) -> None:
        """
        A stroke was able to be translated.
        """
        log.info(
            f"{self._log_marker} "
            "translated(old: List[_Action], new: List[_Action])) called"
        )
        log.info(f"{self._log_marker}     old: {old}")
        log.info(f"{self._log_marker}     new: {new}")
