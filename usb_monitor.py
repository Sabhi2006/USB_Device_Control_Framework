import subprocess
import json
import time
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs") / "usb_activity.log"


def discover_usb_devices():
    """Discover USB devices currently connected to Windows."""

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "Get-PnpDevice -PresentOnly | "
        "Where-Object {$_.InstanceId -like 'USB*'} | "
        "Select-Object Status, Class, FriendlyName, InstanceId | "
        "ConvertTo-Json -Depth 3"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[-] Failed to discover USB devices")
        return []

    if not result.stdout.strip():
        return []

    devices = json.loads(result.stdout)

    if isinstance(devices, dict):
        devices = [devices]

    return devices


def get_device_ids(devices):
    """Return a set of unique device IDs."""

    return {
        device.get("InstanceId")
        for device in devices
        if device.get("InstanceId")
    }


def log_event(action, device):
    """Record a USB activity event."""

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"{timestamp} | {action} | "
        f"Status: {device.get('Status')} | "
        f"Class: {device.get('Class')} | "
        f"Device: {device.get('FriendlyName')} | "
        f"InstanceId: {device.get('InstanceId')}\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_entry)

    print(log_entry.strip())


def monitor_usb_events():
    """Monitor USB device connections and disconnections."""

    print("=" * 60)
    print("REAL-TIME USB MONITORING")
    print("=" * 60)
    print("[+] Monitoring started")
    print("[+] Connect or disconnect a USB device to test")
    print("[+] Press Ctrl+C to stop")
    print("=" * 60)

    previous_devices = discover_usb_devices()
    previous_ids = get_device_ids(previous_devices)

    try:
        while True:

            time.sleep(2)

            current_devices = discover_usb_devices()
            current_ids = get_device_ids(current_devices)

            connected_ids = current_ids - previous_ids
            disconnected_ids = previous_ids - current_ids

            for device in current_devices:
                if device.get("InstanceId") in connected_ids:
                    log_event("USB_CONNECTED", device)

            for device in previous_devices:
                if device.get("InstanceId") in disconnected_ids:
                    log_event("USB_DISCONNECTED", device)

            previous_devices = current_devices
            previous_ids = current_ids

    except KeyboardInterrupt:
        print("\n[+] USB monitoring stopped")


def main():
    monitor_usb_events()


if __name__ == "__main__":
    main()