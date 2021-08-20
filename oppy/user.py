from .userstats import User, UserBm
from datetime import datetime, timezone
from typing import Union, List, Dict, Tuple


class UserData:

    def __init__(self, data_request_client):
        self.data_request_client = data_request_client

    async def user(self, user, token) -> User:
        data = await self.data_request_client.request(endpoint=f"users/{user}", token=token)
        country_code = data.get("country_code")
        country_name = data.get("country")["name"]
        cover_url = data.get("cover_url")
        discord = data.get("discord")
        id = data.get("id")
        interests = data.get("interests")
        followers = data.get("follower_count")
        location = data.get("location")
        me_html = data.get("page")["html"]
        me_raw = data.get("page")["raw"]
        main_mode = data.get("playmode")
        playstyle = data.get("playstyle")
        names = data.get("previous_usernames")
        rank_history = data.get("rankHistory")["data"]
        global_rank = data.get("statistics")["global_rank"]
        country_rank = data.get("statistics")["country_rank"]
        pp = data.get("statistics")["pp"]
        accuracy = data.get("hit_accuracy")
        avatar = data.get("avatar_url")
        comment_count = data.get("comments_count")
        user_group = data.get("default_groups")
        user_groups = data.get("groups")
        dm_friends_only = data.get("pm_friends_only")
        profile_order = data.get("profile_order")
        ranked_and_approved_beatmaps = data.get("ranked_and_approved_beatmapset_count")
        grade_a = data.get("statistics")["grade_counts"]["a"]
        grade_s = data.get("statistics")["grade_counts"]["s"]
        grade_sh = data.get("statistics")["grade_counts"]["sh"]
        grade_ss = data.get("statistics")["grade_counts"]["ss"]
        grade_ssh = data.get("statistics")["grade_counts"]["ssh"]
        max_combo = data.get("statistics")["maximum_combo"]
        ranked_score = data.get("statistics")["ranked_score"]
        total_score = data.get("statistics")["total_score"]
        total_hits = data.get("statistics")["total_hits"]
        twitter = data.get("twitter")
        profile_title = data.get("title")
        profile_title_url = data.get("title_url")  # wtf are these lmao
        username = data.get("username")
        website = data.get("website")
        return User(
            country_code,  # Country Code
            country_name,  # Country Code
            cover_url,  # Profile Banner URL
            discord,  # Discord account
            id,  # User ID
            interests,  # User Interests
            followers,  # Follwers
            location,  # User Location
            me_html,  # me! page in HTML
            me_raw,  # me! page in raw bb code
            main_mode,  # Main osu! game mode
            playstyle,  # User Playstyle
            names,  # Names
            rank_history,  # Rank Histroy for the past 90 days
            global_rank,  # Current Global Rank
            country_rank,  # Current Country Rank
            pp,  # User raw PP
            accuracy,  # User accuracy
            avatar,  # Avatar URL
            comment_count,  # Comment count on the forms
            user_group,  # Main User Group (eg. gmt)
            user_groups,  # All user groups they're in (eg. gmt, alm, bm)
            dm_friends_only,  # DM only from friends
            profile_order,  # User Profile layout
            ranked_and_approved_beatmaps,  # How many ranked + approved beatmaps does the user have
            grade_a,  # A
            grade_s,  # S
            grade_sh,  # S Hidden
            grade_ss,  # SS
            grade_ssh,  # SS Hidden
            max_combo,  # Max combo all time
            ranked_score,  # Ranked score
            total_score,  # Total score
            total_hits,  # Total hits all time
            twitter,  # User Twitter
            profile_title,  # ?
            profile_title_url,  # ?
            username,  # Current Username
            website,  # Website
        )

    async def userbeatmaps(self, user, token) -> UserBm:
        data = await self.data_request_client.request(endpoint=f"users/{user}", token=token)
        return UserBm(
            title,
            status,
        )
