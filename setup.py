from setuptools import setup, find_packages

setup(
    name='resize_gifs',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'resize_gifs=src.resize_gif:process_gifs_from_urls',
        ],
    },
    author='Idan Levian <eidan66: eidan47@gmail.com>',
    description='A package to download and resize GIFs',
    url='https://github.com/eidan66/resize_gifs',
)