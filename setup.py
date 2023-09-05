from setuptools import find_packages, setup

setup(
    name = "PyCM",
    packages = find_packages(include=['pycm']),
    version = "0.0.1",
    description = "Python based Credentials Management",
    author = "Me",
    license = "MIT",
    install_requires = ['keyring==24.2.0'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest==7.4.1'],
    test_suite = 'tests',
)
