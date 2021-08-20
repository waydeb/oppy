import oppy.http


class Token:
    def __init__(self, token_request_client):
        self.token_request_client = token_request_client

    async def gen(self, client_id, client_secret):
        return await self.token_request_client.gen(client_id=client_id, client_secret=client_secret)
