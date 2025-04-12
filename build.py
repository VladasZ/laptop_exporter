#!/usr/bin/env python3

import subprocess
import os
import shutil


def run_cmd(cmd, check=True):
    print(f"\n▶️ Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error:\n{result.stderr}")
        if check:
            exit(1)
    else:
        print(f"✅ Done:\n{result.stdout.strip()}")
    return result


def ensure_cross_installed():
    if not shutil.which("cross"):
        print("🔧 Installing `cross`...")
        run_cmd(["cargo", "install", "cross"])
    else:
        print("✅ `cross` is already installed.")


def ensure_targets_installed():
    targets = ["x86_64-unknown-linux-gnu", "aarch64-unknown-linux-gnu"]
    for target in targets:
        run_cmd(["rustup", "target", "add", target], check=False)


def build_target(target):
    print(f"🔨 Building for {target}...")
    run_cmd(["cross", "build", "--target", target, "--release"])


if __name__ == "__main__":
    ensure_cross_installed()
    ensure_targets_installed()

    build_target("x86_64-unknown-linux-gnu")
    build_target("aarch64-unknown-linux-gnu")
