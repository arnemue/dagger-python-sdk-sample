# Simple project to experiment with the Dagger Python SDK

The code which is used to run pytest (src and tests folder) comes from https://github.com/ArjanCodes/2022-test-existing-code

Use Python 3.14.7 and Docker. The Dagger SDK is pinned to 0.21.10 and provisions
the matching CLI and engine automatically.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r .devcontainer/requirements.txt -e '.[test]'
python -m pytest -v tests
make run
```

`make run` runs the tests in `python:3.14.7-slim-trixie` through Dagger. For a
network that uses a custom CA, place its PEM certificate in
`$XDG_CONFIG_HOME/dagger/ca-certificates` (or `~/.config/dagger/ca-certificates`
when `XDG_CONFIG_HOME` is unset) before starting the engine. Dagger installs
these certificates in the engine and test container; pip uses the system CA
bundle with certificate verification enabled.
