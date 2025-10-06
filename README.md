```
                          --------------------------
                        /                            \
                     ------------------------------------
                    /                                    \
        -------------------------------------------------
        /                            /\/\/\/\/\ 
        ---------------------------------------------------
                  |        F  i  e  l  d  T  r  i  p       |
                  ------------------------------------------
                   \                                      /
                     ------------------------------------
                          \            /
                            ----------
```

# The Python interface to _[FieldTrip](https://www.fieldtriptoolbox.org)_
<!-- ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fieldtrip-python)
![PyPI - License](https://img.shields.io/pypi/l/fieldtrip-python)
![PyPI - Version](https://img.shields.io/pypi/v/fieldtrip-python)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/fieldtrip/fieldtrip-python/.github%2Fworkflows%2Frun_unit_tests.yml) -->

> [!WARNING]
> This project is **young** and might contain bugs.
> **If you experience any issues, please [let us know](https://github.com/fieldtrip/fieldtrip-python/issues)!**

## Installation instructions

### Important - Windows

Python installation made from Microsoft Store on Windows will not work
(raises DeclarativeService.dll not found), install it from Python website.

### Important - Python/MATLAB compatibility

Specific versions of MATLAB are compatible with
[specific versions of Python](https://uk.mathworks.com/support/requirements/python-compatibility.html).

By default, `fieldtrip-python` uses R2025b, which is compatible with Python 3.10-3.13. 

### Option 1 - Install the MATLAB runtime on first use

1. Install FieldTrip-Python
   ```shell
   pip install fieldtrip-python
   ```
2. Start Python 
   ```shell
   python
   ```
3. Calling a FieldTrip function will try to locate or install MATLAB Runtime. 
   ```python 
   import fieldtrip
   ft_info('Hello, world')
   ``` 
4. Follow the instructions to install the runtime

- **Advantages**
  - Installs the runtime that is required for your python version
  - Does not resintall anything if a compatible runtime already exists
- **Drawbacks**
  - May need to be run in proviledged mode (e.g., `sudo`)
  - May be fiddly on Windows

### Option 2 - Install the MATLAB runtime manually

1. Install the appropriate [MATLAB Runtime](https://uk.mathworks.com/products/compiler/matlab-runtime.html)
2. Install FieldTrip:
   ```python
   pip install fieldtrip-python
   ```

- **Advantages**
  - Graphical interface for installing the runtime
- **Drawbacks**
  - The correct runtime must be selected for your python version

### Option 3 - Install the MATLAB runtime using an installation script

1. Install FieldTrip-Python
   ```shell
   pip install fieldtrip-python
   ```
2. Run the installer
   ```shell
   install_matlab_runtime --version R2025b --yes
   ```

- **Advantages**
  - Exposes installation options (`install_matlab_runtime --help`)
- **Drawbacks**
  - For advanced users

