# Introduction

This package is used to debug an issue found with `pip-18` and the command
`--process-dependency-links`. 

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