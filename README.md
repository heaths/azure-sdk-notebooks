# Interactive Azure SDK Samples

These samples use [Jupyter](https://jupyter.org) to host different runtimes that allow you to experience the Azure SDK interactively.

## Getting Started

The easiest way to run these samples is to install [Docker](https://docker.com) and run a container with everything you need. On Windows, running [Docker on Windows Subsystem for Linux version 2 (WSL2)](https://docs.docker.com/docker-for-windows/wsl) is the fastest option.

### Visual Studio Code: Development Containers

You can open this workspace directory in [Visual Studio Code](https://code.visualstudio.com) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extensions installed.

Soon after Code has opened, you should be prompted to reopen Code in a container automatically; however, you can also do so manually:

1. Press `F1` (default binding) to open the command window.

2. Type "Remote-Containers: Reopen in Container" and press enter with the command selected.

This will restart Code and build the container, which may take a few minutes. After the workspace folder is displayed in Code, you can open or create _\*.ipynb_ notebooks, execute command blocks, or make changes as desired.

If you would like to use the Jupyter Notebook browser experience instead, navigate to <http://127.0.0.1:8888?token=vscode>.

### Docker

You can also manually build and run the container:

1. Build the container:

   ```bash
   docker build -t azure-sdk-notebooks .devcontainer
   ```

2. Start the container:

   ```bash
   docker run -it --rm -p 8888:8888 -v "${PWD}:/home/jovyan/work" azure-sdk-notebooks
   ```

3. Navigate to <http://127.0.0.1:8888?token=vscode> or, if using [Visual Studio Code](https://code.visualstudio.com) with the Python extension installed, paste that link into the prompt after running `Python: Specify local or remote Jupyter server for connections`.

When finished, click `Ctrl+C` twice in the terminal to close the connection and shut down the container. If `--rm` was passed to `docker run`, the container is automatically deleted but any changes to the file system will be saved since you passed a volume mount using `-v`.
