# crypto_tools

> An open-source, python library that helps you build software for breaking "traditional" cyphers and codes
> (cryptograms too).

At this early stage in this project, this README is designed with two users in mind:
* developers who want to use this library within their software;
* developers who want to contribute to build crypto_tools.

When the project will become large enough, most of the information needed by the audiences listed above will be moved
to a different place (most likely a dedicated website). Then the main purpose of this README will become that of
providing the information that everyone expects to find on pypi.org, plus an index of the other available resources.

**Table of Contents**
* [Usage](#Usage)
* [Contribute](#Contribute)

<a name="Usage"></a>

## Usage

The package can be installed by running:

```
pip install crypto-tools 
```

It can then be imported with:

```
import crypto_tools
```

or using a from... import... statement. Please note the different naming (- vs. _), which was originally caused by an
error when setting up the project in pypi.

The package is made of the sub-packages that follow.

### utils

Generally short functions written to avoid repetition in the rest of the package. This doesn't generally need to be
imported.

### data

Data files used by the rest of the package. This doesn't generally need to be imported, unless you're planning to
rewrite on your own some of the logics provided by the package.

### stats

Tools that help you compute basic statistics on the text that you're analysing, such as calculating letter or ngram
frequencies, or the index of coincidence.

### analysis

Tools that help you analyse a cyphertext before you apply other cryptoanalytic techniques (e.g. to estimate the
probable language of an unknown cyphertext).

<a name="Contribute"></a>

## Contribute

to do