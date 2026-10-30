# Dell Inspiron 14 5410 2-in-1 — Complete Documentation & Guides

Welcome to the comprehensive documentation branch for the Dell Inspiron 14 5410 2-in-1 Hackintosh.

---

## 📚 Table of Contents

1. **[BIOS Configuration Guide](01-BIOS-Configuration.md)**
   * Complete UEFI/BIOS configuration for Dell Inspiron laptops.
   * Switching SATA from RAID On (Intel VMD) to AHCI without data loss.
   * Secure Boot, TPM, Fastboot, and Virtualization settings.

2. **[Creating Installer USB](02-Creating-Installer-USB.md)**
   * Formatting FAT32 / GPT on Windows.
   * Downloading macOS recovery payloads (`com.apple.recovery.boot`).
   * Placing the EFI structure onto the USB drive.

3. **[macOS Installation Walkthrough](03-macOS-Installation-Walkthrough.md)**
   * One-time boot menu (F12) selection.
   * Disk Utility drive preparation (APFS & GUID Partition Scheme).
   * Step-by-step installation stages and reboot handling.

4. **[Post-Installation Tuning & Customization](04-Post-Installation-Tuning.md)**
   * Generating unique serials with `macserial` for iCloud & iMessage.
   * Sound verification and audio layout IDs for Realtek ALC236.
   * Wi-Fi 6 optimization (`itlwm_he=1`) and Bluetooth pairing.
   * I2C Trackpad and multi-touch gestures tuning.
   * Battery health management and sleep/wake optimizations.

5. **[Troubleshooting & Diagnostic FAQ](05-Troubleshooting-Guide.md)**
   * Resolving black screens during boot (`WhateverXe` flags).
   * Fixing stuck boots at `[EB|#LOG:EXITBS:START]`.
   * Resolving NVMe missing drive in Disk Utility.
   * Audio dropouts and microphone array solutions.
