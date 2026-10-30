# 02 — Creating Installer USB

This guide covers preparing a bootable macOS USB installer on Windows or macOS.

---

## 🛠️ Requirements

- A USB flash drive (16 GB or larger, USB 3.0 recommended).
- Internet access for downloading Apple recovery files.
- The `Dell-Inspiron-5410-OpenCore-1.0.8-EFI.zip` archive.

---

## 🪟 Method 1: Creating on Windows (Fastest)

### Step 1: Format the USB Drive
1. Insert your USB flash drive.
2. Open **Disk Management** (`Win + X` -> Disk Management).
3. Right-click your USB flash drive volume and select **Format...**:
   * File System: **FAT32**
   * Allocation unit size: **Default**
   * Volume label: `BOOT`
4. Click **OK**.

### Step 2: Copy the EFI Folder
1. Download `Dell-Inspiron-5410-OpenCore-1.0.8-EFI.zip` from [Releases](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/releases/latest).
2. Extract the archive.
3. Copy the resulting `EFI` folder directly to the root of your USB drive:
   ```text
   D:\
   └── EFI\
       ├── BOOT\
       │   └── BOOTx64.efi
       └── OC\
           ├── ACPI\
           ├── Drivers\
           ├── Kexts\
           ├── Resources\
           ├── Tools\
           ├── OpenCore.efi
           └── config.plist
   ```

### Step 3: Download macOS Recovery
Run OpenCore's official `macrecovery` utility from command prompt or PowerShell:

```bash
# macOS Sequoia / Tahoe Recovery
python Utilities/macrecovery/macrecovery.py -b Mac-CFF7D910A743CAAF -m 00000000000000000 -os latest download
```

This creates a `com.apple.recovery.boot` folder containing:
- `BaseSystem.dmg` (~960 MB)
- `BaseSystem.chunklist`

Copy `com.apple.recovery.boot` directly to the root of your USB drive (`D:\com.apple.recovery.boot`).

Your USB drive root structure should look like this:
```text
D:\
├── com.apple.recovery.boot\
│   ├── BaseSystem.chunklist
│   └── BaseSystem.dmg
└── EFI\
    ├── BOOT\
    └── OC\
```

---

## 🍏 Method 2: Creating on macOS

If you already have access to a real Mac or Hackintosh:
1. Download macOS from the Mac App Store.
2. Plug in your 16GB+ USB flash drive named `MyVolume`.
3. Open Terminal and run the official Apple `createinstallmedia` command:
   ```bash
   sudo /Applications/Install\ macOS\ Sequoia.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume
   ```
4. Once completed, mount the hidden EFI partition using **MountEFI** or **OCAT**.
5. Copy the `EFI` folder to the EFI partition.
