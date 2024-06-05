import pyHook
import pythoncom

def OnKeyboardEvent(event):
    print('Key:', event.Key)
    return True

def detect_keylogger_windows():
    hook_manager = pyHook.HookManager()
    hook_manager.KeyDown = OnKeyboardEvent
    hook_manager.HookKeyboard()
    pythoncom.PumpMessages()
