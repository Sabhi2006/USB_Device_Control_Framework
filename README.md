# USB Device Control & Monitoring Framework

A Windows-based cybersecurity framework designed to detect, monitor,
and restrict unauthorized USB activity through device identification,
policy enforcement, file activity auditing, and security reporting.

---

## Project Overview

USB devices can introduce security risks such as unauthorized data
transfer, malware introduction, and misuse of portable storage.

This project provides a practical endpoint security framework that
monitors USB activity, identifies connected devices, applies
authorization policies, and records security events for auditing.

The framework is developed using Python and Windows system tools.

---

## Objectives

- Detect USB device connections and disconnections.
- Identify USB devices using hardware identifiers.
- Maintain allowlist and blocklist policies.
- Detect unauthorized USB devices.
- Restrict suspicious or unauthorized USB activity.
- Monitor file operations on USB storage devices.
- Record security events with timestamps.
- Generate audit logs and security reports.
- Demonstrate practical blue-team endpoint monitoring techniques.

---

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

- Applies the configured restriction policy to unauthorized
  USB devices.
- Records enforcement actions.
- Supports controlled testing of device access restrictions.

### 7. File Activity Monitoring

- Monitors file operations on USB storage devices.
- Records file creation, modification, and deletion events.
- Records relevant file paths and timestamps.
- Supports auditing of file movement activity.

### 8. Security Logging

- Maintains timestamped USB activity records.
- Records device information and security actions.
- Stores monitoring results for later analysis.

### 9. Reporting

- Generates security audit reports.
- Summarizes USB activity and policy decisions.
- Provides evidence of detected and restricted activity.

---

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
        ALLOW       BLOCK
          |           |
          v           v
   File Activity   Device Control
     Monitoring    / Restriction
          |           |
          +-----+-----+
                |
                v
         Security Logger
                |
                v
         Report Generator
                |
                v
          Audit Report