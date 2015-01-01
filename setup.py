#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='beat',
    version='0.1.3',
    description=('Swatch Internet Time conversion(beats)'),
    author='Tony Garcia',
    author_email='tonysk8@gmx.net',
    entry_points={
        'console_scripts': [
            'beat=beat.beat:main'
        ]
    },
    packages=['beat'],
    url = 'https://github.com/tonyskapunk/beat',
    download_url = 'https://github.com/tonyskapunk/beat/tarball/0.1.r3',
    license = "GNU General Public License v3 (GPLv3)",
    zip_safe=False
)
