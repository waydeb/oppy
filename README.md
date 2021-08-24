# oppy (op.py)

oppy is the wrapper for use on the osu! v2 api. 
Version 1.0.0

![version](https://img.shields.io/pypi/v/op.py?style=for-the-badge)
![downloads](https://img.shields.io/pypi/dm/op.py?style=for-the-badge)
![status](https://img.shields.io/pypi/status/op.py?style=for-the-badge)

## Installation

To install please use pip to install oppy

```bash
pip install op.py
```

## Usage - User Data

```python
import oppy
import asyncio
client = oppy.Client()
user = client.user_data
async def main():
    data = await user.user(user="peppy", token="a long string") #makes the api request using oppy.Client.user_data.user()
    print(
    data.pp, # User PP
    data.id, # User ID
    data.username, # Username
    data.global_rank, # User Global Rank
    ) # returns the users raw pp, id, name and global rank
asyncio.get_event_loop().run_until_complete(main())
```

## Usage - Beatmap Data | Lookup

```python
import oppy
import asyncio
client = oppy.Client()
beatmap = client.beatmap_data
async def main():
    data = await beatmap.lookup(beatmap="big black", token="a long string") #makes the api request using oppy.Client.beatmap_data.lookup()
    print(
    data.id, # Map ID
    data.artist, # Map song artist
    data.mapper, # Map creator
    ) # returns the beatmap id
asyncio.get_event_loop().run_until_complete(main())
```

## Usage - Token

```python
import oppy
import asyncio
client = oppy.Client()
tk = client.gen_token
async def main():
    tkn = await tk.gen(client_secret="string", client_id=0) # makes request using oppy.Client.gen_token.gen()
    print(tkn) # Token
asyncio.get_event_loop().run_until_complete(main())
```

## Support
Feel free to email me at `wayde@alphaxdev.xyz` or contact me on discord support server https://discord.gg/DAPgevH9EX

