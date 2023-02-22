import time
import uuid
import redis
from redis_utilities import RedisUtilities

lock_key = 'mylock'
expiration_time = 50  # in seconds

redUtil = RedisUtilities()

redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")

redUtil.getRedisLock(redis_client, lock_key, expiration_time)

print(redis_client.get("rxh82f6"))

time.sleep(50)


# release the lock
redis_client.delete(lock_key)





