# Copyright 2020 Heath Stewart.
# Licensed under the MIT License. See LICENSE.txt in the project root for license information.

ARG BASE=jupyter/base-notebook
FROM $BASE

LABEL maintainer="Heath Stewart (https://github.com/heaths)"

ENV DOTNET_CLI_TELEMETRY_OPTOUT=1 \
    DOTNET_NOLOGO=1 \
    PATH="$PATH:/home/$NB_USER/.dotnet/tools" \
    TZ=America/Los_Angeles

# Install dependencies as root.
USER root

RUN export DEBIAN_FRONTEND=noninteractive \
    # Prepare .NET.
 && wget -qO /tmp/packages-microsoft-prod.deb https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb \
 && dpkg -i /tmp/packages-microsoft-prod.deb \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    lsb-release \
    git \
    gnupg \
    # Prepare Azure CLI.
 && curl -sL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor \
    | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null \
 && AZ_REPO=$(lsb_release -cs) \
 && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" \
    | tee /etc/apt/sources.list.d/azure-cli.list \
    # Install new packages.
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    azure-cli \
    dotnet-sdk-3.1 \
    # Install the bash kernel to use Azure CLI.
 && conda install --quiet --yes \
    "bash_kernel=0.7.2" \
    # Clean up.
 && rm -f /tmp/packages-microsoft-prod.deb \
 && conda clean -fy --all \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Switch back to running the container as non-root.
USER $NB_UID

# Install .NET global tools as user.
RUN dotnet tool install -g Microsoft.dotnet-interactive \
 && dotnet interactive jupyter install

# Set notebook folder on startup.
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
