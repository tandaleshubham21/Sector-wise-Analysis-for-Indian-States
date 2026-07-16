#!/usr/bin/env python3
import yaml
import os
import sys

def validate_yaml_files(directory=".github/workflows"):
    error_found = False
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        yaml.safe_load(f)
                    print(f'✅ {path} is valid YAML')
                except yaml.YAMLError as e:
                    print(f'❌ {path} has YAML error: {e}')
                    error_found = True
                except Exception as e:
                    print(f'❌ {path} error: {e}')
                    error_found = True

    if error_found:
        print("\n❌ YAML validation failed!")
        sys.exit(1)
    else:
        print("\n✅ All YAML files are valid!")

if __name__ == "__main__":
    validate_yaml_files()