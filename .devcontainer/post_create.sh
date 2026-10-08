#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")/.."
# The SDK provisions the matching CLI and engine when make run starts.
python -m pip install -r .devcontainer/requirements.txt -e '.[test]'
