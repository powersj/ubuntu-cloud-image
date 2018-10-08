# Ubuntu Cloud Image

[![Build Status](https://travis-ci.org/powersj/ubuntu-cloud-image.svg?branch=master)](https://travis-ci.org/powersj/ubuntu-cloud-image) [![Snap Status](https://build.snapcraft.io/badge/powersj/ubuntu-cloud-image.svg)](https://build.snapcraft.io/user/powersj/ubuntu-cloud-image)

Find the latest Ubuntu images for clouds

This is used to find the latest Ubuntu image information for clouds. The following clouds are supported:

    Amazon Web Services (aws)
    Amazon Web Services China (aws-cn)
    Amazon Web Services GovCloud (aws-govcloud)
    Microsoft Azure (azure)
    Google Compute Engine (gce)
    Kernel-based Virtual Machine (kvm)
    Linux Containers (lxc)
    Metal as a Service (MAAS) Version 2 (maasv2)
    Metal as a Service (MAAS) Version 3 (maas)

The program uses the streams output provided by various clouds to determine the latest images available on clouds. Where they are supported this includes the latest daily, minimal, and daily minimal images as well. Daily and minimal images are enabled with the `--daily` and `--minimal` flags.

The output is the full JSON output from streams providing details about the requested image. If no image matches the specific filter then an empty JSON array is printed.

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

At the very least a user needs to provide the cloud name and Ubuntu release's codename to find image information for:

```shell
ubuntu-cloud-image kvm bionic
```

Other options available to a user based on the cloud.
