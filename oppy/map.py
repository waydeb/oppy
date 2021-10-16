from .mapstats import *
from datetime import datetime, timezone
from typing import Union, List, Dict, Tuple


class Beatmap:
    def __init__(self, data_request_client):
        self.data_request_client = data_request_client

    async def map(self, token, beatmap) -> BeatmapStats:

        data = await self.data_request_client.request(endpoint=f'beatmapsets/{beatmap}', token=token)
        return data