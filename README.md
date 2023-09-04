# Plover Steno Engine Hooks Logger

[Plover][] uses [Engine Hooks][] to allow [plugins][] to listen to its
[steno engine][] events. This [extension][] plugin simply connects into all the
known Engine Hooks, and logs out the given parameters to the [Plover log][],
which can be handy during Plover plugin development.

## Install

This plugin is not currently planned to go in the [Plover Plugins Registry][],
nor published to [PyPI][], since its only really useful for developers during
development. Therefore, it can be installed using [git][]:

```sh
git clone git@github.com:paulfioravanti/plover-steno-engine-hooks-logger.git
cd plover-steno-engine-hooks-logger
plover -s plover_plugins install .
```

> Where `plover` in the command is a reference to your locally installed version
> of Plover. See the [Invoke Plover from the command line][] page for details on
> how to create that reference.

- After re-opening Plover, open the Configuration screen (either click the
  Configuration icon, or from the main Plover application menu, select
  `Preferences...`)
- Open the Plugins tab
- Check the box next to `plover_steno_engine_hooks_logger` to activate the
  plugin

## Usage

Once you have installed the plugin and restarted Plover, open up `plover.log`
under Plover's configuration directory:

- Windows: `C:\Users\<your username>\AppData\Local\plover\plover`
- macOS: `~/Library/Application Support/plover`
- Linux: `~/.config/plover`

There, you should see entries there prefixed with `[STENO ENGINE HOOK]`.

If you ever find the logs getting too noisy, then comment out any of the hooks
you don't need to listen to in the `_HOOKS` list.

[Engine Hooks]: https://plover.readthedocs.io/en/latest/api/engine.html#engine-hooks
[extension]: https://plover.readthedocs.io/en/latest/plugin-dev/extensions.html
[git]: https://git-scm.com/
[Invoke Plover from the command line]: https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line
[Plover]: https://www.openstenoproject.org/
[Plover log]: https://plover.readthedocs.io/en/latest/api/log.html
[Plover Plugins Registry]: https://github.com/openstenoproject/plover_plugins_registry
[plugins]: https://plover.readthedocs.io/en/latest/plugins.html
[PyPI]: https://pypi.org/
[steno engine]: https://plover.readthedocs.io/en/latest/api/engine.html
