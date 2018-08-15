# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image class."""

from .streams import Streams


class Image:
    """TODO."""

    def __init__(self, minimal=False, daily=False):
        """TODO."""
        self.filter = None
        self.keyring_path = '/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg'

        if minimal and daily:
            self.mirror_url = 'https://cloud-images.ubuntu.com/minimal/daily/'
        elif minimal:
            self.mirror_url = 'https://cloud-images.ubuntu.com/minimal/releases/'
        elif daily:
            self.mirror_url = 'https://cloud-images.ubuntu.com/daily/'
        else:
            self.mirror_url = 'https://cloud-images.ubuntu.com/releases/'

    def find(self):
        """Find list of images with the setup filter.

        Returns:
            list of dictionaries of images

        """
        stream = Streams(
            mirror_url=self.mirror_url,
            keyring_path=self.keyring_path
        )

        return stream.query(self.filter)[0]


class Azure(Image):
    """TODO."""
    # no minimal


class AWS(Image):
    """TODO.

    https://bugs.launchpad.net/cloud-images/+bug/1458825
    """

    def __init__(self, release=None, region=None, root_store='ssd',
                 minimal=False, daily=False):
        """TODO."""
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
    """TODO."""
    # only release, no minimal or daily


class AWSGovCloud(AWS):
    """TODO."""
    # only release, no minimal or daily


class GCE(Image):
    """TODO."""
    # all


class KVM(Image):
    """TODO.

    We should print sha256sum
    """
    # all


class LXC(Image):
    """TODO.

    We should print sha256sum
    """
    # all


class MAASv2(Image):
    """TODO.
    https://images.maas.io/ephemeral-v2/daily/
    https://images.maas.io/ephemeral-v2/releases/
    """
    # no minimal


class MAASv3(Image):
    """TODO.

    https://images.maas.io/ephemeral-v3/daily/
    """
    # only daily, no release or minimal
