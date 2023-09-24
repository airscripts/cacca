#!/bin/bash
set -e
echo "[1/2] Running tests..."
pdm run pytest

echo "[2/2] Run complete!"
exit 0