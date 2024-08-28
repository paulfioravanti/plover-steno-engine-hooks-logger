# Plover Steno Engine Hooks Logger

[![Build Status][Build Status image]][Build Status url] [![linting: pylint][linting image]][linting url]


[Plover][] uses [Engine Hooks][] to allow [plugins][] to listen to its
[steno engine][] events. This hybrid [extension][]/[GUI Tool][] plugin simply
connects into all the known Engine Hooks, and logs out the given parameters to
the [Plover log][], which can be handy during Plover plugin development.

## Install

This plugin is not currently planned to go in the [Plover Plugins Registry][],
nor published to [PyPI][], since its only really useful for developers during
development. Therefore, it can be installed using [git][]:

```console
git clone git@github.com:paulfioravanti/plover-steno-engine-hooks-logger.git
cd plover-steno-engine-hooks-logger
plover --script plover_plugins install --editable .
```

> Where `plover` in the command is a reference to your locally installed version
> of Plover. See the [Invoke Plover from the command line][] page for details on
> how to create that reference.

When necessary, the plugin can be uninstalled via the command line with the
following command:

```console
plover --script plover_plugins uninstall plover-steno-engine-hooks-logger
```

## Usage

Since both the Extension and GUI Tool logging cover the same ground, you will
likely only want to have one open at a single time (depending on what kind of
plugin you are developing), otherwise the logs will get very noisy.

### Enabling the Extension

- After re-opening Plover, open the Configuration screen (either click the
  Configuration icon, or from the main Plover application menu, select
  `Preferences...`)
- Open the Plugins tab
- Check the box next to `plover_steno_engine_hooks_logger_extension` to activate
  the plugin

### Enabling the GUI Tool

- After re-opening Plover, click the Steno Engine Hooks Logger button on the
  Plover UI.

Once you have installed the plugin and restarted Plover, open up `plover.log`
under Plover's configuration directory:

- Windows: `C:\Users\<your username>\AppData\Local\plover\plover`
- macOS: `~/Library/Application Support/plover`
- Linux: `~/.config/plover`

There, you should see entries there prefixed with `[STENO ENGINE HOOK]`.

If you ever find the logs getting too noisy, then comment out any of the hooks
you don't need to listen to in the `_HOOKS` list.

## Development

If you are a [Tmuxinator][] user, you may find my
[plover_steno_engine_hooks_logger project file][] of reference.

### Python Version

Plover's Python environment currently uses version 3.9 (see Plover's
[`workflow_context.yml`][] to confirm the current version).

So, in order to avoid unexpected issues, use your runtime version manager to
make sure your local development environment also uses Python 3.9.x.

### Type Checking and Linting

- [Mypy][] is used for static type checking
- [Pylint][] is used for code quality

Run type checking and linting with the following commands:

```console
mypy plover_steno_engine_hooks_logger
pylint plover_steno_engine_hooks_logger
```

If you are a [`just`][] user, you may find the [`justfile`][] useful during
development in running multiple test commands. You can run the following command
from the project root directory:

```console
just --working-directory . --justfile test/justfile
```

### Deploying Changes

After making any code changes, install the plugin into Plover with the following
command:

```console
plover --script plover_plugins install --editable .
```

When necessary, the plugin can be uninstalled via the command line with the
following command:

```console
plover --script plover_plugins uninstall plover-q-and-a
```

[Build Status image]: https://github.com/paulfioravanti/plover-steno-engine-hooks-logger/actions/workflows/ci.yml/badge.svg
[Build Status url]: https://github.com/paulfioravanti/plover-steno-engine-hooks-logger/actions/workflows/ci.yml
[Engine Hooks]: https://plover.readthedocs.io/en/latest/api/engine.html#engine-hooks
[extension]: https://plover.readthedocs.io/en/latest/plugin-dev/extensions.html
[git]: https://git-scm.com/
[GUI Tool]: https://plover.readthedocs.io/en/latest/plugin-dev/gui_tools.html
[Invoke Plover from the command line]: https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line
[`just`]: https://github.com/casey/just
[`justfile`]: ./justfile
[linting image]: https://img.shields.io/badge/linting-pylint-yellowgreen
[linting url]: https://github.com/pylint-dev/pylint
[Mypy]: https://github.com/python/mypy
[Plover]: https://www.openstenoproject.org/
[Plover log]: https://plover.readthedocs.io/en/latest/api/log.html
[Plover Plugins Registry]: https://github.com/openstenoproject/plover_plugins_registry
[plover_steno_engine_hooks project file]: https://github.com/paulfioravanti/dotfiles/blob/master/tmuxinator/plover_steno_engine_hooks.yml
[plugins]: https://plover.readthedocs.io/en/latest/plugins.html
[Pylint]: https://github.com/pylint-dev/pylint
[PyPI]: https://pypi.org/
[steno engine]: https://plover.readthedocs.io/en/latest/api/engine.html
[Tmuxinator]: https://github.com/tmuxinator/tmuxinator
[`workflow_context.yml`]: https://github.com/openstenoproject/plover/blob/master/.github/workflows/ci/workflow_context.yml
