import json
import os

class Memory:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

        self.files = {
            "profile": os.path.join(base_path, "profile.json"),
            "ideas": os.path.join(base_path, "ideas.json"),
            "progress": os.path.join(base_path, "progress.json")
        }

        # Initialize files if they don't exist
        for path in self.files.values():
            if not os.path.exists(path):
                with open(path, "w") as f:
                    json.dump({}, f)

    def load(self, key):
        path = self.files.get(key)
        if not path:
            raise ValueError(f"Unknown memory key: {key}")

        with open(path, "r") as f:
            return json.load(f)

    def save(self, key, data):
        path = self.files.get(key)
        if not path:
            raise ValueError(f"Unknown memory key: {key}")

        with open(path, "w") as f:
            json.dump(data, f, indent=2)