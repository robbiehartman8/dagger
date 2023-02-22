import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

import redis
from redis_utilities import RedisUtilities


redUtil = RedisUtilities()

redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")

redis_client.flushdb()





