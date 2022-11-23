# reapy-boost

`reapy` is a nice pythonic wrapper around the quite unpythonic [ReaScript Python API](https://www.reaper.fm/sdk/reascript/reascripthelp.html#p "ReaScript Python API documentation") for [REAPER](https://www.reaper.fm/ "REAPER").

# the boost

This fork started as local copy for working on the repository as contributor. But since I've added a lot of functionality, that is still waits for approval (probably for an infinity), I made this fork to establish my own API.

So, I'll try to keep the fork as consistent as possible with the original repository, but while @RomeoDespres adds some own API which conflicts with API of the fork — they are going aside.

A few major features included in boost now:

- `ExtState` class, that can be used as property, or state of GUI widgets and be statically type-checked:

```Python
>>> state = reapy_boost.ExtState("my section", "my value", 5)
... print(state.value)
5
... state.value = 3
... print(state.value)
3
... del state.value
... print(state.value)
None
```

- JulianSader `JS_API` integrated in Python! All the recent functions are automatically generated from the GitHub source and availble in the `reapy_boost.JS` module. They are also statically type-checked and some broken bindings are fixed manually.

- cliffon `ReaImGui` extension is also wrapped in statically typed module and can be used directly from the module `reapy_boost.ImGui`. But I hope to introduce a pythonic gui system, based on this extension, but without leaking abstractions, so later we can have several back-ends for it. For now it is just a sketch, that works only inside `REAPER` and will be changed before the final release. But even now it look quite better that «pure» `ImGui` example:

```Python
from typing import Dict, Generator, Set
import reapy_boost as rpr
from reapy_boost import gui
from sample_editor.project import RenderedTracks



class TrackList(gui.Table):

    def len(self) -> int:
        return rpr.Project().n_tracks

    def make_rows(self, min_row: int,
                  max_row: int) -> Generator[gui.TableRow, None, None]:
        project = rpr.Project()
        rendered_tracks: rpr.ExtState[Set[str]] = rpr.ExtState(
            "levitanus sample_editor",
            "rendered tracks",
            None,
            project=project)
        tracks = project.tracks

        def on_click(track: rpr.Track, value: bool) -> None:
            _tracks = rendered_tracks.value
            if _tracks is None:
                _tracks = []
            else:
                _tracks = [rpr.Track.from_GUID(guid) for guid in value]
            if value:
                _tracks.append(track)
            else:
                _tracks.remove(track)
            rendered_tracks.value = set(track.GUID for track in _tracks)

        for row in range(min_row, max_row):
            if row >= project.n_tracks:
                break
            track = tracks[row]
            is_rendered = track in rendered_tracks.tracks
            yield gui.TableRow({
                "#": str(row),
                "name": track.name,
                "is_rendered": gui.CheckBox("")\
                    .set_click(lambda value: on_click(track, value))\
                    .set_value(is_rendered),
            })


dock_button = gui.CheckBox("dock")

content = gui.Content(
    dock_button,
    gui.Button("greet")\
        .set_click(lambda: rpr.print('hello'))\
        .width(100),
    gui.Row(
        gui.Text("my text"), gui.Button("new"), spacing=100
    ),
    TrackList("rendered tracks")
)

root = gui.Window(name="sample editor", content=content)
dock_button.state = root.docked

root.run()

```

- changed API for connection to distant machines:

```Python
import ipaddress
import reapy_boost

# add Web Interface to Raper freferences at the given location.
# reapy_boost.add_web_interface("/home/levitanus/.config/REAPER/", 4460)

# Then we can start REAPER, and connect to it with IP and port.
reapy_boost.connect(
    reapy_boost.Host(ipaddress.IPv4Address(reapy_boost.LOCALHOST), 4468)
)
reapy_boost.test_api()
```

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
$ python -c "import reapy_boost; reapy_boost.configure_reaper()"
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
>>> reapy_boost.print("Hello world!")
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
