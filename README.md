# USB Device Control & Monitoring Framework

A Windows-based cybersecurity framework designed to detect, monitor,
and audit USB activity through device identification, authorization
policies, file activity monitoring, integrity verification, security
alerts, and reporting.

## Project Overview

USB devices can introduce security risks such as unauthorized data
transfer, malware introduction, and misuse of portable storage.

This project provides a practical endpoint security framework that
monitors USB activity, identifies connected devices, applies
authorization policies, and records security events for auditing.

The framework is developed using Python and Windows system tools.

## Objectives

- Detect USB device connections and disconnections.
- Identify USB devices using hardware identifiers.
- Maintain allowlist and blocklist policies.
- Detect unauthorized USB devices.
- Apply authorization decisions to USB activity.
- Monitor file operations on USB storage devices.
- Verify file integrity using SHA-256 hashing.
- Generate security alerts for suspicious activity.
- Record security events with timestamps.
- Generate audit logs and security reports.
- Demonstrate practical blue-team endpoint monitoring techniques.

## Features

### 1. USB Device Discovery

- Discovers USB devices currently recognized by Windows.
- Retrieves device status, class, friendly name, and instance ID.
- Uses Windows Plug and Play information for device identification.

### 2. Real-Time USB Monitoring

- Detects USB device connections.
- Detects USB device disconnections.
- Records device information for each event.
- Maintains a timestamped activity log.

### 3. Device Identification & Fingerprinting

- Extracts Vendor ID (VID).
- Extracts Product ID (PID).
- Extracts Serial Number where available.
- Uses device identifiers to support authorization decisions.

### 4. Allowlist / Blocklist

- Maintains approved device records.
- Maintains blocked device records.
- Compares detected devices against configured policies.
- Records authorization decisions.

### 5. Unauthorized Device Detection

- Identifies devices that do not match the approved policy.
- Records unauthorized connection attempts.
- Generates security alerts for suspicious activity.

### 6. Device Control

- Applies configured authorization decisions to detected devices.
- Records enforcement-related security events.
- Supports controlled testing of authorization decisions.

> **Note:** The current prototype demonstrates detection, policy
> evaluation, and alerting. Automatic Windows USB-device disabling
> is not claimed as a completed feature.

### 7. File Activity Monitoring

- Monitors file operations on USB storage devices.
- Records file creation, modification, and deletion events.
- Records relevant file paths and timestamps.
- Supports auditing of file movement activity.

### 8. File Integrity Monitoring

- Creates SHA-256 file integrity baselines.
- Verifies whether files remain unchanged.
- Detects file modifications.
- Records integrity verification results.

### 9. Security Alerting

- Generates alerts for unauthorized USB devices.
- Generates alerts for file integrity violations.
- Records alert timestamps and affected resources.
- Supports security event investigation.

### 10. Security Logging

- Maintains timestamped USB activity records.
- Records device information and security actions.
- Stores monitoring results for later analysis.

### 11. Security Reporting

- Generates security audit reports.
- Summarizes USB activity and integrity events.
- Displays recent security events.
- Provides evidence of detected suspicious activity.

### 12. Security Dashboard

- Displays USB connection statistics.
- Displays file activity statistics.
- Displays integrity violation counts.
- Displays recent security events.
- Supports dashboard refresh.

## Project Architecture

```text
USB Device Connected / Disconnected
                |
                v
       USB Event Monitor
                |
                v
       Device Identification
       VID / PID / Serial / ID
                |
                v
        Authorization Engine
        Allowlist / Blocklist
                |
          +-----+-----+
          |           |
          v           v
        ALLOW       UNAUTHORIZED
          |           |
          v           v
   File Activity   Security Alerts
    Monitoring          |
          |             |
          v             |
   File Integrity       |
    Monitoring          |
          |             |
          +-----+-------+
                |
                v
         Security Logger
                |
                v
         Report Generator
                |
                v
          Audit Report
                |
                v
       Security Dashboard
```

## Technologies Used

- Python
- Windows PowerShell
- Windows Plug and Play / WMI
- JSON
- File System Monitoring
- SHA-256 Hashing
- Tkinter
- Git & GitHub

## Project Structure

```text
USB_Device_Control_Framework/
│
├── config/
│   ├── allowlist.json
│   └── blocklist.json
│
├── logs/
│   └── usb_activity.log
│
├── reports/
│   └── security_audit_report.txt
│
├── screenshots/
│   ├── policy_engine1.png
│   ├── file_monitoring.png
│   ├── integrity_monitoring.png
│   ├── security_audit_report.png
│   ├── security_dashboard.png
│   ├── security_alerts.png
│   └── integration_test.png
│
├── usb_monitor.py
├── device_manager.py
├── policy_engine.py
├── file_monitor.py
├── integrity_monitor.py
├── alert_manager.py
├── reporter.py
├── dashboard.py
├── integration_test.py
├── authorization_test.py
├── config.py
├── logger.py
├── main.py
└── README.md
```

## How to Run

### 1. Clone the repository

```powershell
git clone https://github.com/Sabhi2006/USB_Device_Control_Framework.git
```

### 2. Open the project directory

```powershell
cd USB_Device_Control_Framework
```

### 3. Run USB monitoring

```powershell
python usb_monitor.py
```

### 4. Run authorization testing

```powershell
python authorization_test.py
```

### 5. Run file monitoring

```powershell
python file_monitor.py
```

### 6. Run integrity monitoring

```powershell
python integrity_monitor.py
```

### 7. Generate security reports

```powershell
python reporter.py
```

### 8. Launch the security dashboard

```powershell
python dashboard.py
```

### 9. Run integration testing

```powershell
python integration_test.py
```

## Testing

The framework was tested using simulated USB device identifiers
and controlled file operations.

### Test Results

- USB device connection and disconnection events detected.
- Authorized and unauthorized device decisions verified.
- File creation, modification, and deletion events recorded.
- File integrity baseline and hash verification tested.
- Integrity violations detected successfully.
- Security alerts generated for unauthorized devices and integrity violations.
- Security audit reports generated successfully.
- Dashboard displayed monitoring statistics and recent security events.
- Integration testing completed successfully.

### Sample Test Results

```text
Authorized device: True
Unauthorized device: False

Integrity check PASSED
Integrity check FAILED - File modified

ALERT | Type: UNAUTHORIZED_USB
ALERT | Type: FILE_INTEGRITY_VIOLATION

INTEGRATION TEST COMPLETED
```

## Sample Security Report

The framework generates a security audit report containing:

- USB connection and disconnection counts.
- File creation, modification, and deletion counts.
- Integrity baseline and verification results.
- Integrity violation counts.
- Recent security events.
- Security status information.

Example:

```text
============================================================
USB DEVICE CONTROL FRAMEWORK
SECURITY AUDIT REPORT
============================================================

EVENT SUMMARY
------------------------------------------------------------
USB Connected:              7
USB Disconnected:           7
Files Created:              2
Files Modified:             1
Files Deleted:              1
Integrity Baselines:        1
Integrity Checks Passed:    1
Integrity Violations:       1

SECURITY STATUS
------------------------------------------------------------
[!] WARNING: File integrity violations detected
```

## Security Applications

This framework demonstrates practical blue-team security techniques
for:

- Endpoint monitoring.
- USB device identification.
- Unauthorized device detection.
- File activity auditing.
- File integrity verification.
- Security event logging.
- Security alerting.
- Audit report generation.

## Limitations

- The current implementation is a prototype.
- Testing is performed using controlled device identifiers and file operations.
- Automatic Windows USB-device disabling is not implemented in the current prototype.
- Advanced malware detection is outside the current project scope.
- Long-term database storage is not currently implemented.

## Future Enhancements

- Real-time graphical monitoring improvements.
- Email or notification-based security alerts.
- Database integration for long-term event storage.
- Advanced device control and restriction capabilities.
- Role-based access control.
- Improved USB device fingerprinting.
- Automated security response mechanisms.
- Enhanced reporting and visualization.

## Project Status

The project is currently in the **prototype and testing stage**.

The framework demonstrates USB device monitoring, authorization
policy evaluation, file activity auditing, integrity monitoring,
security alerting, reporting, dashboard visualization, and
integration testing.

## Author

**Sabhi Kumar Gautam**

## License

This project is intended for educational and cybersecurity
internship purposes.