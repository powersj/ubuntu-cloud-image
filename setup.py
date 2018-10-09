# This file is part of ubuntu-cloud-image. See LICENSE for license information.
"""Ubuntu Cloud Image setup.py."""

import os
from setuptools import find_packages, setup

PWD = os.path.abspath(os.path.dirname(__name__))
README_FILE = os.path.join(PWD, 'README.md')
with open(README_FILE, 'r') as readme:
    README_TEXT = readme.read()

setup(
    name='ubuntu-cloud-image',
    version='18.1',
    description='Download the newest Ubuntu cloud images.',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    author='Joshua Powers',
    author_email='josh.powers@canonical.com',
    url='https://github.com/powersj/ubuntu-cloud-image',
    download_url=(
        'https://github.com/powersj/ubuntu-cloud-image/tarball/master'
    ),
    python_requires='>=3.4',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later"
        " (GPLv3+)",
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
