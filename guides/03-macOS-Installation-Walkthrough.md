# 03 — macOS Installation Walkthrough

Step-by-step instructions from cold boot to the macOS desktop.

---

## ⚡ Step 1: Booting OpenCore

1. Plug the prepared USB flash drive into any USB port on your Dell Inspiron 14 5410.
2. Turn on the laptop and immediately tap **F12** until the **One-Time Boot Menu** appears.
3. Under UEFI Boot options, select your **UEFI: USB Flash Drive**.
4. The OpenCanopy graphical boot picker will appear on screen.
5. Highlight and press Enter on **Install macOS (macOS Recovery)**.

---

## 💻 Step 2: Preparing the Internal Drive (Disk Utility)

1. When the macOS Recovery screen loads, click **Disk Utility** and click **Continue**.
2. In the top-left menu of Disk Utility, click **View** and select **Show All Devices**.
3. Select your internal SSD (e.g. `KIOXIA KBG40ZNS512G NVMe` or your target partition).
4. Click **Erase** in the toolbar:
   * **Name**: `Macintosh HD`
   * **Format**: `APFS`
   * **Scheme**: `GUID Partition Map`
5. Click **Erase** and wait for the operation to complete.
6. Close Disk Utility.

---

## 🍎 Step 3: Installing macOS

1. On the main Recovery menu, select **Install macOS** and click **Continue**.
2. Agree to the Apple software license terms.
3. Select the `Macintosh HD` disk you just formatted and click **Continue**.
4. The installer will write the initial installation files (typically 15-25 minutes).
5. **Reboot Stages**:
   * The laptop will restart automatically several times.
   * **Always let OpenCore boot the default highlighted entry** (usually labelled `macOS Installer` or `Macintosh HD`).
   * Do not remove the USB drive until the initial macOS setup assistant (country/language selection) appears.

---

## 🖥️ Step 4: First-Time Setup

1. Complete the standard macOS setup assistant:
   * Select your Country and Language.
   * Connect to your Wi-Fi network (AX201 is functional).
   * We recommend selecting **Set Up Later** for Apple ID / iCloud until you generate your own SMBIOS serials in the next guide.
   * Create your local administrator account.
2. You will land on the macOS desktop with full hardware graphics acceleration enabled!
