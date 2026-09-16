"""
package_project.py - RetinaXAI Production ZIP Packager
Packages all source code, SQLite database, documentation, and launchers into
a clean, standalone distribution zip file for hackathon presentation and client handoff.
"""

import os
import zipfile
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_NAME = "RetinaXAI_Commercial_v2.0.zip"
ZIP_PATH = os.path.join(PROJECT_DIR, ZIP_NAME)

EXCLUDED_DIRS = {'__pycache__', '.git', '.vscode', '.idea', '.gemini'}
EXCLUDED_FILES = {ZIP_NAME, '.DS_Store', 'package_project.py'}

def create_zip():
    print(f"Creating standalone distribution package: {ZIP_NAME}...")
    file_count = 0

    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            # Prune excluded directories in-place
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

            for file in files:
                if file in EXCLUDED_FILES or file.endswith('.pyc'):
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_DIR)
                
                # Add to zip
                zipf.write(full_path, rel_path)
                file_count += 1
                print(f"  + Added: {rel_path}")

    size_mb = os.path.getsize(ZIP_PATH) / (1024 * 1024)
    print("=" * 60)
    print(" PACKAGE GENERATION COMPLETE!")
    print(f" Total files bundled: {file_count}")
    print(f" Output Archive:      {ZIP_PATH}")
    print(f" Archive Size:        {size_mb:.2f} MB")
    print("=" * 60)
    return ZIP_PATH

if __name__ == '__main__':
    create_zip()
