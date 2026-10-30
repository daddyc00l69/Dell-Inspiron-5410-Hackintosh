#!/usr/bin/env python3
"""
macOS Recovery Image Downloader & USB Deployer
Crafted for Dell Inspiron 14 5410 2-in-1 OpenCore Hackintosh Project
"""

import os
import sys
import subprocess
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MACRECOVERY_PATH = os.path.join(SCRIPT_DIR, "Utilities", "macrecovery", "macrecovery.py")

VERSIONS = {
    "1": {
        "name": "macOS 16 Tahoe (Latest)",
        "board_id": "Mac-CFF7D910A743CAAF",
        "mlb": "00000000000000000",
        "os_type": "latest"
    },
    "2": {
        "name": "macOS 15 Sequoia",
        "board_id": "Mac-7BA5B2D9E42DDD94",
        "mlb": "00000000000000000",
        "os_type": "default"
    },
    "3": {
        "name": "macOS 14 Sonoma",
        "board_id": "Mac-827FAC58A8FDFA22",
        "mlb": "00000000000000000",
        "os_type": "default"
    },
    "4": {
        "name": "macOS 13 Ventura",
        "board_id": "Mac-B4831CEBD52A0C4C",
        "mlb": "00000000000000000",
        "os_type": "default"
    },
    "5": {
        "name": "macOS 12 Monterey",
        "board_id": "Mac-E43C1C25D4880AD6",
        "mlb": "00000000000000000",
        "os_type": "default"
    },
    "6": {
        "name": "macOS 11 Big Sur",
        "board_id": "Mac-2BD1B31983FE1663",
        "mlb": "00000000000000000",
        "os_type": "default"
    }
}

def print_banner():
    print("=" * 70)
    print("       macOS Official Recovery Image Downloader & Deployer      ")
    print("         Optimized for OpenCore 1.0.8 Hackintosh Systems          ")
    print("=" * 70)
    print()

def list_removable_drives():
    drives = []
    if os.name == "nt":
        import ctypes
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
            if bitmask & (1 << (ord(letter) - ord('A'))):
                drive_str = f"{letter}:\\"
                drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive_str)
                # DRIVE_REMOVABLE = 2
                if drive_type == 2:
                    drives.append(f"{letter}:")
    return drives

def main():
    print_banner()

    print("Available macOS Recovery Versions:")
    for key, info in sorted(VERSIONS.items()):
        print(f"  [{key}] {info['name']}")
    print("  [Q] Quit")
    print()

    choice = input("Select an option (1-6, default: 1): ").strip()
    if choice.lower() == "q":
        sys.exit(0)
    if not choice:
        choice = "1"

    if choice not in VERSIONS:
        print(f"Invalid option: {choice}")
        sys.exit(1)

    selected = VERSIONS[choice]
    print(f"\nTargeting: {selected['name']}...")
    print(f"Board ID:  {selected['board_id']}")
    print(f"MLB:       {selected['mlb']}")
    print()

    out_dir = os.path.join(SCRIPT_DIR, "com.apple.recovery.boot")
    os.makedirs(out_dir, exist_ok=True)

    cmd = [
        sys.executable,
        MACRECOVERY_PATH,
        "-b", selected["board_id"],
        "-m", selected["mlb"],
        "-os", selected["os_type"],
        "-o", out_dir,
        "download"
    ]

    print("Connecting directly to Apple CDN servers...")
    print("-" * 70)
    res = subprocess.run(cmd)
    print("-" * 70)

    if res.returncode != 0:
        print("❌ Download failed. Please verify your internet connection.")
        sys.exit(res.returncode)

    dmg_path = os.path.join(out_dir, "BaseSystem.dmg")
    chunk_path = os.path.join(out_dir, "BaseSystem.chunklist")

    if os.path.exists(dmg_path) and os.path.exists(chunk_path):
        size_mb = os.path.getsize(dmg_path) / (1024 * 1024)
        print(f"\n✅ Download Verified!")
        print(f"  • BaseSystem.dmg:       {size_mb:.1f} MB")
        print(f"  • BaseSystem.chunklist: {os.path.getsize(chunk_path)} bytes")
        print(f"  • Stored at:            {out_dir}")
    else:
        print("❌ Recovery files were not found after download.")
        sys.exit(1)

    # Option to copy directly to USB
    drives = list_removable_drives()
    if drives:
        print(f"\nDetected Removable USB Drive(s): {', '.join(drives)}")
        deploy = input(f"Would you like to copy recovery files directly to your USB drive? (Y/n): ").strip().lower()
        if deploy != "n":
            target_drive = drives[0]
            if len(drives) > 1:
                target_drive = input(f"Enter target drive letter ({'/'.join(drives)}): ").strip().upper()
                if not target_drive.endswith(":"):
                    target_drive += ":"

            dest = os.path.join(f"{target_drive}\\", "com.apple.recovery.boot")
            print(f"Deploying recovery files to {dest}...")
            shutil.copytree(out_dir, dest, dirs_exist_ok=True)
            print(f"✅ Successfully deployed to {dest}!")

    print("\n🎉 Recovery setup complete! Ready for OpenCore installation.")

if __name__ == "__main__":
    main()
