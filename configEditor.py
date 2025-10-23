"""
configEditor.py - Edit and validate config.json for Personal Paraphrase

Supports both standalone use and integration into a multi-module config manager.
"""

import json
import os
import shutil

CONFIG_PATH = "config.json"
BACKUP_PATH = "config_backup.json"

# 🧠 Load Config
def load_config(path=CONFIG_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# 💾 Save Config
def save_config(config, path=CONFIG_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {path}")

# 🛡️ Backup Config
def backup_config(path=CONFIG_PATH, backup_path=BACKUP_PATH):
    if os.path.exists(path):
        shutil.copy(path, backup_path)
        print(f"Backup created at {backup_path}")

# 🔍 View Config
def view_config(config):
    print(json.dumps(config, indent=2))

# 🛠 Edit Key
def edit_key(config, section, key, new_value):
    if section not in config:
        raise KeyError(f"Section '{section}' not found in config.")
    config[section][key] = new_value
    print(f"Updated [{section}][{key}] → {new_value}")
    return config

# 🧪 Validate Config (basic)
def validate_config(config):
    required_sections = ["persona_resolution", "chat_history", "llm"]
    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section: {section}")
    print("Config validation passed.")

# 🚀 Standalone CLI
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Edit Personal Paraphrase config.json")
    parser.add_argument("--view", action="store_true", help="View current config")
    parser.add_argument("--edit", nargs=3, metavar=("SECTION", "KEY", "VALUE"), help="Edit a config value")
    parser.add_argument("--validate", action="store_true", help="Validate config structure")
    args = parser.parse_args()

    try:
        config = load_config()
        if args.view:
            view_config(config)
        if args.edit:
            section, key, value = args.edit
            backup_config()
            config = edit_key(config, section, key, value)
            save_config(config)
        if args.validate:
            validate_config(config)
    except Exception as e:
        print(f"Error: {e}")
