class BeatmapStats:
    def __init__(self, id, author, artist, artist_unicode, title, title_unicode, bpm, date_uploaded, date_ranked,
                 date_approved, date_loved, date_updated, cover_url, discussion, length, diffs, star_rating):
        self.id = id
        self.author = author
        self.artist = artist
        self.artist_unicode = artist_unicode
        self.title = title
        self.title_unicode = title_unicode
        self.bpm = bpm
        self.date_uploaded = date_uploaded
        self.date_ranked = date_ranked
        self.date_approved = date_approved
        self.date_loved = date_loved
        self.date_updated = date_updated
        self.cover_url = cover_url
        self.discussion = discussion
        self.length = length
        self.diffs = diffs  # ?
        self.star_rating = star_rating


class BeatmapScores:
    def __init__(self, first, top5, top10, id):
        self.first = first
        self.top5 = top5
        self.top10 = top10
        self.id = id
