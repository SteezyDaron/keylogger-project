import winreg

def detect_keylogger_windows():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
    for i in range(1024):
        try:
            value_name, value_data, value_type = winreg.EnumValue(key, i)
            if "keylogger" in value_name.lower() or "keylogger" in value_data.lower():
                print("Suspicious registry key found:", value_name, value_data)
        except OSError:
            break
