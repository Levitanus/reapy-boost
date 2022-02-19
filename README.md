# reapy-boost

`reapy` is a nice pythonic wrapper around the quite unpythonic [ReaScript Python API](https://www.reaper.fm/sdk/reascript/reascripthelp.html#p "ReaScript Python API documentation") for [REAPER](https://www.reaper.fm/ "REAPER").

# the boost

This fork started as local copy for working on the repository as contributor. But since I've added a lot of functionality, that is still waits for approval (probably for an infinity), I made this fork to establish my own API.

So, I'll try to keep the fork as consistent as possible with the original repository, but while @RomeoDespres adds some own API which conflicts with API of the fork — they are going aside.

## feel free to contribute!

So, the baseline and base principle of the fork is to be «boosted»: review PRs as fast as possible, and, if they makes what they declare — just put them into the project. It may produce not very consistent codebase and not so clean architecture, but it will produce a stable API that can be used in the projects of contributors.

## Contents

1. [Installation](#installation)
2. [Usage](#usage)
    * [ReaScript API](#reascript-api)
    * [`reapy` API](#reapy-api)
    * [Performance](#performance)
    * [Documentation](#documentation)
3. [Contributing](#contributing)
4. [Author](#author)
5. [License](#license)

## Installation

If you feel you need more explanation than the straightforward instructions below, head to the detailed [installation guide](https://python-reapy.readthedocs.io/en/latest/install_guide.html).

reapy is available via `pip`:

```bash
$ pip install reapy-boost
```

One additional step is required to let REAPER know reapy is available. First, open REAPER. Then in a terminal, run:

```bash
$ python -c "import reapy_boost; reapy.configure_reaper()"
```

Restart REAPER, and you're all set! You can now import `reapy` from inside or outside REAPER as any standard Python module.

Instead of creating a new ReaScript containing:

```python
from reaper_python import *
RPR_ShowConsoleMsg("Hello world!")
```

you can open your usual Python shell and type:

```python
>>> import reapy_boost
>>> reapy.print("Hello world!")
```

## Usage

### ReaScript API

All ReaScript API functions are available in `reapy_boost` in the sub-module `reapy_boost.reascript_api`. Note that in ReaScript Python API, all function names start with `"RPR_"`. That unnecessary pseudo-namespace has been removed in `reapy_boost`. Thus, you shall call `reapy_boost.reascript_api.GetCursorPosition` in order to trigger `reaper_python.RPR_GetCursorPosition`. See example below.

```python
>>> from reapy_boost import reascript_api as RPR
>>> RPR.GetCursorPosition()
0.0
>>> RPR.SetEditCurPos(1, True, True)
>>> RPR.GetCursorPosition()
1.0
```

Note that if you have the [SWS extension](http://sws-extension.org/) installed, the additional ReaScript functions it provides will be available in `reapy_boost.reascript_api` and usable inside and outside REAPER as well.

### `reapy_boost` API

The purpose of `reapy_boost` is to provide a more pythonic API as a substitute for ReaScript API. Below is the `reapy_boost` way of executing the example above.

```python
>>> import reapy_boost
>>> project = reapy_boost.Project() # Current project
>>> project.cursor_position
0.0
>>> project.cursor_position = 1
>>> project.cursor_position
1.0
```
The [translation table](https://python-reapy_boost.readthedocs.io/en/latest/api_table.html) matches ReaScript functions with their `reapy_boost` counterparts.

### Performance

When used from inside REAPER, `reapy_boost` has almost identical performance than native ReaScript API. Yet when it is used from the outside, the performance is quite worse. More precisely, since external API calls are processed in a `defer` loop inside REAPER, there can only be around 30 to 60 of them per second. In a time-critical context, you should make use of the `reapy_boost.inside_reaper` context manager.

```python
>>> import reapy_boost
>>> project = reapy_boost.Project() # Current project
>>> # Unefficient (and useless) call
>>> bpms = [project.bpm for _ in range(1000)] # Takes at least 30 seconds...
>>> # Efficient call
>>> with reapy_boost.inside_reaper():
...     bpms = [project.bpm for _ in range(1000)]
...
>>> # Takes only 0.1 second!

```

While `reapy_boost.inside_reaper` saves time on defered calls, performance outside REAPER can be increased within method `map` which exsists on every notable `reapy_boost` object. Within `object.map("method_name", iterables={"arg_name":[<list of values>]}, defaults{"def_arg_name":value})` performance can be insreased with saving on socket connections between outside and inside scripts.

```python
import reapy_boost
take = reapy_boost.Project().selected_items[0].active_take

@reapy_boost.inside_reaper()
def test():
    for i in [6.0] * 1000000:
        take.time_to_ppq(6.0)

def test_map():
    take.map('time_to_ppq', iterables={'time': [6.0] * 1000000})

test()      # runs 140s
test_map()  # runs 12s as from outside as from inside
```

### Documentation

Check the [documentation](https://python-reapy.readthedocs.io/ "reapy online documentation") and especially the [API guide](https://python-reapy.readthedocs.io/en/latest/api_guide.html) and [Translation Table](https://python-reapy.readthedocs.io/en/latest/api_table.html) for more information.

## Contributing

For now, about a half of ReaScript API has a `reapy` counterpart, the docs are far from great, and many bugs are waiting to be found. Feel free to improve the project by checking the [contribution guide](CONTRIBUTING.md)!

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.
