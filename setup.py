from setuptools import find_packages, setup

setup(
    name             = 'pkgA',
    packages         = find_packages(),
    install_requires = [
        'numpy>=1.14',
        'pkgB'
    ],
    dependency_links = [
        'git+https://github.com/mmngreco/pkgB.git#egg=pkgB-0']
)

