#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"
zip -r CandyFlowERP.zip candyflow -x '*.git*' -x '__pycache__/*' -x '*.pyc' -x 'db.sqlite3'
echo "ZIP generado en: $REPO_ROOT/CandyFlowERP.zip"
