from .user import *
from .token import *
from .map import *
from .news import *
from .http import RqToken, Data


class Client:
    def __init__(self):
        self.data_request_client = Data()
        self.token_request_client = RqToken()
        self.gen_token = Token(self.token_request_client)
        self.user_data = UserData(self.data_request_client)
        self.beatmap_data = Beatmap(self.data_request_client)
        self.news_info = OsuNews(self.data_request_client)
