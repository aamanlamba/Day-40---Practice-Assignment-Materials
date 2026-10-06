import json, time, random

class LegacyAdapter:
    def __init__(self, endpoint="http://legacy-host.local/api"):
        self.endpoint = endpoint

    def fetch(self, payload):
        # Simulates an old integration contract; no real external call is made.
        time.sleep(0.001)
        return {
            "status": "OK",
            "legacyCode": random.choice(["00", "00", "00", "91"]),
            "payload": payload,
            "raw": json.dumps(payload),
        }
