#!/usr/bin/env python3
import re
import sys
from datetime import datetime

def update_readme_timestamp(readme_path="README.md"):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

        # Pattern to find the existing marker
        pattern = r"<!-- LAST_VALIDATED: -->.*?<!-- /LAST_VALIDATED -->"
        replacement = f"<!-- LAST_VALIDATED: -->**{current_time}** <!-- /LAST_VALIDATED -->"

        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content)
            action = "updated"
        else:
            # Append new section if marker doesn't exist
            new_content = content.rstrip() + f"\n\n---\n\n<!-- LAST_VALIDATED: -->**{current_time}** <!-- /LAST_VALIDATED -->"
            action = "added"

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ README timestamp {action} successfully: {current_time}")
        return True

    except Exception as e:
        print(f"❌ Error updating README: {e}")
        return False

if __name__ == "__main__":
    success = update_readme_timestamp()
    sys.exit(0 if success else 1)