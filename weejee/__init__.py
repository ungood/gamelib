import boardgamegeek as bgg

# Cache BGG requests for 15 minutes
cache = bgg.CacheBackendSqlite('cache.db', ttl=15 * 60)
client = bgg.BGGClient(cache=cache)