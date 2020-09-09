# Interactive Azure SDK Samples

These samples use [Jupyter](https://jupyter.org) to host different runtimes that allow you to experience the Azure SDK interactively.

## Getting Started

The easiest way to run these samples is to install [Docker](https://docker.com) and run a container with everything you need. On Windows, running [Docker on Windows Subsystem for Linux version 2 (WSL2)](https://docs.docker.com/docker-for-windows/wsl) is the fastest option.

1. Install and run [Docker](https://docker.com).

2. Build the container:

   ```bash
   docker build -t azure-sdk-notebooks ./devcontainer
   ```

3. Start the container:

   ```bash
   docker run -it --rm -p 8888:8888 -v "${PWD}:/home/jovyan/work azure-sdk-notebooks
   ```

4. Click on or copy and paste the link in the terminal output. If using [Visual Studio Code](https://code.visualstudio.com) with the Python extension installed, you can also paste the link in the prompt after running `Python: Specify local or remote Jupyter server for connections`.

5. When finished, click `Ctrl+C` twice in the terminal to close the connection and shut down the container. If `--rm` was passed to `docker run`, the container is automatically deleted.
