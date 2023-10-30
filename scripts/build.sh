#!/bin/bash
set -e
echo "[1/2] Building..."
pdm run pyinstaller -n cacca -F src/cacca/cli.py
pdm run pyinstaller -n node -F src/cacca/node.py

echo "[2/2] Build complete!"
exit 0