# coding=utf-8
# date：2022/8/26 17:30

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

"""
全局函数对任何数据结构都适用
"""

# delete(*names) 删除redis中一个或多个键的所有数据
#       返回值：int删除的个数
# v = redis_conn.delete('name_1')
# print(v)

# exists(name) 判断redis中是否存在某个键
#       返回值：存在True； 不存在False
# v = redis_conn.exists('name')
# print(v)

# rename(src, dst) 对键 重命名
#       返回值：成功True
# v = redis_conn.rename('name_2', 'name_new')
# print(v)

# move(name, db) 移动redis中某个键的所有数据到某个db中
# 返回值：成功True
# v = redis_conn.move('name_new', 6)
# print(v)

# randomkey() 随机获取redis中某个键名
# v = redis_conn.randomkey()
# print(v)

# type(name) 查看redis中某个键数据结构类型
# 返回值：none (key不存在)
#        string (字符串)
#        list (列表)
#        set (集合)
#        zset (有序集)
#        hash (哈希表)
# v = redis_conn.type('num_2')
# print(v)
