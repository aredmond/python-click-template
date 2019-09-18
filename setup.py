import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-click-app",
    version="0.0.1",
    author="Andrew Redmond",
    author_email="andrewpredmond@gmail.com",
    description="python click app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user/repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Optional
        'console_scripts': [
            'pyclick=src.entry_point:entry_point',
        ],
    },
)