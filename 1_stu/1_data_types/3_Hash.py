# coding=utf-8
# date：2022/8/25 10:30

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

"""
Hash 哈希 内部存储为各个键值对
"""

# hset(name, key, value) 哈希中添加一个键值对
#       key存在则修改，key不存在则添加
#       返回值：返回添加成功的个数
# v = redis_conn.hset('Zarten', 'age', 10)
# print(v)

# hmset(name, mapping) 设置哈希中的多个键值对
#       mapping：dict类型
#       返回值：成功True
# v = redis_conn.hmset('Zarten', {'sex': 1, 'tel': '123'})
# print(v)

# hmget(name, keys, *args) 获取哈希中多个键值对
#       返回值：值的列表   形如： [b'1', b'123'] <class 'list'>
# v1 = redis_conn.hmget('Zarten', ['sex', 'tel'])
# v2 = redis_conn.hmget('Zarten', 'sex', 'tel')
# print(v1, v2)

# hget(name, key) 获取指定key的值
# v = redis_conn.hget('Zarten', 'age')
# print(v)

# hgetall(name) 获取哈希中所有的键值对
#       返回值：dict类型
# v = redis_conn.hgetall('Zarten')
# print(v)

# hlen(name) 获取哈希中键值对的个数
# v = redis_conn.hlen('Zarten')
# print(v)

# hkeys(name) 获取哈希中所有的键key
# v = redis_conn.hkeys('Zarten')
# print(v)

# hvals(name) 获取哈希中所有的值value
# v = redis_conn.hvals('Zarten')
# print(v)

# hexists(name, key) 检查哈希中是否有某个键key
#       返回值：有True 没有False
# v = redis_conn.hexists('Zarten', 'bcd')
# print(v)

# hdel(self, name, *keys) 删除哈希中键值对
#       返回值：int删除的个数
# v = redis_conn.hdel('Zarten', 'age')
# print(v)

# hincrby(name, key, amount=1) 自增哈希中key对应的value值  value必须为int类型
# 若所给的key不存在则创建，amount默认增加1，可以为负数
# 返回值：int增加后的数值
# v = redis_conn.hincrby('Zarten', 'sex', -3)
# print(v)

# hincrbyfloat(name, key, amount=1.0) 自增哈希中key对应的value值  value必须为float类型
# 若所给的key不存在则创建，amount默认增加1.0，可以为负数
# 返回值：float增加后的数值
# v1 = redis_conn.hset('Zarten', 'nums', 7.0)
# v2 = redis_conn.hincrbyfloat('Zarten', 'nums', -2.0)
# print(v2)

# expire(name, time) 设置整个键的过期时间
# time：秒，时间一到，立马自动删除
# v1 = redis_conn.hset('Zarten_1', 'nums', 7.0)
# v2 = redis_conn.expire('Zarten_1', 10)
# print(v2)

# hscan(name, cursor=0, match=None, count=None) 增量迭代获取哈希中的数据
#       cursor：游标（基于游标分批取获取数据）
#       match：匹配指定key，默认None 表示所有的key
#       count：每次分片最少获取个数，默认None表示采用Redis的默认分片个数
#       返回值：tuple类型；（扫描位置，所有dict数据）
# v = redis_conn.hscan('Zarten')
# print(v)

# hscan_iter(name, match=None, count=None) 返回hscan的生成器
# v = redis_conn.hscan_iter('Zarten')
# for i in v:
#     print(type(i), i)

