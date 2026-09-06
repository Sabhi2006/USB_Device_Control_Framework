from pathlib import Path
from datetime import datetime


class SecurityReporter:
    def __init__(self, log_file="logs/usb_activity.log"):
        self.log_file = Path(log_file)

    def read_events(self):
        """Read all recorded security events."""
        if not self.log_file.exists():
            return []

        with open(self.log_file, "r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    def generate_summary(self, events):
        """Count different types of security events."""
        summary = {
            "USB_CONNECTED": 0,
            "USB_DISCONNECTED": 0,
            "FILE_CREATED": 0,
            "FILE_MODIFIED": 0,
            "FILE_DELETED": 0,
            "INTEGRITY_BASELINE_CREATED": 0,
            "INTEGRITY_CHECK_PASSED": 0,
            "INTEGRITY_MODIFIED": 0,
        }

        for event in events:
            for event_type in summary:
                if event_type in event:
                    summary[event_type] += 1

        return summary

    def generate_report(self):
        """Generate a readable security audit report."""
        events = self.read_events()
        summary = self.generate_summary(events)

        report = []
        report.append("=" * 60)
        report.append("USB DEVICE CONTROL FRAMEWORK")
        report.append("SECURITY AUDIT REPORT")
        report.append("=" * 60)
        report.append(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report.append("")

        report.append("EVENT SUMMARY")
        report.append("-" * 60)

        report.append(
            f"USB Connected:              {summary['USB_CONNECTED']}"
        )
        report.append(
            f"USB Disconnected:           {summary['USB_DISCONNECTED']}"
        )
        report.append(
            f"Files Created:              {summary['FILE_CREATED']}"
        )
        report.append(
            f"Files Modified:             {summary['FILE_MODIFIED']}"
        )
        report.append(
            f"Files Deleted:              {summary['FILE_DELETED']}"
        )
        report.append(
            f"Integrity Baselines:        "
            f"{summary['INTEGRITY_BASELINE_CREATED']}"
        )
        report.append(
            f"Integrity Checks Passed:    "
            f"{summary['INTEGRITY_CHECK_PASSED']}"
        )
        report.append(
            f"Integrity Violations:       "
            f"{summary['INTEGRITY_MODIFIED']}"
        )

        report.append("")
        report.append("SECURITY STATUS")
        report.append("-" * 60)

        if summary["INTEGRITY_MODIFIED"] > 0:
            report.append(
                "[!] WARNING: File integrity violations detected"
            )
        else:
            report.append("[+] No file integrity violations detected")

        report.append("")
        report.append("RECENT SECURITY EVENTS")
        report.append("-" * 60)

        if events:
            for event in events[-10:]:
                report.append(event)
        else:
            report.append("No security events recorded.")

        report.append("=" * 60)

        return "\n".join(report)

    def save_report(self, output_file="reports/security_audit_report.txt"):
        """Save the generated report to a text file."""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = self.generate_report()

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(report)

        print(report)
        print(f"\n[+] Report saved to: {output_path}")


if __name__ == "__main__":
    reporter = SecurityReporter()
    reporter.save_report()