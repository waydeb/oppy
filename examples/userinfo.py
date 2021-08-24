"""
This example allows for basic info about a user using the osu! v2 API
Note; To make use of this you'll need to have a token, you can find out how to make one in gen_token.py
Required args:
user - This is the username or user id of the person you want to lookup. | str
token - The token you made using gen_token.py | str
"""
import oppy
import asyncio

client = oppy.Client()
user = client.user_data


async def main():
    data = await user.user(user="peppy", token="a long string here")
    print(
        data.pp,  # Users PP
        data.username,  # Users username
        data.id,  # Users ID
        data.global_rank,  # Users Global Rank
        data.country_rank,  # Users Country Rank
        data.country_name,  # Users Country Name
    )

asyncio.get_event_loop().run_until_complete(main())