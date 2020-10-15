import redis

# r = redis.Redis("localhost", port=6379)
r = redis.Redis("localhost")        # Default listen all port 6379
v = r.get("name")
print(v)

print(r.set("tadp","microservices"))
print(r.set("count",1))
