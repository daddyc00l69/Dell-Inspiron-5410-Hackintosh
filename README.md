# Dell Inspiron 14 5410 2-in-1 — OpenCore 1.0.8 Hackintosh

[![macOS](https://img.shields.io/badge/macOS-Sequoia%20%7C%20Tahoe-blue?logo=apple&logoColor=white)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh)
[![OpenCore](https://img.shields.io/badge/OpenCore-1.0.8-success?logo=apple&logoColor=white)](https://github.com/acidanthera/OpenCorePkg)
[![Release](https://img.shields.io/github/v/release/daddyc00l69/Dell-Inspiron-5410-Hackintosh?color=orange&logo=github)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/releases/latest)
[![Validated](https://img.shields.io/badge/ocvalidate-passed%20(0%20errors)-brightgreen)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh)

A fully optimized, production-ready OpenCore 1.0.8 EFI designed specifically for the **Dell Inspiron 14 5410 2-in-1** laptop featuring the **11th Gen Intel Core i5-1155G7 (Tiger Lake-U)** and **Intel Iris Xe Graphics**.

---

## 🧭 Repository Branches & Resources

This repository is organized into dedicated branches for distinct workflows:

| Branch | Purpose & Contents | Direct Link |
| :--- | :--- | :--- |
| **`main`** | The ready-to-use OpenCore 1.0.8 `EFI` folder, validated configuration, and pre-built ZIP release. | [Explore `main`](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/main) |
| **`docs`** | Comprehensive step-by-step installation guides, post-install tweaks, audio layout tuning, and troubleshooting. | [Explore `docs`](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/docs) |
| **`hardware-report`** | Raw ACPI dumps (`dsdt.aml`, all original SSDTs), full JSON device report, PCI topology, and rebuild instructions. | [Explore `hardware-report`](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/hardware-report) |
| **`windows-recovery`** | Complete guide on safely returning to Windows, repairing Windows Bootloader, switching back to RAID, and dual-boot recovery. | [Explore `windows-recovery`](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/windows-recovery) |

---

## 💻 Hardware Specifications

| Component | Hardware Specification | Hackintosh Status |
| :--- | :--- | :--- |
| **Model** | Dell Inspiron 14 5410 2-in-1 | Verified |
| **Motherboard** | Dell 0HJ1G8 (Tiger Lake-LP Chipset) | Fully Supported via custom SSDTs |
| **Processor** | 11th Gen Intel® Core™ i5-1155G7 @ 2.50 GHz (4 Cores / 8 Threads) | Native XCPM via Comet Lake CPUID Spoof (`0x0A0655`) |
| **Graphics** | Intel® Iris® Xe Graphics (`8086:9A49`, 80 EUs) | Hardware Accelerated via [`WhateverXe.kext`](https://github.com/b00t0x/WhateverXe) |
| **Memory** | DDR4 3200 MHz | Fully Functional |
| **Storage** | 512GB NVMe SSD (KIOXIA KBG40ZNS512G) | Managed via `NVMeFix.kext` (Requires BIOS AHCI mode) |
| **Display** | 14.0" FHD (1920x1080) IPS (AUO323D) | Smooth backlight control via `SSDT-PNLF.aml` |
| **Audio** | Realtek ALC236 (`10EC:0236`), layout-id `11` | Native audio via `AppleALC.kext` + `SimpleHDA.kext` |
| **Wi-Fi** | Intel® Wi-Fi 6 AX201 160MHz (`8086:A0F0`) | Native Wi-Fi menu bar integration via `AirportItlwm.kext` |
| **Bluetooth** | Intel® Wireless Bluetooth® (`8087:0026`) | Supported via `IntelBluetoothFirmware` + `BlueToolFixup` |
| **Touchscreen** | ELAN900C (I2C HID) | Multi-touch working via `VoodooI2C.kext` + `SSDT-GPI0.aml` |
| **Touchpad** | DLL0A89 (I2C HID) | Smooth macOS trackpad gestures via `VoodooI2CHID.kext` |
| **Keyboard** | Standard PS/2 (`DLLK0A89`) | Responsive input via `VoodooPS2Keyboard.kext` |
| **Battery Status** | Dell Smart Battery | Percentage and AC status working via `ECEnabler.kext` |

---

## 📦 Quick Start (USB Creation)

1. Format a 16GB+ USB drive as **FAT32** with GUID Partition Table (GPT).
2. Download the pre-built EFI:
   * **[Download Latest Release (v1.0.0)](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/releases/latest)**
3. Extract the ZIP and copy the `EFI` folder to the root of your USB drive (`D:\EFI`).
4. Download macOS recovery using OpenCore's `macrecovery`:
   ```bash
   python Utilities/macrecovery/macrecovery.py -b Mac-CFF7D910A743CAAF -m 00000000000000000 -os latest download
   ```
5. Place the resulting `com.apple.recovery.boot` folder directly onto the root of the USB drive (`D:\com.apple.recovery.boot`).

---

## ⚙️ Essential BIOS Settings

Before booting from your USB drive, restart and press **F2** to enter Dell BIOS:

> [!IMPORTANT]
> **Storage Mode (Critical)**:
> By default, Dell ships laptops with **RAID On / Intel VMD**. macOS **cannot see NVMe drives in RAID mode**.
> Change **System Configuration -> SATA Operation** from `RAID On` to **`AHCI / NVMe`**.
> *(If you want to keep your Windows install working without reformatting, follow the [Safe Mode SATA Switch Guide](https://github.com/daddyc00l69/Dell-Inspiron-5410-Hackintosh/tree/windows-recovery) before toggling this setting).*

* **Secure Boot**: `Disabled`
* **Intel SGX**: `Disabled`
* **Fastboot**: Set to `Thorough`
* **USB Boot Support**: `Enabled`
* **Wake on LAN / WLAN**: `Disabled`

---

## 🔒 Important SMBIOS Notice

The configuration in this repository uses a generic serial number placeholder. **Before signing into Apple ID / iCloud / iMessage**, generate your own unique serials:

```bash
macserial -m MacBookPro16,2 -n 1
```

Insert your generated `SystemSerialNumber`, `MLB`, and a new `SystemUUID` into `config.plist` under `PlatformInfo -> Generic`.

---

## 🤝 Credits & Acknowledgements

* [Acidanthera](https://github.com/acidanthera) for OpenCorePkg, Lilu, AppleALC, VirtualSMC, and VoodooPS2.
* [b00t0x](https://github.com/b00t0x/WhateverXe) for WhateverXe (Intel Xe-LP graphics acceleration on macOS).
* [laobamac](https://github.com/laobamac) for SimpleHDA (Tahoe AppleHDA injection) and updated AirportItlwm.
* [OpenIntelWireless](https://github.com/OpenIntelWireless) for Intel Wi-Fi and Bluetooth kexts.
* [VoodooI2C team](https://github.com/VoodooI2C/VoodooI2C) for I2C touchpad and touchscreen drivers.
