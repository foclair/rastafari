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


## Release

To release a new version of Rastafari, bump the version number in
`src/rastafari/__init__.py` and create a git tag starting with a lower
case `v` followed by the new version number.  [GitLab's
releases][gitlab-release] is the recommended way to create this tag
for non-prereleases.

Remember that you can create pre-release versions and install them
with [pip's --pre flag][pip-pre] if you want to test a feature with
another package without affecting other users of this package.

[gitlab-release]: https://git.smhi.se/foclair/rastafari/-/releases
[pip-pre]: https://pip.pypa.io/en/stable/cli/pip_install/#pre-release-versions


## Maintenance

This package is maintained by [FO Luft][] at SMHI.

[FO Luft]: mailto:foluftadmin@smhi.se
