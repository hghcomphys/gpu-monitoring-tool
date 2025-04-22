from setuptools import setup, find_packages

setup(
    name='gtop',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gtop = gtop.cli:main',
        ],
    },
    install_requires=[
        'nvidia-ml-py>=11.450.129',
        'plotext>=5.2.8',
    ],
    # python_requires='>=3.8',
)

