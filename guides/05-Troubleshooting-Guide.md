# 05 — Troubleshooting Guide

Common issues, symptoms, root causes, and verified fixes for the Dell Inspiron 14 5410 2-in-1.

---

## 🔍 Symptom Matrix

| Issue | Root Cause | Solution |
| :--- | :--- | :--- |
| **Installer Disk Utility does not show internal SSD** | Intel VMD / RAID is enabled in BIOS | Enter BIOS (**F2**), navigate to **SATA Operation**, and switch from `RAID On` to **`AHCI / NVMe`**. |
| **Boot hangs at `[EB|#LOG:EXITBS:START]`** | Memory Map / Booter quirk mismatch | Verify in `Booter -> Quirks` that `SetupVirtualMap = True`, `RebuildAppleMemoryMap = True`, and `ProvideCurrentCpuInfo = True`. |
| **Black screen after verbose text finishes** | Framebuffer / Panel communication timeout | Ensure `WhateverXe.kext` is loaded and `boot-args` contains `-allow3d -disablegfxfirmware`. Laptops with internal displays do **not** use `-wex-nopanel`. |
| **Trackpad or Touchscreen unresponsive** | GPIO pin interrupt routing | Ensure `SSDT-GPI0.aml` and `SSDT-XOSI.aml` are enabled in `ACPI -> Add`, and `_OSI to XOSI` patch is enabled in `ACPI -> Patch`. |
| **Wi-Fi connection fails or drops** | AppleVTD / I/O Mapper conflict | Ensure `Kernel -> Quirks -> DisableIoMapper = True` is set. |
| **Audio not detected or no sound** | Missing AppleHDA on macOS Tahoe | Ensure `SimpleHDA.kext` and `AppleALC.kext` are enabled. Verify `alcid=11` in `boot-args`. |
| **System restarts unexpectedly during sleep** | Wake on LAN / AC enabled | In Dell BIOS, turn off **Wake on AC** and **Wake on LAN/WLAN**. In macOS, disable "Wake for network access" in Battery settings. |
| **RTC reset error on reboot ("Time not set")** | Dell RTC checksum write bug | Ensure `Kernel -> Quirks -> DisableRtcChecksum = True` is enabled in `config.plist`. |

---

## 🛠️ Performing an NVRAM Reset

If you ever experience weird boot loops or leftover cache:
1. Turn on laptop and tap **F12** to enter OpenCore picker.
2. In the picker, select **Reset NVRAM** (press Spacebar if auxiliary tools are hidden).
3. The system will automatically reboot with a pristine NVRAM state.
