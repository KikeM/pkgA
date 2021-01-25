from setuptools import find_packages, setup

setup(
    name             = 'pkgA',
    packages         = find_packages(),
    install_requires = [
        'pip-install-test>0.4',
        'pkgB@git+https://github.com/mmngreco/pkgB.git#egg=pkgB-0'
    ],
)

