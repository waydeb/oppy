class User:
    def __init__(self, country_code, country_name, cover_url, discord, id, interests, followers,
                 location, me_html, me_raw, main_mode, playstyle, names, rank_history, global_rank,
                 country_rank, pp, accuracy, avatar, comment_count, user_group, user_groups,
                 dm_friends_only, profile_order, ranked_and_approved_beatmaps,
                 grade_a, grade_s, grade_sh, grade_ss, grade_ssh, max_combo, ranked_score,
                 total_score, total_hits, twitter, profile_title, profile_title_url, username, website):
        self.country_code = country_code
        self.country_name = country_name
        self.cover_url = cover_url
        self.discord = discord
        self.id = id
        self.interests = interests
        self.followers = followers
        self.location = location
        self.me_html = me_html
        self.me_raw = me_raw
        self.main_mode = main_mode
        self.playstyle = playstyle
        self.names = names
        self.rank_histroy = rank_history
        self.global_rank = global_rank
        self.country_rank = country_rank
        self.pp = pp
        self.accuracy = accuracy
        self.avatar = avatar
        self.comment_count = comment_count
        self.user_group = user_group
        self.user_groups = user_groups
        self.dm_friends_only = dm_friends_only
        self.profile_order = profile_order
        self.ranked_and_approved_beatmaps = ranked_and_approved_beatmaps
        self.grade_a = grade_a
        self.grade_s = grade_s
        self.grade_sh = grade_sh
        self.grade_ss = grade_ss
        self.grade_ssh = grade_ssh
        self.max_combo = max_combo
        self.ranked_score = ranked_score
        self.total_score = total_score
        self.total_hits = total_hits
        self.twitter = twitter
        self.profile_title = profile_title
        self.profile_title_url = profile_title_url
        self.username = username
        self.website = website


class UserBm:
    def __init__(self, approved_beatmaps):
        self.approved_beatmaps = approved_beatmaps
