# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image class."""

import json
import logging
import os

from .streams import Streams


class Image:
    """Base cloud image to set default mirror URL and keyring."""

    name = 'unknown'

    def __init__(self, release, arch, daily=False, minimal=False):
        """Initialize base image."""
        self._log = logging.getLogger(__name__)

        self.release = release
        self.arch = arch
        self.daily = daily
        self.minimal = minimal

        self.mirror_url = self._mirror_url()

    def __repr__(self):
        """Return string representation of class."""
        return '%s%s%s (%s) image for %s' % (
            'daily ' if self.daily else '',
            'minimal ' if self.minimal else '',
            self.release,
            self.arch,
            self.name
        )

    @property
    def filter(self):
        """Create filter."""
        return []

    def _mirror_url(self):
        """Create mirror URL baed on filter settings."""
        mirror_base_url = 'https://cloud-images.ubuntu.com'

        if self.minimal and self.daily:
            return '%s/minimal/daily/' % mirror_base_url

        if self.minimal:
            return '%s/minimal/releases/' % mirror_base_url

        if self.daily:
            return '%s/daily/' % mirror_base_url

        return '%s/releases/' % mirror_base_url

    def search(self):
        """Find list of images with the setup filter.

        Returns:
            dictionary of discovered image

        Raises:
            SystemExit: when no results found

        """
        keyring_path = '/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg'
        snap = os.getenv('SNAP')
        if snap:
            keyring_path = '%s%s' % (snap, keyring_path)

        stream = Streams(
            mirror_url=self.mirror_url,
            keyring_path=keyring_path
        )

        try:
            result = stream.query(self.filter)[0]
        except IndexError:
            result = {}

        self._log.info(json.dumps(result, sort_keys=True, indent=4))


class AWS(Image):
    """AWS class."""

    name = 'AWS'

    def __init__(self, release, arch, region, root_store='ssd',
                 daily=False, minimal=False):
        """Initialize AWS instance.

        Args:
            release: str, Ubuntu release codename
            arch: str, architecture of image
            region: str, Cloud region
            root_store: str, either ssd or instance
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(release, arch, daily, minimal)

        self.region = region
        self.root_store = root_store

    def __repr__(self):
        """Return string representation of class."""
        return '%s%s%s (%s) image for %s (%s)' % (
            'daily ' if self.daily else '',
            'minimal ' if self.minimal else '',
            self.release,
            self.arch,
            self.name,
            self.region
        )

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'endpoint=https://ec2.%s.amazonaws.com' % self.region,
            'region=%s' % self.region,
            'release=%s' % self.release,
            'root_store=%s' % self.root_store,
            'virt=hvm',
        ]


class AWSChina(AWS):
    """AWS China class."""

    name = 'AWS China'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'endpoint=https://ec2.%s.amazonaws.com.cn' % self.region,
            'region=%s' % self.region,
            'release=%s' % self.release,
            'root_store=%s' % self.root_store,
            'virt=hvm',
        ]


class AWSGovCloud(AWS):
    """AWS GovCloud class."""

    name = 'AWS GovCloud'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'endpoint=https://ec2.%s.amazonaws-govcloud.com' % self.region,
            'region=%s' % self.region,
            'release=%s' % self.release,
            'root_store=%s' % self.root_store,
            'virt=hvm',
        ]


class Azure(Image):
    """Azure class."""

    name = 'Azure'

    def __init__(self, release, arch, region, daily=False):
        """Initialize Azure instance.

        No minimal images.

        Args:
            release: str, Ubuntu release codename
            arch: str, architecture of image
            region: str, Cloud region
            daily: boolean, find daily image (default: false)
        """
        super().__init__(release, arch, daily)

        self.region = region

    def __repr__(self):
        """Return string representation of class."""
        return '%s%s%s (%s) image for %s (%s)' % (
            'daily ' if self.daily else '',
            'minimal ' if self.minimal else '',
            self.release,
            self.arch,
            self.name,
            self.region
        )

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'endpoint=https://management.core.windows.net/',
            'region=%s' % self.region,
            'release=%s' % self.release
        ]


class GCE(Image):
    """GCE class."""

    name = 'GCE'

    def __init__(self, release, arch, region, daily=False, minimal=False):
        """Initialize GCE instance.

        Args:
            release: str, Ubuntu release codename
            arch: str, architecture of image
            region: str, Cloud region
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(release, arch, daily, minimal)

        self.region = region

    def __repr__(self):
        """Return string representation of class."""
        return '%s%s%s (%s) image for %s (%s)' % (
            'daily ' if self.daily else '',
            'minimal ' if self.minimal else '',
            self.release,
            self.arch,
            self.name,
            self.region
        )

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'endpoint=https://www.googleapis.com',
            'region=%s' % self.region,
            'release=%s' % self.release
        ]


class KVM(Image):
    """KVM class."""

    name = 'KVM'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'ftype=disk1.img',
            'release=%s' % self.release
        ]


class LXC(Image):
    """LXC class."""

    name = 'LXC'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'ftype=squashfs',
            'release=%s' % self.release
        ]


class MAASv2(Image):
    """MAAS v2 class."""

    name = 'MAAS (v2)'

    def __init__(self, release, arch, kernel='generic', daily=False):
        """Initialize MAAS v2 instance.

        This uses the older v2 API.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            kernel: str, kernel flavor (default: generic)
            daily: boolean, find daily image (default: false)
        """
        super().__init__(release, arch, daily)

        self.kernel = kernel

        if daily:
            self.mirror_url = 'https://images.maas.io/ephemeral-v2/daily/'
        else:
            self.mirror_url = 'https://images.maas.io/ephemeral-v2/releases/'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'ftype=root-image.gz',
            'kflavor=%s' % self.kernel,
            'release=%s' % self.release
        ]


class MAASv3(Image):
    """MAAS v3 class."""

    name = 'MAAS'

    def __init__(self, release, arch, kernel='generic'):
        """Initialize MAAS v3 instance.

        The newest image API.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            kernel: str, kernel flavor (default: generic)
        """
        super().__init__(release, arch)

        self.kernel = kernel
        self.mirror_url = 'https://images.maas.io/ephemeral-v3/daily/'

    @property
    def filter(self):
        """Create filter."""
        return [
            'arch=%s' % self.arch,
            'ftype=squashfs',
            'kflavor=%s' % self.kernel,
            'release=%s' % self.release
        ]
