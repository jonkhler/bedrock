#!/usr/bin/env sh
set -eu

BEDROCK_HOME="${BEDROCK_HOME:-$HOME/.bedrock}"
BIN_DIR="${BIN_DIR:-$HOME/.local/bin}"

echo "Installing bedrock to $BEDROCK_HOME..."

# Clone or update
if [ -d "$BEDROCK_HOME" ]; then
    cd "$BEDROCK_HOME" && git pull --ff-only
else
    git clone https://github.com/jonkhler/bedrock.git "$BEDROCK_HOME"
fi

# Symlink binary
mkdir -p "$BIN_DIR"
ln -sf "$BEDROCK_HOME/bin/bedrock" "$BIN_DIR/bedrock"

echo "Installed. Make sure $BIN_DIR is on your PATH."
echo ""
echo "Quick start:"
echo "  bedrock ~/dev/my-app \"Python 3.13, uv, pyright strict, pytest\""
echo ""
echo "Run 'bedrock --help' for all options."
