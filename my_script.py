import json
import os
import platform
import shutil
from datetime import datetime, timezone

def detect_os():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"

disk = shutil.disk_usage("/")

data = {
    "os_name": detect_os(),
    "os_version": platform.release(),
    "architecture": platform.machine(),
    "hostname": platform.node(),
    "username": os.environ.get("USER") or os.environ.get("USERNAME") or "unknown",
    "free_disk_gb": round(disk.free / (1024 ** 3), 2),
    "started_at": datetime.now(timezone.utc).isoformat(),
}

with open("os_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
