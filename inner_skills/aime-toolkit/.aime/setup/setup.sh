#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"
ln -sf "$SKILL_DIR/bin/aime" /usr/local/bin/aime
echo "aime cli installed to /usr/local/bin/aime"
