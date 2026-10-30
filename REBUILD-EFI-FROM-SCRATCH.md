# Rebuild EFI From Scratch Guide

If you ever update BIOS, encounter an unbootable configuration, or need to rebuild the OpenCore EFI for the Dell Inspiron 14 5410 from raw ACPI tables, follow this emergency recovery procedure.

---

## 📂 Required Raw Files (Included in this Branch)

All original system tables dumped directly from the Dell Inspiron 14 5410 are stored in the [`Raw_ACPI_Dumps`](Raw_ACPI_Dumps) folder:
* `dsdt.aml`: Master System Description Table.
* `apic.aml`, `dmar.aml`, `hpet.aml`, `lpit.aml`, `nhlt.aml`.
* `ssdt1.aml` through `ssdt11.aml`.

---

## 🛠️ Step 1: Re-Compiling Custom SSDTs with iASL

Using `iasl.exe` (Intel ACPI Component Architecture compiler):

```bash
iasl -tc SSDT-PLUG.dsl
iasl -tc SSDT-EC.dsl
iasl -tc SSDT-RTCAWAC.dsl
iasl -tc SSDT-PNLF.dsl
iasl -tc SSDT-GPI0.dsl
iasl -tc SSDT-XOSI.dsl
```

### Purpose of Each SSDT:
1. **`SSDT-PLUG.aml`**: Injects `plugin-type = 1` into the first processor thread (`\_SB.PR00`) to initiate macOS native XCPM power management.
2. **`SSDT-EC.aml`**: Injects a compliant dummy Embedded Controller (`EC`) to appease macOS Catalina/Big Sur/Monterey/Ventura/Sonoma/Tahoe since Dell names the hardware controller `ECDV`.
3. **`SSDT-RTCAWAC.aml`**: Disables the modern AWAC timer and re-enables the legacy RTC clock (`_STA = 0` on AWAC).
4. **`SSDT-PNLF.aml`**: Injects backlight controls (`_UID = 19`) for Intel Tiger Lake integrated graphics.
5. **`SSDT-GPI0.aml`**: Enables Intel Tiger Lake GPIO controller (`_STA = 0x0F` on `GPI0`) allowing VoodooI2C to receive interrupts from the ELAN900C touchpad and touchscreen.
6. **`SSDT-XOSI.aml`**: Redirects ACPI `_OSI` OS queries to Windows 10/11 (`"Windows 2019"`), ensuring all Dell thermal sensors and touchpad interfaces stay enabled.

---

## ⚙️ Step 2: Essential Kernel Quirks for Tiger Lake

In OpenCore `config.plist`:

### 1. Kernel -> Emulate (CPUID Spoof)
* **`Cpuid1Data`**: `55060A00 00000000 00000000 00000000` (Comet Lake CPUID `0x0A0655`)
* **`Cpuid1Mask`**: `FFFFFFFF 00000000 00000000 00000000`

### 2. Kernel -> Quirks
* **`ProvideCurrentCpuInfo`**: `True` (Essential for correct core count and TSC calibration).
* **`AppleXcpmCfgLock`**: `True` (Prevents panic on MSR 0xE2 lock).
* **`CustomSMBIOSGuid`**: `True` (Required for Dell laptops to update SMBIOS).
* **`DisableIoMapper`**: `True` (Prevents VT-d memory mapping conflicts).
* **`DisableRtcChecksum`**: `True` (Prevents Dell BIOS resetting time and CMOS).

---

## 🎮 Step 3: Graphics Configuration (WhateverXe)

1. Remove `WhateverGreen.kext` (do **not** use WhateverGreen with WhateverXe).
2. Add `WhateverXe.kext` immediately after `Lilu.kext`.
3. Set `boot-args`: `-v keepsyms=1 debug=0x100 -allow3d -disablegfxfirmware alcid=11`.
4. In `DeviceProperties -> Add -> PciRoot(0x0)/Pci(0x2,0x0)`:
   * `device-id`: `<49 9A 00 00>`
   * `framebuffer-patch-enable`: `<01 00 00 00>`
   * `framebuffer-stolenmem`: `<00 00 C0 03>` (if 60MB DVMT allocation)
   * `enable-metal`: `<01 00 00 00>`

---

## 🩺 Step 4: Verification

Always validate the generated `config.plist` using `ocvalidate`:
```bash
./ocvalidate config.plist
```
Ensure it returns:
`Completed validating config.plist in X ms. No issues found.`
