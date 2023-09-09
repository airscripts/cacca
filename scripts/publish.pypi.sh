#!/bin/bash
set -e
echo "[1/2] Publishing to PyPi..."
pdm publish

echo "[2/2] Publish complete!"
exit 0