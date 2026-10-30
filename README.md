<div align="center">

#  macOS Recovery Downloader & USB Provisioner

### Automated 1-Click Tool for Downloading Official Apple macOS Recovery Images
*Direct from Apple Content Delivery Network (CDN) Servers*

---

[![macOS](https://img.shields.io/badge/macOS-Tahoe%20%7C%20Sequoia%20%7C%20Sonoma-blue?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh)
[![Verification](https://img.shields.io/badge/Verification-Apple%20SHA--256%20Chunklist-orange?style=for-the-badge&logo=securityscorecard&logoColor=white)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh)

</div>

---

## ⚡ Quick 1-Click Launch

### On Windows
Simply double-click:
```text
Download-Recovery.bat
```
*(Or right-click `Download-Recovery.ps1` and select **Run with PowerShell**).*

### On macOS / Linux
Open Terminal in this directory and execute:
```bash
python3 download_recovery.py
```

---

## 🖥️ Interactive GUI / Menu Preview

```text
======================================================================
       macOS Official Recovery Image Downloader & Deployer      
         Optimized for OpenCore 1.0.8 Hackintosh Systems          
======================================================================

Available macOS Recovery Versions:
  [1] macOS 16 Tahoe (Latest)
  [2] macOS 15 Sequoia
  [3] macOS 14 Sonoma
  [4] macOS 13 Ventura
  [5] macOS 12 Monterey
  [6] macOS 11 Big Sur
  [Q] Quit

Select an option (1-6, default: 1): 1

Connecting directly to Apple CDN servers...
----------------------------------------------------------------------
Saving http://oscdn.apple.com/.../BaseSystem.chunklist ... 100%
Saving http://oscdn.apple.com/.../BaseSystem.dmg ...       100%
----------------------------------------------------------------------
Image verification complete!

✅ Download Verified!
  • BaseSystem.dmg:       916.0 MB
  • BaseSystem.chunklist: 3604 bytes

Detected Removable USB Drive(s): D:
Would you like to copy recovery files directly to your USB drive? (Y/n): Y
Deploying recovery files to D:\com.apple.recovery.boot...
✅ Successfully deployed to D:\com.apple.recovery.boot!
```

---

## 📋 Board ID & Model Reference Matrix

For advanced users or manual scripts, here are the exact Apple Board IDs and MLBs used by this utility:

| macOS Version | Marketing Name | Apple Board ID | Target MLB | OS Type |
| :--- | :--- | :--- | :--- | :---: |
| **macOS 16** | **Tahoe** | `Mac-CFF7D910A743CAAF` | `00000000000000000` | `latest` |
| **macOS 15** | **Sequoia** | `Mac-7BA5B2D9E42DDD94` | `00000000000000000` | `default` |
| **macOS 14** | **Sonoma** | `Mac-827FAC58A8FDFA22` | `00000000000000000` | `default` |
| **macOS 13** | **Ventura** | `Mac-B4831CEBD52A0C4C` | `00000000000000000` | `default` |
| **macOS 12** | **Monterey** | `Mac-E43C1C25D4880AD6` | `00000000000000000` | `default` |
| **macOS 11** | **Big Sur** | `Mac-2BD1B31983FE1663` | `00000000000000000` | `default` |
| **macOS 10.15** | **Catalina** | `Mac-CFF7D910A743CAAF` | `00000000000PHCD00` | `default` |

---

## 🔒 Verification & Security

* Every recovery image is downloaded **directly from Apple Content Delivery Network servers** (`oscdn.apple.com` and `osrecovery.apple.com`).
* Files are verified cryptographically in real-time chunk-by-chunk using Apple's official `BaseSystem.chunklist` SHA-256 signatures.
* No modified or third-party operating system files are ever injected.

---

## 🌿 Repository Navigation

* 🏠 **[Main Branch](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/main)**: Validated OpenCore 1.0.8 EFI for Dell Inspiron 14 5410.
* 📖 **[Documentation Branch](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/docs)**: Installation walkthroughs and BIOS configuration.
* 🔍 **[Hardware Report Branch](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/hardware-report)**: ACPI dumps, hardware JSON audit, and USB port mapping.
* 🪟 **[Windows Recovery Branch](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/windows-recovery)**: Returning to Windows and dual-boot recovery.
