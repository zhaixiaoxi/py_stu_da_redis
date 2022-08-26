# coding=utf-8
# date：2022/8/25 10:31

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

"""
集合中的元素不重复，一般用于过滤元素
"""

# sadd(name, *values) 添加元素到集合中
#       若插入已有的元素，则自动不插入
#       返回值：返回添加成功的个数
# v = redis_conn.sadd('Zarten', 'apple', 'a', 'b', 'c')
# print(v)

# scard(name) 返回集合中元素的个数
# v = redis_conn.scard('Zarten')
# print(v)

# smembers(name) 获取集合中的所有元素
#       返回值：set类型， 形如：{b'a', b'apple', b'c', b'b'}
# v = redis_conn.smembers('Zarten')
# print(v)

# srandmember(name, number=None) 随机获取一个或N个元素
#       name：键名
#       number：一个或N个，默认返回一个。若返回N个，则返回List类型
#       返回值：返回一个值或一个列表
# v = redis_conn.srandmember('Zarten', 2)
# print(v)

# sismember(name, value) 判断某个值是否在集合中
#       返回值：在True,  不在False
# v = redis_conn.sismember('Zarten', 'appl')
# print(v)

# spop(name) 随机删除并返回集合中的元素
# v = redis_conn.spop('Zarten')
# print(v)

# srem(name, *values) 删除集合中的一个或多个元素
# 返回值：返回删除的个数int
# v = redis_conn.srem('Zarten', 'c', 'a')
# print(v)

# smove(src, dst, value) 将src集合中的一个value值，移动到dst集合中
#       若value不存在时，返回False
#       返回值：成功True
# v = redis_conn.smove('Zarten', 'Fruit', 'apple')
# print(v)

# sdiff(keys, *args) 返回在keys集合中,但不在其他集合的所有元素（差集）
#       返回值：set类型 {b'2', b'4', b'3', b'1'}
# v = redis_conn.sdiff('Fruit', 'Zarten')
# print(v)

# sdiffstore(dest, keys, *args) 在keys集合中，不在其他集合中的元素保存在dest集合中 即上面的sdiff的返回值（差集）保存在dest集合中
#       dest：新的集合，设置的新集合，旧集合会被覆盖
#       返回值：int 返回作用的个数
# v = redis_conn.sdiffstore('Left', 'Fruit', 'Zarten')
# print(v)

# sinter(keys, *args) 返回一个集合与其他集合的交集
#       返回值：set类型
# v = redis_conn.sinter('Left', 'Fruit')
# print(v)

# sinterstore(dest, keys, *args) 返回keys集合与其他集合的交集，并保存在dest集合中
#       dest：另一个集合，设置新集合，旧集合元素会被覆盖
#       返回值：int返回作用的个数
# v = redis_conn.sinterstore('Right', 'Left', 'Fruit')
# print(v)

# sunion(keys, *args) 返回一个集合与其他集合的并集
# v = redis_conn.sunion('Right', 'Left')
# print(v)

# sunionstore(dest, keys, *args) 返回keys集合与其他集合的并集，并保存在dest集合中
#       dest：另一个集合，设置新集合，旧集合元素会被覆盖
#       返回值：int新集合元素个数
# v = redis_conn.sunionstore('Union', 'Zarten', 'Fruit')
# print(v)
