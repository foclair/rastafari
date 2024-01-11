# Rastafari

Rasterize vector features. This library is built to rasterize emission sources in the CLAIR air quality modelling system. In contrast to most available libraries used to rasterize vector features, this library produces rasters with weights proportional to the fraction of each cell that is covered by a feature.


### Features:

* line rasterization using DDA algorithm producing weights for fractions of cell
* polygon rasterization using polygon fill
* mass-consistent resampling of rasters to another resolution and projection

## Install

Use pip to install Rastafari:

```console
python -m pip install rastafari
```


## Development

To install Rastafari in a local venv for development, run:
```console
git clone https://gitlab.com/foclair/rastafari.git
cd rastafari
sudo yum install python3.11-devel
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install cython wheel
RASTAFARI_USE_CYTHON=1 python -m pip install --no-build-isolation -e .[test]
```

Rastafari uses [pre-commit][].  Install it and run `pre-commit
install` to run its checks every time you commit.  Run the checks
manually with

```console
pre-commit run -a
```

[pytest][] is used as a test runner:

```console
pytest
```

Rastafari comes fully typed.  Use [mypy][] to check the type annotations:

```console
mypy .
```

All these tools will be run in CI in case you forget.

[mypy]: https://www.mypy-lang.org/
[pre-commit]: https://pre-commit.com/
[pytest]: https://pytest.org/
[pip-tools]: https://github.com/jazzband/pip-tools/


## Release

To release a new version of Rastafari, bump the version number in
`src/rastafari/__init__.py` and create a git tag starting with a lower
case `v` followed by the new version number.

Remember that you can create pre-release versions and install them
with [pip's --pre flag][pip-pre] if you want to test a feature with
another package without affecting other users of this package.

[pip-pre]: https://pip.pypa.io/en/stable/cli/pip_install/#pre-release-versions


## Maintenance

This package is maintained by [FO Luft][] at SMHI.

[FO Luft]: mailto:foluftadmin@smhi.se
