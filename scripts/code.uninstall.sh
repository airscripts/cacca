#!/bin/bash
set -e
echo "[1/2] Uninstalling..."
cat .vscode/extensions.list | xargs -L 1 code --uninstall-extension

echo "[2/2] Uninstall complete!"
exit 0