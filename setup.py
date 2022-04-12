import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crypto_tools",
    version="0.0.1",
    author="Rocco Barbini",
    author_email="roccobarbi@gmail.com",
    description="Tools that can be used to build software for breaking \"traditional\" cyphers and codes.",
    long_description=long_description,
    download_url="https://github.com/roccobarbi/crypto_tools/releases/tag/0.0.1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
