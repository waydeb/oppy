"""
This example allows you to exchange your Client ID and Client Secret for an access token
The access token will allow you to access pretty much any other part of the osu! API.
Required args:
client_id - Your Client ID | int
client_secret - Your Client Secret | str
"""
import oppy
import asyncio

client = oppy.Client()
token = client.gen_token


async def main():
    data = await token.gen(client_id=1, client_secret="abc1234")
    print(data)

asyncio.get_event_loop().run_until_complete(main())
