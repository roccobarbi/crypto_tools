from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crypto_tools",
    packages=find_packages(exclude=['tests*']),
    version="1.0.7",
    author="Rocco Barbini",
    author_email="roccobarbi@gmail.com",
    description="Tools that can be used to build software for breaking \"traditional\" cyphers and codes.",
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
    long_description=long_description,
    url="https://github.com/roccobarbi/crypto_tools",
    download_url="https://github.com/roccobarbi/crypto_tools/releases/tag/1.0.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
