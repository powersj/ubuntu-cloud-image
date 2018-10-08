# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image class."""

from .streams import Streams


class Image:
    """Base cloud image to set default mirror URL and keyring."""

    def __init__(self, daily=False, minimal=False):
        """Initialize base image."""
        self.filter = None
        self.keyring_path = '/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg'

        mirror_base_url = 'https://cloud-images.ubuntu.com/'
        if minimal and daily:
            self.mirror_url = '%s/minimal/daily/' % mirror_base_url
        elif minimal:
            self.mirror_url = '%s/minimal/releases/' % mirror_base_url
        elif daily:
            self.mirror_url = '%s/daily/' % mirror_base_url
        else:
            self.mirror_url = '%s/releases/' % mirror_base_url

    def find(self):
        """Find list of images with the setup filter.

        Returns:
            list of dictionaries of images

        """
        stream = Streams(
            mirror_url=self.mirror_url,
            keyring_path=self.keyring_path
        )

        try:
            return stream.query(self.filter)[0]
        except IndexError:
            return {}


class AWS(Image):
    """AWS class."""

    def __init__(self, release=None, region=None, root_store='ssd',
                 daily=False, minimal=False):
        """Initialize AWS instance.

        Args:
            release: str, Ubuntu release codename
            region: str, Cloud region
            root_store: str, either ssd or instance
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(daily, minimal)

        self.filter = [
            'arch=amd64',
            'endpoint=https://ec2.%s.amazonaws.com' % region,
            'region=%s' % region,
            'release=%s' % release,
            'root_store=%s' % root_store,
            'virt=hvm',
        ]


class AWSChina(AWS):
    """AWS China class."""

    def __init__(self, release=None, region=None, root_store='ssd'):
        """Initialize AWS China instance.

        No daily or minimal images.

        Args:
            release: str, Ubuntu release codename
            region: str, Cloud region
            root_store: str, either ssd or instance
        """
        super().__init__()

        self.filter = [
            'arch=amd64',
            'endpoint=https://ec2.%s.amazonaws.com.cn' % region,
            'region=%s' % region,
            'release=%s' % release,
            'root_store=%s' % root_store,
            'virt=hvm',
        ]


class AWSGovCloud(AWS):
    """AWS GovCloud class."""

    def __init__(self, release=None, region=None, root_store='ssd'):
        """Initialize AWS instance.

        No daily or minimal images.

        Args:
            release: str, Ubuntu release codename
            region: str, Cloud region
            root_store: str, either ssd or instance
        """
        super().__init__()

        self.filter = [
            'arch=amd64',
            'endpoint=https://ec2.%s.amazonaws-govcloud.com' % region,
            'region=%s' % region,
            'release=%s' % release,
            'root_store=%s' % root_store,
            'virt=hvm',
        ]


class Azure(Image):
    """Azure class."""

    def __init__(self, release=None, region=None, daily=False):
        """Initialize Azure instance.

        No minimal images.

        Args:
            release: str, Ubuntu release codename
            region: str, Cloud region
            daily: boolean, find daily image (default: false)
        """
        super().__init__(daily)

        self.filter = [
            'arch=amd64',
            'endpoint=https://management.core.windows.net/',
            'region=%s' % region,
            'release=%s' % release
        ]


class GCE(Image):
    """GCE class."""

    def __init__(self, release=None, region=None, daily=False, minimal=False):
        """Initialize GCE instance.

        Args:
            release: str, Ubuntu release codename
            region: str, Cloud region
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(daily, minimal)

        self.filter = [
            'arch=amd64',
            'endpoint=https://www.googleapis.com',
            'region=%s' % region,
            'release=%s' % release
        ]


class KVM(Image):
    """KVM class."""

    def __init__(self, release=None, arch='amd64', daily=False, minimal=False):
        """Initialize KVM instance.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(daily, minimal)

        self.filter = [
            'arch=%s' % arch,
            'ftype=disk1.img',
            'release=%s' % release
        ]


class LXC(Image):
    """LXC class."""

    def __init__(self, release=None, arch='amd64', daily=False, minimal=False):
        """Initialize KVM instance.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            daily: boolean, find daily image (default: false)
            minimal: boolean, find minimal image (default: false)
        """
        super().__init__(daily, minimal)

        self.filter = [
            'arch=%s' % arch,
            'ftype=squashfs',
            'release=%s' % release
        ]


class MAASv2(Image):
    """MAAS v2 class."""

    def __init__(self, release=None, arch='amd64', kernel='generic',
                 daily=False):
        """Initialize MAAS v2 instance.

        This uses the older v2 API.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            kernel: str, kernel flavor (default: generic)
            daily: boolean, find daily image (default: false)
        """
        super().__init__(daily)

        if daily:
            self.mirror_url = 'https://images.maas.io/ephemeral-v2/daily/'
        else:
            self.mirror_url = 'https://images.maas.io/ephemeral-v2/releases/'

        self.filter = [
            'arch=%s' % arch,
            'ftype=root-image.gz',
            'kflavor=%s' % kernel,
            'release=%s' % release
        ]


class MAASv3(Image):
    """MAAS v3 class."""

    def __init__(self, release=None, arch='amd64', kernel='generic'):
        """Initialize MAAS v3 instance.

        The newest image API.

        Args:
            release: str, Ubuntu release codename
            arch: str, base architecture
            kernel: str, kernel flavor (default: generic)
        """
        super().__init__()

        self.mirror_url = 'https://images.maas.io/ephemeral-v3/daily/'

        self.filter = [
            'arch=%s' % arch,
            'ftype=squashfs',
            'kflavor=%s' % kernel,
            'release=%s' % release
        ]
