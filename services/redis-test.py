import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

import time
import uuid
import redis
from redis_utilities import RedisUtilities

lock_key = 'grpc-lock'
expiration_time = 50  # in seconds

redUtil = RedisUtilities()

redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")

redUtil.getRedisLock(redis_client, lock_key, expiration_time)

print(redis_client.get('jdjdjd'))

redis_client.delete(lock_key)





