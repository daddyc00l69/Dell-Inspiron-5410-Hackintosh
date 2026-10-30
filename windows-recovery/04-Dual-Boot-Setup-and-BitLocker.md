# 04 — Dual-Boot Setup & BitLocker Management

Running Windows 11 and macOS together on the Dell Inspiron 14 5410.

---

## 🔐 BitLocker Notice (Very Important!)

Dell laptops often have **BitLocker Drive Encryption** turned ON by default from the factory.

> [!WARNING]
> Changing BIOS settings (like switching from RAID to AHCI, disabling Secure Boot, or updating OpenCore) modifies the system's TPM PCR measurements. If BitLocker is enabled without suspension, **Windows will lock you out and demand your 48-digit BitLocker Recovery Key** on the next boot!

### How to back up or suspend BitLocker:
1. In Windows, press `Win + S` and type **BitLocker**. Click **Manage BitLocker**.
2. Click **Back up your recovery key**:
   * Save it to your Microsoft Account, or save it to a separate USB drive.
3. Before changing BIOS settings or installing OpenCore, click:
   **Suspend protection** -> Click **Yes**.
4. Once you have finished dual-booting and everything is stable, click **Resume protection**.

---

## 🪟 Partitioning One SSD for Dual-Boot

If you are using the single 512GB internal KIOXIA NVMe SSD:

1. In Windows, open **Disk Management** (`diskmgmt.msc`).
2. Right-click your main Windows volume (`C:`) and select **Shrink Volume...**.
3. Enter the amount to shrink for macOS (e.g., `200000` MB for ~200 GB). Click **Shrink**.
4. Leave the freed space as **Unallocated**.
5. Boot into the macOS Installer USB.
6. In Disk Utility, format that Unallocated space as **APFS** named `Macintosh HD`.
7. Install macOS onto `Macintosh HD`.

Both Windows and macOS will share the EFI partition cleanly!

---

## 🎯 Booting Windows from OpenCore Picker

Our OpenCore `config.plist` is already configured with `ScanPolicy = 0`.
When OpenCore boots:
* You will see icons for both **Macintosh HD** and **Windows Boot Manager**.
* You can select Windows and press Enter to boot Windows directly.
* To make Windows your default OS: highlight Windows in the picker and press **`Ctrl + Enter`**.
