#!/usr/bin/env bash
set -euo pipefail

# Install + verify Northflank CLI.
# Uses npm by default; falls back to yarn if npm is unavailable.

if command -v northflank >/dev/null 2>&1; then
  echo "northflank CLI already installed: $(northflank --version || true)"
else
  if command -v npm >/dev/null 2>&1; then
    echo "Installing @northflank/cli via npm..."
    npm i -g @northflank/cli
  elif command -v yarn >/dev/null 2>&1; then
    echo "Installing @northflank/cli via yarn..."
    yarn global add @northflank/cli
  else
    echo "ERROR: neither npm nor yarn is installed." >&2
    echo "Install Node.js first: https://nodejs.org/" >&2
    exit 1
  fi
fi

echo "CLI version check:"
northflank --version

echo
echo "Next step: run 'northflank login' to authenticate."
