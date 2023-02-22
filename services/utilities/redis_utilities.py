import redis
import uuid
import time

class RedisUtilities:

    def getRedisClient(self, redis_host, redis_port, redis_db, logger):
        try:
            redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
            return redis_client
        except:
            logger.critical(f"Cannot connect to the redis server: {redis_host}")

    def getRedisLock(self, redis_client, lock_key, expiration_time):
        lock_value = str(uuid.uuid4())
        i = 1
        while not redis_client.setnx(lock_key, lock_value):
            time.sleep(0.05)
            if redis_client.ttl(lock_key) == -1:
                redis_client.delete(lock_key)
                lock_value = str(uuid.uuid4())
            print("connot get lock", i)
            i += 1
        
        redis_client.expire(lock_key, expiration_time)
                
