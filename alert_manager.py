import json
from datetime import datetime
from pathlib import Path


class AlertManager:
    def __init__(self):
        self.log_file = Path(__file__).parent / "logs" / "usb_activity.log"
        self.log_file.parent.mkdir(exist_ok=True)

    def _write_alert(self, alert_type, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        alert = (
            f"{timestamp} | ALERT | Type: {alert_type} | "
            f"Message: {message}"
        )

        print(f"[!] {alert}")

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(alert + "\n")

    def check_usb_device(self, device, authorized):
        if not authorized:
            self._write_alert(
                "UNAUTHORIZED_USB",
                f"Unauthorized device detected: {device}"
            )
            return False

        return True

    def check_integrity(self, path, integrity_passed):
        if not integrity_passed:
            self._write_alert(
                "FILE_INTEGRITY_VIOLATION",
                f"File integrity violation detected: {path}"
            )
            return False

        return True


if __name__ == "__main__":
    alert_manager = AlertManager()

    print("SECURITY ALERT TEST")
    print("=" * 50)

    # Test 1: Authorized device
    authorized_device = {
        "vid": "2717",
        "pid": "FF40"
    }

    print("\n[+] Testing authorized device...")
    print(
        "Result:",
        alert_manager.check_usb_device(
            authorized_device,
            authorized=True
        )
    )

    # Test 2: Unauthorized device
    unauthorized_device = {
        "vid": "1234",
        "pid": "5678"
    }

    print("\n[+] Testing unauthorized device...")
    print(
        "Result:",
        alert_manager.check_usb_device(
            unauthorized_device,
            authorized=False
        )
    )

    # Test 3: Integrity violation
    print("\n[+] Testing file integrity violation...")
    print(
        "Result:",
        alert_manager.check_integrity(
            "test_usb/integrity_test.txt",
            integrity_passed=False
        )
    )

    print("\n[+] Alert testing completed.")