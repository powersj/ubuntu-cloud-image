# Ubuntu Cloud Image

[![Build Status](https://travis-ci.org/powersj/ubuntu-cloud-image.svg?branch=master)](https://travis-ci.org/powersj/ubuntu-cloud-image) [![Snap Status](https://build.snapcraft.io/badge/powersj/ubuntu-cloud-image.svg)](https://build.snapcraft.io/user/powersj/ubuntu-cloud-image)

Find the latest Ubuntu Images for clouds

## Install

Users can obtain ubuntu-cloud-image as a snap:

```shell
snap install ubuntu-cloud-image
```

Or via PyPI:

```shell
pip3 install ubuntu-cloud-image
```

## Usage

At the very least a user needs to provide the Ubuntu release's codename and cloud to find information for:

```shell
ubuntu-cloud-image bionic ec2
```

Other options available to a user:

* `--arch` to specify a different architecture (default: amd64)
* `--region` to filter on a specific cloud region
* `--minimal` to find a minimal image
* `--debug` provides additional verbose output

```shell
ubuntu-cloud-image <release> <cloud> [--arch <arch>] [--region <region>] [--minimal] [--debug]
```
