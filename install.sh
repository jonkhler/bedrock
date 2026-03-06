#!/usr/bin/env sh
set -eu

BEDROCK_HOME="${BEDROCK_HOME:-$HOME/.bedrock}"

echo "Installing bedrock to $BEDROCK_HOME..."

# Clone or update
if [ -d "$BEDROCK_HOME" ]; then
    cd "$BEDROCK_HOME" && git pull --ff-only
else
    git clone https://github.com/jonkhler/bedrock.git "$BEDROCK_HOME"
fi

# Install CLI via uv
if command -v uv >/dev/null 2>&1; then
    uv tool install --force "$BEDROCK_HOME"
    echo "Installed via uv tool."
else
    echo "uv not found. Install uv first: https://docs.astral.sh/uv/getting-started/installation/"
    echo "Then run: uv tool install $BEDROCK_HOME"
    exit 1
fi

echo ""
echo "Quick start:"
echo "  bedrock new ~/dev/my-app \"Python 3.13, uv, pyright strict, pytest\""
echo ""
echo "Run 'bedrock --help' for all options."
