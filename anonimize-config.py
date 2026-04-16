import json
import os

CONFIG_FILE = "openclaw.json"
TEMPLATE_FILE = "openclaw.template.json"

# Substrings that indicate a secret key
SECRET_SUBSTRINGS = [
    "apikey",
    "api-key",
    "api_key",
    "_key",
    "token",
    "secret",
    "password",
    "credential",
    "access",
    "refresh",
    "auth",
]

# Exact keys to skip redaction for (exceptions)
ALLOWLIST = ["provider", "mode", "auth", "profiles", "google-antigravity-auth", "tokens", "maxTokens"]


def is_secret(key):
    # Check allowlist first
    if key in ALLOWLIST:
        return False

    k_lower = key.lower()
    # auth is tricky because "auth": {...} contains config, but "token" is inside.
    # We recurse, so we only redact leaf values or specific keys.
    # If the key itself is "auth", we don't redact the whole object, we descend.
    # But if the key is "authToken", we redact the value.

    # Actually, my redact function descends dictionaries.
    # It only marks a value as REDACTED if we are at a key that looks like a secret
    # AND the value is not a dictionary (or list).
    return any(s in k_lower for s in SECRET_SUBSTRINGS)


def redact(data):
    if isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                new_data[k] = redact(v)
            elif is_secret(k):
                new_data[k] = "<REDACTED>"
            else:
                new_data[k] = v
        return new_data
    elif isinstance(data, list):
        return [redact(item) for item in data]
    else:
        return data


def main():
    if not os.path.exists(CONFIG_FILE):
        print(f"Config file {CONFIG_FILE} not found.")
        return

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

        sanitized = redact(config)

        with open(TEMPLATE_FILE, "w") as f:
            json.dump(sanitized, f, indent=2)

        print(f"Sanitized config written to {TEMPLATE_FILE}")
    except Exception as e:
        print(f"Error processing config: {e}")


if __name__ == "__main__":
    main()
