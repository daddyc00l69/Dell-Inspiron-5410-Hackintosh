# USB Port Mapping Guide — Dell Inspiron 14 5410 2-in-1

Proper USB port mapping is vital on macOS to guarantee sleep/wake stability, full USB 3.0/3.1 speeds, and clean power management.

---

## 🔌 Hardware USB Controllers

Your Dell Inspiron 14 5410 features two distinct USB Host Controllers:

1. **Primary xHCI Controller (PCH)**:
   * **Device ID**: `8086:A0ED`
   * **PCI Path**: `PciRoot(0x0)/Pci(0x14,0x0)`
   * **ACPI Path**: `\_SB.PC00.XHCI`
   * Controls the standard Type-A ports, internal camera, and Bluetooth.
2. **Thunderbolt / Type-C USB 3.10 Controller**:
   * **Device ID**: `8086:9A13`
   * **PCI Path**: `PciRoot(0x0)/Pci(0xd,0x0)`
   * **ACPI Path**: `\_SB.PC00.TXHC`
   * Controls the USB 3.2 Gen 2 Type-C port with Power Delivery & DisplayPort Alt Mode.

---

## 🗺️ Physical Port Map Table

| Physical Port | Connector Type | USB 2.0 Companion Port | USB 3.0 Companion Port | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Left USB Type-A** | Type-A (USB 3.2 Gen 1) | `HS01` (USB 2.0) | `SS01` (5 Gbps) | Standard USB 3.0 external port |
| **Right USB Type-A** | Type-A (USB 3.2 Gen 1) | `HS02` (USB 2.0) | `SS02` (5 Gbps) | Standard USB 3.0 external port |
| **Left USB Type-C** | Type-C w/ Switch | `HS03` / `TXHC` | `SS03` / `TXHC` | 10 Gbps Type-C port with Power Delivery & DP |
| **Internal HD Webcam** | Internal (`255`) | `HS05` | N/A | Integrated 720p HD Camera |
| **Intel Bluetooth** | Internal (`255`) | `HS07` | N/A | Bluetooth 5.1 interface on AX201 (`8087:0026`) |
| **Fingerprint Sensor** | Internal (`255`) | `HS09` | N/A | Goodix MOC Fingerprint (`27C6:639C`) |

---

## 🛠️ How to Map Ports Using USBToolBox

If you want to customize or regenerate the USB map:

1. Download **USBToolBox Windows Tool** from [GitHub](https://github.com/USBToolBox/tool/releases).
2. Run `USBToolBox.exe` in Windows.
3. Select **D. Discover Ports**:
   * Plug a USB 2.0 device into both Type-A ports and the Type-C port (with adapter).
   * Plug a USB 3.0 drive into both Type-A ports and the Type-C port.
4. Select **S. Select Ports and Build Kext**:
   * Set physical Type-A ports to `Type 0` (or `Type 3` for USB 3).
   * Set Type-C port to `Type 9` (Type-C with switch).
   * Set Internal Camera and Bluetooth to `Type 255` (Internal).
5. Press **K** to build `UTBMap.kext`.
6. Add `UTBMap.kext` and `USBToolBox.kext` into your `EFI/OC/Kexts` folder.
