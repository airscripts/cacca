#!/bin/bash
set -e
echo "[1/4] Setting things up..."

echo "[2/4] Installing pdm dependencies..."
pdm add

echo "[3/4] Installing nvm dependencies..."
source ~/.nvm/nvm.sh
nvm install

echo "[4/4] Setup complete!"
exit 0