# Tool to generate cog
import os.path
import sys
from pathlib import Path


cog_name = sys.argv[1]

if not cog_name.endswith("Cog"):
    cog_name += "Cog"

cog_template = f"""
import logging

from discord import app_commands
from discord.ext import commands

from nameless import Nameless, shared_vars

__all__ = ["{cog_name}"]

class {cog_name}(commands.Cog):
    def __init__(self, bot: Nameless):
        self.bot = bot


async def setup(bot: Nameless):
    await bot.add_cog({cog_name}(bot))
    logging.info("%s cog added!", __name__)


async def teardown(bot: Nameless):
    await bot.remove_cog({cog_name}.__cog_name__)
    logging.warning("%s cog removed!", __name__)
"""

path = Path(os.path.dirname(__file__))

with open(path.parent / "nameless" / "cogs" / f"{cog_name}.py", "w+") as f:
    f.write(cog_template)

print(f"Cog {cog_name} generated!")
