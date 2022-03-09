import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from SpamRobo.utils import load_plugins
import logging
from telethon import events
from . import anon, anon2, anon3, anon4, anon5, anon6, anon7, anon8, anon9, anon10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "SpamRobo/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Spam Robo Successfully deployed !")
print("Now open telegram add your and your enemy in same chat and fuck him up.")
print(" Don't forget to visit @DevilsHeavenMF")

if __name__ == "__main__":
    anon.run_until_disconnected()
    
if __name__ == "__main__":
    anon2.run_until_disconnected()

if __name__ == "__main__":
    anon3.run_until_disconnected()
    
if __name__ == "__main__":
    anon4.run_until_disconnected()

if __name__ == "__main__":
    anon5.run_until_disconnected()
    
if __name__ == "__main__":
    anon6.run_until_disconnected()
    
if __name__ == "__main__":
    anon7.run_until_disconnected()

if __name__ == "__main__":
    anon8.run_until_disconnected()
    
if __name__ == "__main__":
    anon9.run_until_disconnected()

if __name__ == "__main__":
    anon10.run_until_disconnected()    
