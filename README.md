# Dell Inspiron 14 5410 2-in-1 Hackintosh (OpenCore 1.0.8)

Complete OpenCore EFI for installing and running macOS (macOS 15 Sequoia / macOS 16 Tahoe) on the **Dell Inspiron 14 5410 2-in-1**.

---

## 💻 Hardware Specifications

| Component | Specification |
| :--- | :--- |
| **Model** | Dell Inspiron 14 5410 2-in-1 |
| **Motherboard** | Dell 0HJ1G8 (Tiger Lake-LP) |
| **CPU** | 11th Gen Intel® Core™ i5-1155G7 (4 Cores / 8 Threads, up to 4.50 GHz) |
| **iGPU** | Intel® Iris® Xe Graphics (Device ID: `8086:9A49`, 80 EUs) |
| **RAM** | DDR4 3200MHz |
| **Storage** | 512GB NVMe SSD (KIOXIA) |
| **Display** | 14.0" FHD (1920x1080) IPS AUO323D Touchscreen |
| **Audio Codec** | Realtek ALC236 (`10EC:0236`), layout-id `11` |
| **Wi-Fi** | Intel® Wi-Fi 6 AX201 160MHz (`8086:A0F0`) |
| **Bluetooth** | Intel® Wireless Bluetooth® (`8087:0026`) |
| **Touchpad & Touchscreen** | ELAN900C / DLL0A89 (I2C HID) |
| **Keyboard** | Standard PS/2 Keyboard (`DLLK0A89`) |

---

## ✅ What Works

- [x] **Graphics Acceleration (QE/CI)**: Working via `WhateverXe.kext` (v0.6.1) with `-allow3d` and `-disablegfxfirmware`.
- [x] **CPU Power Management**: Native XCPM power scaling via Comet Lake CPUID spoof (`0x0A0655`) + `ProvideCurrentCpuInfo`.
- [x] **Audio**: Speakers and Headphone combo jack working via `AppleALC.kext` + `SimpleHDA.kext` (layout-id `11`).
- [x] **Wi-Fi**: Working natively via `AirportItlwm.kext`.
- [x] **Bluetooth**: Working via `IntelBluetoothFirmware.kext` + `IntelBTPatcher.kext` + `BlueToolFixup.kext`.
- [x] **I2C Touchpad & Touchscreen**: Full multi-touch gestures via `VoodooI2C.kext` + `VoodooI2CHID.kext`.
- [x] **Backlight Control & Brightness Keys**: Working with `SSDT-PNLF.aml` and `BrightnessKeys.kext`.
- [x] **Battery Status**: Battery percentage and charging indicators via `ECEnabler.kext` + `SMCBatteryManager.kext`.
- [x] **OpenCore GUI**: OpenCanopy graphical picker with Acidanthera GoldenGate theme.

---

## ⚙️ Essential BIOS Settings

Restart and press **F2** to enter BIOS:

1. **Storage / SATA Operation**: Change from `RAID On` / `VMD` to **`AHCI / NVMe`** *(Critical: macOS installer cannot detect NVMe drives in RAID/VMD mode)*.
2. **Secure Boot**: **Disabled**.
3. **Intel SGX**: **Disabled**.
4. **Fastboot**: **Thorough**.

---

## 🚀 Installation Guide

1. Format a USB drive as FAT32 / GUID Partition Map.
2. Copy the `EFI` folder to the EFI partition or root of the USB drive.
3. Download macOS recovery into `com.apple.recovery.boot`.
4. Boot into the OpenCore bootloader by pressing **F12** at startup.
5. In macOS installer, open Disk Utility, format your internal drive as **APFS** / **GUID Partition Map**, and install macOS.

---

## 🔒 Post-Install Notice (Generate Your Own SMBIOS)

Before signing in to iCloud/Apple ID, generate unique serial numbers using `macserial`:

```bash
macserial -m MacBookPro16,2 -n 1
```

Replace `SystemSerialNumber`, `MLB`, and `SystemUUID` under `PlatformInfo -> Generic` in your `config.plist`.
