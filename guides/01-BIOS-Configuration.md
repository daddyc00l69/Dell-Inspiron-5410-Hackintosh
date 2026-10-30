# 01 — BIOS Configuration Guide

Before booting OpenCore or installing macOS, your Dell Inspiron 14 5410 2-in-1 UEFI BIOS must be configured appropriately.

---

## 🔑 Accessing Dell BIOS

1. Shut down your laptop completely.
2. Power on the laptop and immediately start tapping the **F2** key until the BIOS screen appears.

---

## ⚙️ Settings Configuration Table

| BIOS Section | Option | Recommended Setting | Rationale |
| :--- | :--- | :--- | :--- |
| **System Configuration** | **SATA Operation** | **AHCI / NVMe** | **CRITICAL**: Default is `RAID On / VMD`. Apple has no driver for Intel VMD RAID. The installer cannot detect internal NVMe drives unless in AHCI mode. |
| **Security** | **Secure Boot Enable** | **Disabled** | macOS kernels and unsigned OpenCore drivers cannot boot under Microsoft UEFI Secure Boot keys. |
| **Security** | **Intel SGX** | **Disabled** | Prevents memory allocation locking bugs. |
| **Security** | **PTT (TPM 2.0)** | **Enabled or Disabled** | Does not affect macOS (macOS ignores TPM). |
| **Pre-boot Behavior** | **Fastboot** | **Thorough** | Ensures all hardware buses and PCI lanes are fully initialized during cold boot. |
| **System Configuration** | **USB Boot Support** | **Enabled** | Required to boot external USB recovery media. |
| **System Configuration** | **Thunderbolt (TBT)** | **Enabled** | Allows Type-C display output and peripherals. |
| **Virtualization Support** | **Intel Virtualization (VT-x)** | **Enabled** | Allows hardware virtualization. |
| **Virtualization Support** | **VT-for-Direct I/O (VT-d)** | **Enabled / Disabled** | Handled seamlessly by `DisableIoMapper = True` in our OpenCore `config.plist`. |
| **Power Management** | **Wake on AC / LAN** | **Disabled** | Prevents unexpected sleep wake-ups while laptop lid is closed. |

---

## 💡 Switching RAID to AHCI Without Reinstalling Windows

If your laptop currently runs Windows in RAID mode:
1. Boot into Windows.
2. Open Command Prompt as Administrator and run:
   ```cmd
   bcdedit /set {current} safeboot minimal
   ```
3. Restart into BIOS (**F2**) and switch **SATA Operation** to **AHCI / NVMe**.
4. Save and exit (F10). Windows will automatically boot into Safe Mode and load the AHCI controller driver.
5. In Safe Mode, open Command Prompt as Administrator and run:
   ```cmd
   bcdedit /deletevalue {current} safeboot
   ```
6. Restart. Windows will now boot normally in AHCI mode, and macOS can also see the drive!
