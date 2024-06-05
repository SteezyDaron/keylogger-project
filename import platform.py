import platform

def main():
    os_type = platform.system()
    if os_type == "Linux":
        detect_keylogger_linux()
    elif os_type == "Windows":
        detect_keylogger_windows()
    else:
        print("Unsupported operating system:", os_type)

if __name__ == "__main__":
    main()
