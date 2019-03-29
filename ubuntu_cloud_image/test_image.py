# This file is part of ubuntu-bug-triage. See LICENSE file for license info.
"""Test view module."""
from .image import (
    Image, AWS, AWSChina, AWSGovCloud, Azure, GCE, KVM, LXC, MAASv2, MAASv3
)


def test_image():
    """TODO."""
    image = Image('bionic', 'amd64')
    assert image.mirror_url == 'https://cloud-images.ubuntu.com/releases/'
    assert not image.daily
    assert not image.minimal
    assert not image.filter
    assert str(image) == 'bionic (amd64) image for unknown'


def test_image_daily():
    """TODO."""
    image = Image('trusty', 's390x', daily=True)
    assert image.mirror_url == 'https://cloud-images.ubuntu.com/daily/'
    assert image.daily
    assert not image.minimal
    assert str(image) == 'daily trusty (s390x) image for unknown'


def test_image_daily_minimal():
    """TODO."""
    image = Image('bionic', 'ppc64el', minimal=True, daily=True)
    assert image.mirror_url == 'https://cloud-images.ubuntu.com/minimal/daily/'
    assert image.daily
    assert image.minimal
    assert str(image) == 'daily minimal bionic (ppc64el) image for unknown'


def test_image_minimal():
    """TODO."""
    image = Image('xenial', 'arm64', minimal=True)
    assert image.mirror_url == (
        'https://cloud-images.ubuntu.com/minimal/releases/'
    )
    assert not image.daily
    assert image.minimal
    assert str(image) == 'minimal xenial (arm64) image for unknown'


def test_aws():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'
    region = 'us-west-2'

    image = AWS(release, arch, region)
    assert str(image) == '%s (%s) image for AWS (%s)' % (release, arch, region)
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws.com' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_aws_daily():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'
    region = 'us-west-2'

    image = AWS(release, arch, region, daily=True)
    assert str(image) == (
        'daily %s (%s) image for AWS (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws.com' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_aws_daily_minimal():
    """TODO."""
    release = 'trusty'
    arch = 'ppc64el'
    region = 'us-west-1'

    image = AWS(release, arch, region, daily=True, minimal=True)
    assert str(image) == (
        'daily minimal %s (%s) image for AWS (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws.com' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_aws_minimal():
    """TODO."""
    release = 'bionic'
    arch = 'arm64'
    region = 'us-east-2'

    image = AWS(release, arch, region, minimal=True)
    assert str(image) == (
        'minimal %s (%s) image for AWS (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws.com' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_aws_china():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'
    region = 'us-west-2'

    image = AWSChina(release, arch, region)
    assert str(image) == (
        '%s (%s) image for AWS China (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws.com.cn' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_aws_govcloud():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'
    region = 'us-west-2'

    image = AWSGovCloud(release, arch, region)
    assert str(image) == (
        '%s (%s) image for AWS GovCloud (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://ec2.%s.amazonaws-govcloud.com' % region,
        'region=%s' % region,
        'release=%s' % release,
        'root_store=ssd',
        'virt=hvm',
    ]


def test_azure():
    """TODO."""
    release = 'bionic'
    arch = 'amd64'
    region = 'west-us-2'

    image = Azure(release, arch, region)
    assert str(image) == (
        '%s (%s) image for Azure (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://management.core.windows.net/',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_azure_daily():
    """TODO."""
    release = 'disco'
    arch = 'amd64'
    region = 'west-us-2'

    image = Azure(release, arch, region, daily=True)
    assert str(image) == (
        'daily %s (%s) image for Azure (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://management.core.windows.net/',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_gce():
    """TODO."""
    release = 'trusty'
    arch = 'amd64'
    region = 'us-central1'

    image = GCE(release, arch, region)
    assert str(image) == '%s (%s) image for GCE (%s)' % (release, arch, region)
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://www.googleapis.com',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_gce_daily():
    """TODO."""
    release = 'xenial'
    arch = 'arm64'
    region = 'us-west2'

    image = GCE(release, arch, region, daily=True)
    assert str(image) == (
        'daily %s (%s) image for GCE (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://www.googleapis.com',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_gce_daily_minimal():
    """TODO."""
    release = 'trusty'
    arch = 'amd64'
    region = 'us-central1'

    image = GCE(release, arch, region, daily=True, minimal=True)
    assert str(image) == (
        'daily minimal %s (%s) image for GCE (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://www.googleapis.com',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_gce_minimal():
    """TODO."""
    release = 'bionic'
    arch = 'ppc64el'
    region = 'us-east1'

    image = GCE(release, arch, region, minimal=True)
    assert str(image) == (
        'minimal %s (%s) image for GCE (%s)' % (release, arch, region)
    )
    assert image.filter == [
        'arch=%s' % arch,
        'endpoint=https://www.googleapis.com',
        'region=%s' % region,
        'release=%s' % release
    ]


def test_kvm():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'

    image = KVM(release, arch)
    assert str(image) == '%s (%s) image for KVM' % (release, arch)
    assert image.filter == [
        'arch=%s' % arch,
        'ftype=disk1.img',
        'release=%s' % release
    ]


def test_lxc():
    """TODO."""
    release = 'xenial'
    arch = 'amd64'

    image = LXC(release, arch)
    assert str(image) == '%s (%s) image for LXC' % (release, arch)
    assert image.filter == [
        'arch=%s' % arch,
        'ftype=squashfs',
        'release=%s' % release
    ]


def test_maasv2():
    """TODO."""
    release = 'cosmic'
    arch = 'ppc64el'
    kernel = 'generic'

    image = MAASv2(release, arch, kernel)
    assert str(image) == '%s (%s) image for MAAS (v2)' % (release, arch)
    assert image.filter == [
        'arch=%s' % arch,
        'ftype=root-image.gz',
        'kflavor=%s' % kernel,
        'release=%s' % release
    ]


def test_maasv2_daily():
    """TODO."""
    release = 'cosmic'
    arch = 'ppc64el'
    kernel = 'generic'

    image = MAASv2(release, arch, kernel, daily=True)
    assert str(image) == 'daily %s (%s) image for MAAS (v2)' % (release, arch)
    assert image.filter == [
        'arch=%s' % arch,
        'ftype=root-image.gz',
        'kflavor=%s' % kernel,
        'release=%s' % release
    ]


def test_maasv3():
    """TODO."""
    release = 'bionic'
    arch = 'amd64'
    kernel = 'generic'

    image = MAASv3(release, arch, kernel)
    assert str(image) == '%s (%s) image for MAAS' % (release, arch)
    assert image.filter == [
        'arch=%s' % arch,
        'ftype=squashfs',
        'kflavor=%s' % kernel,
        'release=%s' % release
    ]
