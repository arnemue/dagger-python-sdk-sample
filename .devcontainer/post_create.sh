#!/usr/bin/env bash

cd /usr/local
curl -L https://dl.dagger.io/dagger/install.sh | sudo sh
cd -
pip3 install -r .devcontainer/requirements.txt
