from .newsinfo import News
from datetime import datetime, timezone
from typing import Union, List, Dict, Tuple


class OsuNews:

    def __init__(self):
        self.data_request_client = data_request_client

    async def recent(self) -> News:

        data = await self.data_request_client.request(endpoint="news")["news_posts"][0]
        id=data.get("id")
        author=data.get("author")
        edit_url=data.get("edit_url")
        first_image=data.get("first_image")
        first_published=data.get("published_at")
        last_edited=data.get("updated_at")
        slug=data.get("slug")
        title=data.get("title")
        preview=data.get("preview")

        return News(
            id,
            author,
            edit_url,
            first_image,
            first_published,
            last_edited,
            slug,
            title,
            preview,
        )

    async def last(self) -> News:
        data = await self.data_request_client.request(endpoint="news")["news_posts"][1]

        id=data.get("id")
        author=data.get("author")
        edit_url=data.get("edit_url")
        first_image=data.get("first_image")
        first_published=data.get("published_at")
        last_edited=data.get("updated_at")
        slug=data.get("slug")
        title=data.get("title")
        preview=data.get("preview")

        return News(
            id,
            author,
            edit_url,
            first_image,
            first_published,
            last_edited,
            slug,
            title,
            preview,
        )

    async def any(self, post) -> News:
        data = await self.data_request_client.request(endpoint="news")["news_posts"][post]

        id=data.get("id")
        author=data.get("author")
        edit_url=data.get("edit_url")
        first_image=data.get("first_image")
        first_published=data.get("published_at")
        last_edited=data.get("updated_at")
        slug=data.get("slug")
        title=data.get("title")
        preview=data.get("preview")

        return News(
            id,
            author,
            edit_url,
            first_image,
            first_published,
            last_edited,
            slug,
            title,
            preview,
        )
