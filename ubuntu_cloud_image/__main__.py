# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image main module."""

import argparse
import sys

from . import image

CLOUDS = {
    'azure': image.Azure,
    'aws': image.AWS,
    'aws-cn': image.AWSChina,
    'aws-govcloud': image.AWSGovCloud,
    'gce': image.GCE,
    'kvm': image.KVM,
    'lxc': image.LXC,
    'maasv2': image.MAASv2,
    'maasv3': image.MAASv3
}


def parse_args():
    """Set up command-line arguments."""
    parser = argparse.ArgumentParser('ubuntu-cloud-image')
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'

    azure = subparsers.add_parser(
        'azure',
        help='Microsoft Azure'
    )
    azure.add_argument(
        '--region',
        required=True,
        help='TODO'
    )
    azure.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    azure.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )

    aws = subparsers.add_parser(
        'aws',
        help='Amazon Web Services'
    )
    aws.add_argument(
        '--region',
        required=True,
        help='TODO'
    )
    aws.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    aws.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )
    aws.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    aws.add_argument(
        '--root-store',
        default='ssd',
        choices=['ssd', 'instance'],
        help='TODO'
    )

    aws_cn = subparsers.add_parser(
        'aws-cn',
        help='Amazon Web Services China'
    )
    aws_cn.add_argument(
        '--region',
        required=True,
        help='TODO'
    )
    aws_cn.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    aws_cn.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )
    aws_cn.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    aws_cn.add_argument(
        '--root-store',
        default='ssd',
        choices=['ssd', 'instance'],
        help='TODO'
    )

    aws_govcloud = subparsers.add_parser(
        'aws-govcloud',
        help='Amazon Web Services GovCloud'
    )
    aws_govcloud.add_argument(
        '--region',
        required=True,
        help='TODO'
    )
    aws_govcloud.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    aws_govcloud.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )
    aws_govcloud.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    aws_govcloud.add_argument(
        '--root-store',
        default='ssd',
        choices=['ssd', 'instance'],
        help='TODO'
    )

    gce = subparsers.add_parser(
        'gce',
        help='Google Compute Engine'
    )
    gce.add_argument(
        '--region',
        required=True,
        help='TODO'
    )
    gce.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    gce.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    gce.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )

    kvm = subparsers.add_parser(
        'kvm',
        help='Kernel-based Virtual Machine'
    )
    kvm.add_argument(
        '--arch',
        default='amd64',
        help='TODO'
    )
    kvm.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    kvm.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    kvm.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )

    lxc = subparsers.add_parser(
        'lxc',
        help='Linux Containers'
    )
    lxc.add_argument(
        '--arch',
        default='amd64',
        help='TODO'
    )
    lxc.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    lxc.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )
    lxc.add_argument(
        '--minimal',
        action='store_true',
        help='TODO'
    )

    maasv2 = subparsers.add_parser(
        'maasv2',
        help='Metal as a Service (Version 2)'
    )
    maasv2.add_argument(
        '--arch',
        default='amd64',
        help='TODO'
    )
    maasv2.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    maasv2.add_argument(
        '--kernel',
        default='generic',
        help='TODO'
    )
    maasv2.add_argument(
        '--daily',
        action='store_true',
        help='TODO'
    )

    maasv3 = subparsers.add_parser(
        'maasv3',
        help='Metal as a Service (Version 3)'
    )
    maasv3.add_argument(
        '--arch',
        default='amd64',
        help='TODO'
    )
    maasv3.add_argument(
        '--release',
        required=True,
        help='TODO'
    )
    maasv3.add_argument(
        '--kernel',
        default='generic',
        help='TODO'
    )

    return parser.parse_args()


def launch():
    """Launch ubuntu-cloud-image."""
    cli = parse_args()
    cloud = vars(cli).pop('command')
    args = vars(cli)

    print(cloud)
    print(args)
    cloud = CLOUDS[cloud](**args)
    print(cloud.find())


if __name__ == '__main__':
    sys.exit(launch())
