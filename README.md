User credentials management utility

## Requirements

The package uses python 3.8 and keyring. It should be able to work with any python >= 3.8

```python
which python3
python3 --version
```

## Installation

```{python}
# Create a python virtual environment named `.venv`
python3 -m venv .venv
py -m venv .venv

# Activate the virtual environment

# For MacOS and other Unix/Linux platforms
source ./.venv/bin/activate

# For windows OS
.\.venv\Scripts\activate

# Install required packages on your virtual environment
pip install -r requirements.txt
```

## Test, Build and Install

```python
python3 -m pytest
python3 setup.py sdist bdist_wheel
python3 -m pip install -e ./dist/PyCM-<version>.tar.gz
```
