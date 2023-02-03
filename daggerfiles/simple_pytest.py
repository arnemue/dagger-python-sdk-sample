"""Execute a command."""

import sys

import anyio
import dagger


async def test():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")

        python = (
            client.container()
            # pull container
            .from_("python:3.11-slim-bullseye")
            # mount source directory
            .with_mounted_directory("/ws", src)
            # change working directory
            .with_workdir("/ws")
            # install package and test dependencies
            .with_exec(["pip", "install", "-e", ".[test]"])
            # execute tets
            .with_exec(["pytest", "-v", "tests"])
        )

        # execute
        py_stdout = await python.stdout()

    print(py_stdout)


if __name__ == "__main__":
    anyio.run(test)
