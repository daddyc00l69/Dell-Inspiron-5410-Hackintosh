# Dell Inspiron 14 5410 2-in-1 — Complete Hardware Report

This document contains the raw hardware profile, PCI tree, and ACPI addresses dumped directly from the **Dell Inspiron 14 5410 2-in-1** (Dell Motherboard `0HJ1G8`).

---

## 🖥️ System Architecture

* **Motherboard**: Dell Inc. `0HJ1G8` (A00)
* **Chipset**: Intel Tiger Lake-LP PCH
* **BIOS Version**: `2.29.0` (Release Date: `2024-09-26`, UEFI Mode)
* **Platform Type**: Mobile / Laptop (2-in-1 Convertible)

---

## ⚡ Processor (CPU)

* **Name**: 11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz
* **Codename**: Tiger Lake-UP3 (10nm SuperFin)
* **Cores / Threads**: 4 Cores / 8 Threads
* **Base Frequency**: 2.50 GHz (Turbo boost up to 4.50 GHz)
* **Instruction Sets**: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AVX, AVX2, FMA3
* **OpenCore Emulation Profile**: Comet Lake (`Cpuid1Data`: `55060A00000000000000000000000000`, `Cpuid1Mask`: `FFFFFFFF000000000000000000000000`)

---

## 🎮 Integrated Graphics (iGPU)

* **GPU Name**: Intel(R) Iris(R) Xe Graphics (Tiger Lake GT2, 80 Execution Units)
* **PCI Device ID**: `8086:9A49`
* **Subsystem ID**: `1028:0A89`
* **PCI Path**: `PciRoot(0x0)/Pci(0x2,0x0)`
* **ACPI Path**: `\_SB.PC00.GFX0`
* **Internal Panel Model**: AUO323D (eDP 1920x1080 @ 60Hz 14-inch IPS)
* **Kext Provider**: `WhateverXe.kext` (v0.6.1)

---

## 🔊 Audio Subsystem

* **High Definition Audio Controller**: Intel Tiger Lake-LP Smart Sound Audio Controller
  * **Device ID**: `8086:A0C8`
  * **PCI Path**: `PciRoot(0x0)/Pci(0x1f,0x3)`
  * **ACPI Path**: `\_SB.PC00.HDAS`
* **Audio Codec**: Realtek ALC236 / ALC3204
  * **Vendor / Device**: `10EC:0236`
  * **Subsystem**: `1028:0A89`
  * **Tested Working Layout IDs**: `11` (Default), `13`, `14`, `15`
  * **Tahoe AppleHDA Stack**: `SimpleHDA.kext` (v1.0.0) + `AppleALC.kext`

---

## 📡 Networking & Connectivity

### Wi-Fi Adapter
* **Card**: Intel(R) Wi-Fi 6 AX201 160MHz
* **Form Factor**: M.2 2230 CNVi (Integrated Wi-Fi)
* **Device ID**: `8086:A0F0`
* **Subsystem**: `8086:4070`
* **PCI Path**: `PciRoot(0x0)/Pci(0x14,0x3)`
* **ACPI Path**: `\_SB.PC00.CNVW`
* **Driver**: `AirportItlwm.kext` (v2.4.0 Tahoe release)

### Bluetooth
* **Device**: Intel(R) Wireless Bluetooth(R)
* **Bus**: USB (Internal Header)
* **Vendor / Product ID**: `8087:0026`
* **Drivers**: `IntelBluetoothFirmware.kext` + `IntelBTPatcher.kext` + `BlueToolFixup.kext`

---

## 💾 Storage Controllers

* **Storage Controller**: Volume Management Device NVMe RAID Controller (Intel VMD)
  * **Device ID**: `8086:9A0B`
  * **PCI Path**: `PciRoot(0x0)/Pci(0xe,0x0)`
  * **ACPI Path**: `\_SB.PC00.VMD0`
  * **Disk**: KIOXIA KBG40ZNS512G NVMe 512GB (M.2 2230/2280)
  * **Requirement**: BIOS must be toggled to **AHCI / NVMe** mode for macOS recognition.

---

## 🖱️ Input Devices & Embedded Controller

* **Embedded Controller**: Microsoft ACPI-Compliant EC (`PNP0C09`)
  * **ACPI Path**: `\_SB.PC00.LPCB.ECDV` (Dell renamed ECDV -> requires `SSDT-EC.aml` or `ECEnabler.kext`)
* **Touchscreen**: ELAN900C
  * **Bus**: I2C HID Device
  * **Driver**: `VoodooI2C.kext` + `VoodooI2CHID.kext`
* **Touchpad**: DLL0A89
  * **Bus**: I2C / PS/2 dual interface
  * **Driver**: `VoodooI2C.kext`
* **Keyboard**: Dell Standard PS/2 Keyboard (`DLLK0A89`)
  * **Driver**: `VoodooPS2Keyboard.kext`
