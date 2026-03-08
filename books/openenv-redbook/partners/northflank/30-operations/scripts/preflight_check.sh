#!/usr/bin/env bash
set -euo pipefail

echo "== Northflank preflight =="

echo "[1/4] Node/npm"
node --version
npm --version

echo "[2/4] CLI binary"
if ! command -v northflank >/dev/null 2>&1; then
  echo "northflank CLI missing. Run setup_northflank_cli.sh"
  exit 1
fi
northflank --version

echo "[3/4] Auth hint"
echo "Run: northflank login"

echo "[4/4] Team/project targets"
echo "Team: lebot-gameon"
echo "Project: Hackathon"

echo "Preflight complete."
