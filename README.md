# MacnicaDHW Embedded Linux Yocto Project Platform

## Getting Repo tool:

To get the platform you need to have `repo` installed and use it as:

Install the `repo` utility:

```shell
sudo apt install repo
```

## Download the platform source:

To download all sources run the following commands:

``` shell
mkdir macnica-yocto-platform
cd macnica-yocto-platform
repo init -u git@github.com:MacnicaDHW/yocto-platform.git
repo sync
```

At the end of the commands, you have every metadata you need to start work with.

## Setup the environment:

Before run `bitbake` setup the environment running:

``` shell
source ./setup-environment build
```

## Building images

To build `core-image-base` run:

``` shell
$ bitbake core-image-base
```

At the end of build the image will be avaiable in build/tmp/deploy/images/$MACHINE
