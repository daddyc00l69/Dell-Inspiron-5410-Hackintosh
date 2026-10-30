# 01 — Restoring Windows Boot Manager

If your laptop boots directly into OpenCore, or if you formatted the EFI partition and Windows no longer appears in the F12 boot menu, follow these steps to restore the native **Windows Boot Manager**.

---

## 🛠️ Requirements

- A bootable Windows 10/11 USB installation media (created using Microsoft Media Creation Tool), OR access to Windows Recovery Environment (WinRE).

---

## 🚀 Step-by-Step Restoration via Command Prompt

### Step 1: Boot into Command Prompt
1. Insert the Windows USB installer into your Dell laptop.
2. Turn on the laptop and tap **F12** to open the boot menu.
3. Select the **UEFI: Windows USB**.
4. On the setup screen, select your language, then click **Next**.
5. In the bottom-left corner, click **Repair your computer** (do NOT click Install Now).
6. Click **Troubleshoot** -> **Advanced options** -> **Command Prompt**.

---

### Step 2: Identify Drive Letters Using Diskpart
In the Command Prompt window, launch `diskpart`:

```cmd
diskpart
```

List your disks and volumes:
```cmd
list disk
list volume
```

Identify two key partitions:
1. **Windows OS Partition**: Usually labeled `C:` or `D:` (format: NTFS, size ~100GB+). Note the drive letter (e.g. `C:`).
2. **EFI System Partition (ESP)**: The FAT32 partition of size ~100MB - 500MB (hidden, usually has no drive letter).

---

### Step 3: Assign a Drive Letter to the EFI Partition
Assuming your main SSD is Disk 0 and the EFI System Partition is Volume 1:

```cmd
select disk 0
list partition
select partition 1
assign letter=S
exit
```

*(Now the EFI partition is mounted as drive `S:`).*

---

### Step 4: Rebuild Windows BCD and UEFI Boot Files
Run the official Microsoft `bcdboot` command:

```cmd
bcdboot C:\Windows /s S: /f UEFI
```

*(Replace `C:\Windows` with whichever drive letter your Windows directory is located on in WinRE, e.g. `D:\Windows`).*

If successful, you will see:
```text
Boot files successfully created.
```

---

### Step 5: Test and Reboot
1. Type `exit` and restart your laptop.
2. Tap **F12** at startup.
3. You will now see **Windows Boot Manager** listed under UEFI Boot Options!
4. Select it to boot straight into Windows.
