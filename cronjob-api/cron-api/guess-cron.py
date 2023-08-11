import redis
import random as rd

r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

if __name__ == "__main__":
    rn = rd.randrange(50)
    r.set("rn", rn)
