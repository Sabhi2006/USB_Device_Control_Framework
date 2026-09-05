import hashlib
from pathlib import Path
from datetime import datetime


class IntegrityMonitor:
    def __init__(self, log_file="logs/usb_activity.log"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def calculate_hash(self, file_path):
        """Calculate the SHA-256 hash of a file."""
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    def log_event(self, event_type, file_path, old_hash="", new_hash=""):
        """Record an integrity event."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = (
            f"{timestamp} | FILE_INTEGRITY_{event_type} | "
            f"Path: {file_path}"
        )

        if old_hash:
            message += f" | OldHash: {old_hash}"

        if new_hash:
            message += f" | NewHash: {new_hash}"

        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(message + "\n")

        print(message)

    def create_baseline(self, file_path):
        """Create and return the original file hash."""
        file_hash = self.calculate_hash(file_path)

        print(f"[+] Baseline hash created: {file_hash}")

        self.log_event("BASELINE_CREATED", file_path, new_hash=file_hash)

        return file_hash

    def verify_integrity(self, file_path, original_hash):
        """Compare the current hash with the original hash."""
        current_hash = self.calculate_hash(file_path)

        if current_hash == original_hash:
            print("[+] Integrity check PASSED")
            self.log_event("CHECK_PASSED", file_path, new_hash=current_hash)
            return True

        print("[!] Integrity check FAILED - File modified")
        self.log_event(
            "MODIFIED",
            file_path,
            old_hash=original_hash,
            new_hash=current_hash
        )

        return False


if __name__ == "__main__":
    monitor = IntegrityMonitor()

    test_file = Path("test_usb/integrity_test.txt")
    test_file.parent.mkdir(parents=True, exist_ok=True)

    test_file.write_text("Original USB file content", encoding="utf-8")

    print("=" * 60)
    print("FILE INTEGRITY MONITORING")
    print("=" * 60)

    original_hash = monitor.create_baseline(test_file)

    print("\n[+] Checking unchanged file...")
    monitor.verify_integrity(test_file, original_hash)

    test_file.write_text("Modified USB file content", encoding="utf-8")

    print("\n[+] Checking modified file...")
    monitor.verify_integrity(test_file, original_hash)

    print("=" * 60)