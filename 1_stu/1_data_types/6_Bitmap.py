# coding=utf-8
# date：2022/8/25 10:32

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=5, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

"""
bitmap中存放二进制的位0和1，类似位数组。
典型应用是基于redis的布隆过滤器。
属于String字符串数据结构，故bit映射被限制在 512 MB 之内（2^32）
"""

# setbit(name, offset, value) 设置位图的值
#       name：redis键名
#       offset：偏移量，大于等于0。当偏移伸展时，空白位置以0填充
#       value：二进制值 0或1
# v = redis_conn.setbit('Zarten_2', 110, 1)
# print(v)

# getbit(name, offset) 返回位图指定偏移量的值
#       返回值：0或1
# v = redis_conn.getbit('Zarten_2', 100)
# print(v)

# bitcount(key, start=None, end=None) 返回位图中二进制为1的总个数
#       start end指定开始和结束的位，默认整个位图
# v = redis_conn.bitcount('Zarten_2', 10, 1000)
# print(v)

