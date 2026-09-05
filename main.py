
from usb_monitor import discover_usb_devices


def main():
    print("=" * 60)
    print("USB DEVICE CONTROL & MONITORING FRAMEWORK")
    print("=" * 60)

    print("[+] USB monitoring module: Active")
    print("[+] Discovering connected USB devices...")

    devices = discover_usb_devices()

    for device in devices:
        print(f"Status       : {device.get('Status')}")
        print(f"Class        : {device.get('Class')}")
        print(f"FriendlyName : {device.get('FriendlyName')}")
        print(f"InstanceId   : {device.get('InstanceId')}")
        print("-" * 60)

    print(f"[+] Total USB devices detected: {len(devices)}")
    print("[+] USB discovery completed")

    print("=" * 60)


if __name__ == "__main__":
    main()