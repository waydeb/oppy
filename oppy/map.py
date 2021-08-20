from .mapstats import *
from datetime import datetime, timezone
from typing import Union, List, Dict, Tuple


class Beatmap:
    def __init__(self, data_request_client):
        self.data_request_client = data_request_client

    async def lookup(self, token, beatmap) -> BeatmapStats:

        data = await self.data_request_client.request(endpoint=f'beatmapsets/search/{beatmap}', token=token)
        return BeatmapStats(
            id,
            author,
            artist,
            artist_unicode,
            title,
            title_unicode,
            bpm,
            date_uploaded,
            date_ranked,
            date_approved,
            date_loved,
            date_updated,
            cover_url,
            discussion,
            length,
            diffs,
            star_rating,
        )

    async def scores(self, token, beatmap) -> BeatmapScores:
        endpoint = f'https://osu.ppy.sh/api/v2/beatmaps/{beatmap}/scores'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'}
        data = await self.data_request_client.request(endpoint=endpoint, headers=headers)
        return BeatmapScores(
            first,
            top5,
            top10,
            id,
        )
