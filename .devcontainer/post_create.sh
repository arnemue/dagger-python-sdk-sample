#!/usr/bin/env bash

pip3 install -r .devcontainer/requirements.txt
mkdir $HOME/.oh-my-zsh/completions
just --completions zsh > $HOME/.oh-my-zsh/completions/_just.zsh
