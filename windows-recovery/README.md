# Returning to Windows & Dual-Boot Recovery Guide

Complete guide on how to safely return to Windows, restore the factory Windows Boot Manager, fix boot loops, uninstall OpenCore, and configure dual-booting without data loss on the **Dell Inspiron 14 5410 2-in-1**.

---

## 📑 Guides in this Branch

1. **[01 — Restoring Windows Boot Manager](01-Restoring-Windows-Boot-Manager.md)**
   * How to rebuild the Windows BCD and UEFI bootloader using `bcdboot`.
   * Fixing "No bootable devices found" or OpenCore overriding Windows.
   * Accessing Windows Recovery Environment (WinRE) Command Prompt.

2. **[02 — Switching SATA Back to RAID or Keeping AHCI](02-Switching-SATA-Back-To-RAID-or-AHCI.md)**
   * Switching between AHCI and RAID without encountering the `INACCESSIBLE_BOOT_DEVICE` blue screen (BSOD).
   * Using Windows Safe Boot trick to force Windows to load Intel RST or AHCI drivers.

3. **[03 — Cleanly Uninstalling OpenCore](03-Clean-Uninstall-OpenCore.md)**
   * How to mount the EFI partition in Windows.
   * Removing `\EFI\OC` cleanly without touching `\EFI\Microsoft`.
   * Resetting Dell BIOS boot priority to factory default.

4. **[04 — Dual-Booting & BitLocker Management](04-Dual-Boot-Setup-and-BitLocker.md)**
   * Safely partitioning one SSD for both Windows 11 and macOS.
   * Managing BitLocker encryption keys so Windows doesn't lock you out after BIOS changes.
   * Enabling the Windows entry in OpenCore's OpenCanopy picker.
