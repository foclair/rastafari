# Rastafari

Rasterize vector features to grids.

## Development

Rastafari uses [pre-commit][].  Install it and run `pre-commit
install` to run its checks every time you commit.  It will also be run
in the CI pipeline in case you forget.

To update the test requirements in the CI job, install [pip-tools][]
and run

```console
pip-compile setup.cfg --extra test -o test-requirements.txt
```

Add the `--upgrade` flag if you want to update the existing
requirements to the latest version.

[pre-commit]: https://pre-commit.com/
[pip-tools]: https://github.com/jazzband/pip-tools/


## Maintenance

This package is maintained by [FO Luft][] at SMHI.

[FO Luft]: mailto:foluftadmin@smhi.se
