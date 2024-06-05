import psutil

def detect_keylogger_linux():
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            # Check for suspicious process names
            if "keylogger" in process_name.lower():
                print("Suspicious process found:", process_name)
        except psutil.AccessDenied:
            pass
