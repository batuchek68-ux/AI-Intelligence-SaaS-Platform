import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def set_cache(key, value):
    r.set(key, value, ex=3600)

def get_cache(key):
    return r.get(key)
