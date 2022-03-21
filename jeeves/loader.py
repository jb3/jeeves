import glob, inspect, importlib

from discord import app_commands


def find_mods():
    mods = []

    for mod in glob.glob("jeeves/groups/*.py"):
        mod = mod.removesuffix(".py")
        mod = ".".join(mod.split("/"))

        module = importlib.import_module(mod)

        for _, mod in inspect.getmembers(module):
            if isinstance(mod, type) and issubclass(mod, app_commands.Group):
                mods.append(mod)

    return mods
