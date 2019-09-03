# Introduction

This package is used to debug an issue found with `pip-18` and the command
`--process-dependency-links`. 

In collaboration with @mmngreco

# Problem description
A non-PyPi package has the following dependencies:
    - PyPi package (here `numpy` is a proxy).
    - Another non-PyPi package (pkgB) which has the same PyPi package as a dependency.

## Version specification

Our package (`pkgA`) requires a greater or equal version of the PyPi package, while
`pkgB` fixes the version of the PyPi package.

## Issue

Despite the fact that `pkgB` fixes a specific version of our PyPi library, 
`pip` ignores this fact and goes ahead installing the highest available version
of the PyPi package. This creates an unfeasible situation, where `pkgB` and the
PyPi library with an incompatible version coexist in the same environment.

# Code snippets

A couple of useful copy-paste lines to reproduce the mistakes

## No respect for the fixed version

`pkgB` has `numpy==1.14`.

```bash
git checkout standard
pip install --process-dependency-links -I -U --no-cache-dir .
pip list | grep numpy
```

## Totally incompatible versions

`pkgB` has `numpy==1.13`.

```bash
git checkout crash
pip install --process-dependency-links -I -U --no-cache-dir .
pip list | grep numpy
```
