#!/bin/sh
echo "[1/2] Building..."
pdm run pyinstaller src/cacca/cli.py

echo "[2/2] Build complete!"
exit 0