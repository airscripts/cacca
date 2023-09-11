#!/bin/bash
set -e
echo "[1/2] Installing..."
cat .vscode/extensions.list | xargs -L 1 code --install-extension

echo "[2/2] Install complete!"
exit 0