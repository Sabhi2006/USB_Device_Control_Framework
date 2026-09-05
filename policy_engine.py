import json
from pathlib import Path


class PolicyEngine:
    def __init__(self):
        self.allowlist = self._load_policy("allowlist.json")
        self.blocklist = self._load_policy("blocklist.json")

    def _load_policy(self, filename):
        path = Path(__file__).parent / "config" / filename

        try:
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def is_authorized(self, device):
        """
        Check whether a USB device is allowed.

        Device format:
        {
            "vid": "2717",
            "pid": "FF40"
        }
        """

        vid = device.get("vid", "").upper()
        pid = device.get("pid", "").upper()

        # Blocklist takes priority
        for item in self.blocklist:
            if item.get("vid", "").upper() == vid and \
               item.get("pid", "").upper() == pid:
                return False

        # Device must be present in allowlist
        for item in self.allowlist:
            if item.get("vid", "").upper() == vid and \
               item.get("pid", "").upper() == pid:
                return True

        return False