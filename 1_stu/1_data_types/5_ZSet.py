# coding=utf-8
# date：2022/8/25 10:32

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=4, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

"""
有序集合比集合多了一个分数的字段，可对分数升序降序
"""

# zadd(name, Mapping[_Key, _Score], **kwargs) 有序name集合中,添加元素,添加元素时需指定元素的分数
#       返回值：返回添加的个数
# v = redis_conn.zadd('Zarten', {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'tt': 10, 'gg': 6})
# print(v)

# zcard(name) 返回有序集合中元素个数
# v = redis_conn.zcard('Zarten')
# print(v)

# zcount(name, min, max) 返回有序集合中分数范围内的元素个数 包头包尾
# 返回值：个数int
# v = redis_conn.zcount('Zarten', 3, 5)
# print(v)

# zscore(name, value) 返回有序集合中指定某个值的分数
# 返回值：float 类型的分数；形如： -5.0 <class 'float'>
# v= redis_conn.zscore('Zarten', 'b')
# print(v)

# zincrby(name, Value=value, amount=1) 增加有序集合中某个value值的分数
#       value：若存在，则增加其amount分数；若不存在，则增加新值以及对应的分数
#       amount：增加的值，可以为负数
#       返回值：增加后的分数 float类型 ；形如： -5.0 <class 'float'>
# v = redis_conn.zincrby('Zarten', value='b', amount=-5.0)
# print(v)

# zrem(name, *values) 删除有序集合中的某个或多个值
#       返回值：返回删除的个数
# v = redis_conn.zrem('Zarten', 'b', 'a')
# print(v)

# zremrangebyrank(name, min, max) 根据排名次序, 删除有序集合元素
#       返回值：删除个数int
# v = redis_conn.zremrangebyrank('Zarten', 1, 3)
# print(v)

# zremrangebyscore(name, min, max) 根据分数范围，删除有序集合
#       返回值：删除个数 int
# v = redis_conn.zremrangebyscore('Zarten', 3, 4)
# print(v)

# zrank(name, value) 返回某个值在有序集合中的分数排名（从小到大）
# zrevrank(name, value) 返回某个值在有序集合中的分数排名（从大到小）
#       返回值：value在name中的分数排名值，排名从0开始
# v = redis_conn.zrank('Zarten', 'b')
# print(v)

# zrange(name, start, end, desc=False, withscores=False, score_cast_func=float) 返回有序集合分数排序的一段数据
#       start：有序集合索引起始位置（非分数）,索引从0开始
#       end：有序集合索引结束位置（非分数）,索引从0开始
#       desc：排序规则，默认按照分数从小到大排序
#       withscores：是否获取元素的分数，默认只获取元素的值
#       score_cast_func：对分数进行数据转换的函数
#       返回值：list类型 [(b'tt', 10.0), (b'd', 6.0), (b'c', 5.0)] <class 'list'>
# v = redis_conn.zrange('Zarten', start=0, end=1, desc=False, withscores=True, score_cast_func=float)
# print(v)
