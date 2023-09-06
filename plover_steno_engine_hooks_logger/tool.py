"""
Plover Steno Engine Hooks Logger - A Plover GUI Tool to log out the contents of
steno engine hooks using Qt signals.
"""
from plover.engine import StenoEngine
from plover.gui_qt.tool import Tool

from .hooks import StenoEngineHooksLogger

# REF: https://stackoverflow.com/a/28727066/567863
class StenoEngineHooksMetaClass(type(StenoEngineHooksLogger), type(Tool)):
    """
    Metaclass to prevent the following error:
    `TypeError: metaclass conflict: the metaclass of a derived class must be a
    (non-strict) subclass of the metaclasses of all its bases`
    """

class StenoEngineHooksLoggerGUITool(
    Tool,
    StenoEngineHooksLogger,
    metaclass= StenoEngineHooksMetaClass
):
    """
    Plover entry point GUI Tool class to log the contents of steno engine
    hooks.
    """
    TITLE = "Steno Engine\nHooks Logger"
    ICON = ''
    ROLE = "Steno Engine Hooks Logger"

    def __init__(self, engine: StenoEngine) -> None:
        Tool.__init__(self, engine)
        self._log_marker = "[STENO ENGINE HOOK (GUI)]"

        for hook in self._HOOKS:
            engine.signal_connect(hook, getattr(self, f"_{hook}"))
