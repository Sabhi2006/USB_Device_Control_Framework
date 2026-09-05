import os
import time
from pathlib import Path
from datetime import datetime


class FileMonitor:
    def __init__(self, folder_path, log_file="logs/usb_activity.log"):
        self.folder_path = Path(folder_path)
        self.log_file = Path(log_file)

        self.folder_path.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.previous_files = self._get_files()

    def _get_files(self):
        """Return the files currently present in the monitored folder."""
        return {
            str(file): file.stat().st_mtime
            for file in self.folder_path.rglob("*")
            if file.is_file()
        }

    def _log_event(self, event_type, file_path):
        """Record a file activity event."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = (
            f"{timestamp} | FILE_{event_type} | "
            f"Path: {file_path}"
        )

        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(message + "\n")

        print(message)

    def check_for_changes(self):
        """Detect newly created, modified, and deleted files."""
        current_files = self._get_files()

        # Detect newly created files
        for file_path in current_files:
            if file_path not in self.previous_files:
                self._log_event("CREATED", file_path)

        # Detect modified files
        for file_path in current_files:
            if file_path in self.previous_files:
                if current_files[file_path] != self.previous_files[file_path]:
                    self._log_event("MODIFIED", file_path)

        # Detect deleted files
        for file_path in self.previous_files:
            if file_path not in current_files:
                self._log_event("DELETED", file_path)

        self.previous_files = current_files

    def start_monitoring(self, interval=2):
        """Continuously monitor the folder."""
        print("=" * 60)
        print("FILE ACTIVITY MONITORING")
        print("=" * 60)
        print(f"[+] Monitoring folder: {self.folder_path}")
        print("[+] Create, modify, or delete a file to test")
        print("[+] Press Ctrl+C to stop")
        print("=" * 60)

        try:
            while True:
                self.check_for_changes()
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n[+] File monitoring stopped")


if __name__ == "__main__":
    monitor = FileMonitor("test_usb")
    monitor.start_monitoring()