# 04 — Post-Installation Tuning & Customization

Once macOS is installed, complete these essential configuration steps to achieve 100% daily-driver stability.

---

## 1. Booting Without the USB Drive

Currently, OpenCore is on your USB drive. To boot directly from your internal SSD:

1. Download **MountEFI** or **OCAuxiliaryTools (OCAT)** on macOS.
2. Mount the EFI partition of both your USB drive and your internal SSD.
3. Copy the entire `EFI` folder from your USB drive to the EFI partition of your internal SSD.
4. Safely eject the USB drive. Your laptop will now boot directly into OpenCore!

---

## 2. Generating Unique SMBIOS Serials (For Apple ID & iServices)

To avoid conflicts with Apple servers and enable iMessage, FaceTime, and iCloud:

1. Open Terminal and run `macserial` (or use OCAT):
   ```bash
   ./macserial -m MacBookPro16,2 -n 1
   ```
2. You will receive an output in this format:
   ```text
   SerialNumber | BoardSerialNumber (MLB)
   ```
3. Open `config.plist` using ProperTree or OCAT:
   * Navigate to `PlatformInfo -> Generic`.
   * Set `SystemProductName`: `MacBookPro16,2`
   * Set `SystemSerialNumber`: `<Your generated SerialNumber>`
   * Set `MLB`: `<Your generated BoardSerialNumber>`
   * Generate a fresh UUID for `SystemUUID` using `uuidgen` in terminal.
4. Save `config.plist` and reboot.

---

## 3. Audio Layout ID Verification (ALC236)

This EFI is pre-configured with `alcid=11` and `SimpleHDA.kext`.

If headphones or microphone switching need adjustment, test alternative layout IDs in `boot-args`:
- `alcid=11` (Default - Dell Inspiron standard)
- `alcid=13`
- `alcid=14`
- `alcid=15`
- `alcid=99`

To test, edit `NVRAM -> Add -> 7C436110-AB2A-4BBB-A880-FE41995C9F82 -> boot-args` and reboot.

---

## 4. Wi-Fi 6 Optimization (`AirportItlwm`)

By default, AirportItlwm runs in 802.11ac Wi-Fi 5 mode for maximum power efficiency.
To unlock 802.11ax (Wi-Fi 6 High Efficiency mode) on your Intel AX201:
1. Open `config.plist`.
2. Add `itlwm_he=1` to `boot-args`.
3. Save and reboot.

---

## 5. Trackpad & Touchscreen Customization

The Dell Inspiron 14 5410 features an I2C-connected ELAN900C multi-touch panel and trackpad.
- Go to **System Settings -> Trackpad**:
  * Enable **Tap to Click**.
  * Enable **Two-Finger Scroll**.
  * Configure 3-finger swipe for Mission Control / App Exposé.
