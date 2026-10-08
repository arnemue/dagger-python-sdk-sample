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
            .from_("python:3.14.7-slim-trixie")
            # mount source directory
            .with_mounted_directory("/ws", src)
            # change working directory
            .with_workdir("/ws")
            # Use the system CA bundle, including custom CAs installed by Dagger.
            .with_env_variable("PIP_CERT", "/etc/ssl/certs/ca-certificates.crt")
            # install package and test dependencies
            .with_exec(["pip", "install", "-e", ".[test]"])
            # execute tests
            .with_exec(["pytest", "-v", "tests"])
        )

        # execute
        py_stdout = await python.stdout()

    print(py_stdout)


if __name__ == "__main__":
    anyio.run(test)
