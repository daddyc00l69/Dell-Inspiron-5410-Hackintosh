# Release v1.0.0 — OpenCore 1.0.8 EFI for Dell Inspiron 14 5410 2-in-1

### 🚀 Overview
Initial official release of the verified and validated OpenCore 1.0.8 EFI for the **Dell Inspiron 14 5410 2-in-1** laptop running **macOS 15 Sequoia** and **macOS 16 Tahoe**.

---

### 🌟 Key Highlights & Innovations
- **Intel Iris Xe Graphics Acceleration**: Powered by `WhateverXe.kext` (v0.6.1) providing native-like Metal and OpenGL hardware graphics acceleration, resolving the long-standing limitation on Intel Gen12 Tiger Lake mobile iGPUs.
- **Tiger Lake CPU Power Scaling**: CPUID emulation via Comet Lake (`0x0A0655`) coupled with `ProvideCurrentCpuInfo`, enabling full XCPM frequency stepping and C-state residency.
- **macOS Tahoe Audio Stack**: Integration of `SimpleHDA.kext` (v1.0.0) alongside `AppleALC.kext` (layout-id 11), restoring full HD audio without needing system partition root patching or disabling SIP.
- **Native Intel Wi-Fi & Bluetooth**: `AirportItlwm.kext` for direct macOS native menu bar Wi-Fi control on Intel AX201, plus `IntelBluetoothFirmware` and `BlueToolFixup`.
- **I2C Precision Trackpad & Touchscreen**: Full multi-touch macOS gesture support for the ELAN900C touchscreen and DLL0A89 touchpad via `VoodooI2C.kext` + custom `SSDT-GPI0.aml` and `SSDT-XOSI.aml`.
- **OpenCanopy Graphical Picker**: GoldenGate high-definition theme with boot chime support and integrated diagnostic tools.

---

### 📊 Verification & Validation
- **`ocvalidate`**: Clean pass with **0 errors and 0 warnings**.
- **Kext Loading Hierarchy**: Verified and strictly ordered (Lilu -> WhateverXe -> VirtualSMC -> Plugins).

---

### 📦 Included Asset
- **`Dell-Inspiron-5410-OpenCore-1.0.8-EFI.zip`**: Complete pre-configured `EFI` folder ready to extract directly to your USB drive.

---

### ⚠️ Pre-Boot Checklist
1. **Dell BIOS Storage Setting**: Switch **SATA Operation** from `RAID On` (Intel VMD) to **`AHCI / NVMe`**.
2. **Secure Boot**: Set to **Disabled**.
3. **USB Installer**: Extract the ZIP, place `EFI` onto your FAT32 USB drive, and add `com.apple.recovery.boot`.

