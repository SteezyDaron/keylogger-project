from evdev import InputDevice, ecodes

def detect_keylogger_linux():
    devices = [InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        print(device.name)
        try:
            for event in device.read_loop():
                if event.type == ecodes.EV_KEY:
                    print(evdev.categorize(event))
        except:
            pass
