# 03 — Cleanly Uninstalling OpenCore

If you want to completely remove OpenCore from your computer and restore pure Windows single-boot.

---

## 🗑️ Step 1: Remove OpenCore from the EFI System Partition

The EFI partition on your internal SSD contains the bootloaders for all operating systems.

### From Windows:
1. Open PowerShell or Command Prompt as **Administrator**.
2. Run `diskpart`:
   ```cmd
   diskpart
   ```
3. Locate your EFI partition:
   ```cmd
   list disk
   select disk 0
   list partition
   select partition 1    (or whichever partition is System/FAT32 ~100MB)
   assign letter=S
   exit
   ```
4. Now delete the OpenCore folder and replace the fallback bootloader:
   ```cmd
   rd /s /q S:\EFI\OC
   ```
5. *(Optional)* If you replaced `S:\EFI\BOOT\BOOTx64.efi` with OpenCore's boot file:
   Rebuild the original Windows boot files:
   ```cmd
   bcdboot C:\Windows /s S: /f UEFI
   ```
6. Remove the mount point in `diskpart`:
   ```cmd
   diskpart
   select volume S
   remove letter=S
   exit
   ```

---

## 🧹 Step 2: Remove Stale UEFI NVRAM Boot Entries

OpenCore adds an entry to your motherboard's UEFI boot list. To remove it cleanly from Windows:

1. Open PowerShell as Administrator.
2. View existing UEFI boot entries:
   ```cmd
   bcdedit /enum firmware
   ```
3. Locate any entry named **OpenCore**:
   ```text
   Firmware Boot Manager
   ---------------------
   identifier              {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
   description             OpenCore
   ```
4. Delete it using its identifier:
   ```cmd
   bcdedit /delete {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
   ```

---

## ⚙️ Step 3: Reset Dell BIOS Settings

1. Restart laptop and tap **F2** to enter BIOS.
2. In the bottom bar, click **Restore Settings** or **Load Defaults**.
3. Select **BIOS Defaults** and click **OK**.
4. Re-enable **Secure Boot** (`Enabled`).
5. Save and restart. Your Dell laptop is now in 100% factory original state.
