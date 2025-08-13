import random

from .random import Random
from .recommender import Recommender


class Indexed(Recommender):
    def __init__(self, tracks_redis, recommendations_redis, catalog):
        self.random = Random(tracks_redis)
        self.recommendations_redis = recommendations_redis
        self.catalog = catalog

    def recommend_next(self, user: int, prev_track: int, prev_track_time: float) -> int:
        recommendations = self.recommendations_redis.get(user)
        if recommendations:
            shuffled = list(self.catalog.from_bytes(recommendations))
            random.shuffle(shuffled)
            return shuffled[0]
        return self.random.recommend_next(user, prev_track, prev_track_time)