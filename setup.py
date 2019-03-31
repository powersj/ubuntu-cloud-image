# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image setup.py."""

import os
from setuptools import find_packages, setup


def read_readme():
    """Read and return text of README.md."""
    pwd = os.path.abspath(os.path.dirname(__name__))
    readme_file = os.path.join(pwd, 'README.md')
    with open(readme_file, 'r') as readme:
        readme_txt = readme.read()

    return readme_txt


def gather_deps():
    """Read requirements.txt and pre-process for setup.

    Returns:
         list of packages and dependency links.

    """
    default = open('requirements.txt', 'r').readlines()
    new_pkgs = []
    links = []
    for resource in default:
        if 'git+https' in resource.strip():
            links.append(resource)
        else:
            new_pkgs.append(resource)

    return new_pkgs, links


PKGS, LINKS = gather_deps()

setup(
    name='ubuntu-cloud-image',
    version='19.1',
    description='Download the newest Ubuntu cloud images.',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Joshua Powers',
    author_email='josh.powers@canonical.com',
    url='https://github.com/powersj/ubuntu-cloud-image',
    download_url=(
        'https://github.com/powersj/ubuntu-cloud-image/tarball/master'
    ),
    python_requires='>=3.4',
    install_requires=PKGS,
    dependency_links=LINKS,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
    keywords=['ubuntu', 'image', 'cloud'],
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['ubuntu-cloud-image=ubuntu_cloud_image.__main__:launch']
    },
    zip_safe=True
)
