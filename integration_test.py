from pathlib import Path

from usb_monitor import discover_usb_devices
from policy_engine import PolicyEngine
from file_monitor import FileMonitor
from integrity_monitor import IntegrityMonitor
from reporter import SecurityReporter
from alert_manager import AlertManager


def main():
    print("=" * 60)
    print("USB DEVICE CONTROL FRAMEWORK - INTEGRATION TEST")
    print("=" * 60)

    # 1. USB discovery
    print("\n[1] USB DEVICE DISCOVERY")
    devices = discover_usb_devices()
    print(f"[+] Devices detected: {len(devices)}")

    # 2. Authorization and alerts
    print("\n[2] AUTHORIZATION & ALERT TEST")
    policy = PolicyEngine()
    alerts = AlertManager()

    authorized_device = {"vid": "2717", "pid": "FF40"}
    unauthorized_device = {"vid": "1234", "pid": "5678"}

    print("[+] Authorized device:",
          policy.is_authorized(authorized_device))

    print("[+] Unauthorized device:",
          policy.is_authorized(unauthorized_device))

    alerts.check_usb_device(
        unauthorized_device,
        policy.is_authorized(unauthorized_device)
    )

    # 3. File activity monitoring
    print("\n[3] FILE ACTIVITY MONITORING")
    test_folder = Path("test_usb")
    test_file = test_folder / "integration_test.txt"

    monitor = FileMonitor(test_folder)

    test_file.write_text("Initial content", encoding="utf-8")
    monitor.check_for_changes()

    test_file.write_text("Modified content", encoding="utf-8")
    monitor.check_for_changes()

    test_file.unlink()
    monitor.check_for_changes()

    print("[+] File activity test completed")

    # 4. File integrity monitoring
    print("\n[4] FILE INTEGRITY MONITORING")
    integrity_file = test_folder / "integrity_test.txt"
    integrity_file.write_text("Original content", encoding="utf-8")

    integrity = IntegrityMonitor()
    original_hash = integrity.create_baseline(integrity_file)

    passed = integrity.verify_integrity(
        integrity_file,
        original_hash
    )

    print("[+] Integrity check passed:", passed)

    integrity_file.write_text("Modified content", encoding="utf-8")

    passed = integrity.verify_integrity(
        integrity_file,
        original_hash
    )

    print("[+] Integrity check passed:", passed)

    alerts.check_integrity(
        integrity_file,
        passed
    )

    # 5. Security report
    print("\n[5] SECURITY REPORT")
    reporter = SecurityReporter()
    reporter.save_report()

    print("\n[+] INTEGRATION TEST COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()