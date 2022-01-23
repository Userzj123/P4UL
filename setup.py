from setuptools import setup, find_packages
import glob

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='P4UL',
    version='0.0.1',
    description='This repository contains a wide range of python scripts for data pre- and post-processing.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='PALM-4U',
    author='Mikko J.S. Auvinen',
    url='https://github.com/Userzj123/P4UL',
    download_url='https://github.com/Userzj123/P4UL/releases',
    install_requires=['numpy', 'scipy', 'matplotlib', ],
    packages=['pyLib',],
    scripts=glob.glob('**/*.py'),
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    
)