# 02 — Switching SATA Back to RAID or Keeping AHCI

When you install macOS, you must switch your Dell BIOS from **RAID On** to **AHCI / NVMe**.
If you attempt to boot existing Windows installations without preparation, Windows will throw the blue screen error:
`INACCESSIBLE_BOOT_DEVICE`

This guide shows you how to safely switch between AHCI and RAID without reinstalling Windows.

---

## 🔄 Scenario A: Keeping AHCI Mode for Dual-Boot (Recommended)

Running Windows in **AHCI mode** is completely supported by Microsoft and has zero performance loss compared to RAID On. To fix an existing Windows installation that blue-screens after switching to AHCI:

### If Windows is still bootable (Before switching):
1. In Windows, right-click the Start Menu and select **Terminal (Admin)** or **Command Prompt (Admin)**.
2. Run:
   ```cmd
   bcdedit /set {current} safeboot minimal
   ```
3. Restart into BIOS (**F2**).
4. Change **SATA Operation** from `RAID On` to **`AHCI / NVMe`**.
5. Save settings and reboot.
6. Windows will boot into Safe Mode and automatically enable the native Microsoft AHCI driver (`storahci.sys`).
7. In Safe Mode, open Command Prompt as Administrator and run:
   ```cmd
   bcdedit /deletevalue {current} safeboot
   ```
8. Restart normally. Windows will now boot permanently in AHCI mode!

### If you already switched and Windows won't boot:
1. Turn on laptop and tap **F2** to enter BIOS.
2. Switch **SATA Operation** back to **RAID On**.
3. Save and boot into Windows.
4. Follow steps 1-8 above!

---

## 🔙 Scenario B: Completely Switching Back to Factory RAID On

If you want to return your Dell laptop 100% to stock factory settings:

1. In Windows (while still in AHCI), run in Admin Command Prompt:
   ```cmd
   bcdedit /set {current} safeboot minimal
   ```
2. Restart into BIOS (**F2**).
3. Change **SATA Operation** back to **RAID On**.
4. Save and restart. Windows will boot in Safe Mode and load the Intel VMD / RST RAID storage driver (`iaStorVD.sys`).
5. Open Admin Command Prompt in Safe Mode and run:
   ```cmd
   bcdedit /deletevalue {current} safeboot
   ```
6. Restart. Your laptop is back to Dell factory RAID On mode!
