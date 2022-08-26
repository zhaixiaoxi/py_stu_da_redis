# coding=utf-8
# date：2022/8/25 10:26

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

# set(name, value, ex=None, px=None, nx=False, xx=False) 设置单个键值
#       ex：过期时间（秒），时间到了后redis会自动删除
#       px：过期时间（毫秒），时间到了后redis会自动删除。ex、px二选一即可
#       nx：如果设置为True，则只有name不存在时，当前set操作才执行
#       xx：如果设置为True，则只有name存在时，当前set操作才执行
# redis_conn.set('name_1', 'Marten_1', ex=None)
# redis_conn.set('name_2', 'Marten_2', ex=None)

# get 获取单个值
# v = redis_conn.get('name_2')
# print(v)

# mset 设置多个键值
# name_dict = {
#     'name_3': 'Marten_3',
#     'name_4': 'Marten_4'
# }
# redis_conn.mset(name_dict)

# mget 获取多个值
# m = redis_conn.mget('name_1', 'name_2')
# print(m)

# getset 给已有的键设置新值，并返回原有的值 当所给的键不存在时，会设置其新值，但返回值为None
# v = redis_conn.getset('name_1', 'hi')
# print(v)

# setrange(name, offset, value) 根据索引修改某个键的value值
#       返回值为：修改后的字符串长度
#       name：键，所给不存在时自动添加
#       offset：偏移量，以0开始
#       value：修改的字符或字符串，字符串时以offset向后顺延
# length = redis_conn.setrange('name_2', 1, 'zhihu')
# print(length)

# getrange(key, start, end) 根据索引获取某个键的部分value值 包头包尾 若所给的键不存在时，返回空值 b''
# v = redis_conn.getrange('name_4', 0, 2)
# print(v)

# strlen(name) 获取value的长度 所给的键不存在时，返回值为0
# length = redis_conn.strlen('name_2')
# print(length)
# length = redis_conn.strlen('name_8')
# print(length)

# incr(name, amount=1) 整数值自增 默认自增1 返回值:修改后的int类型值
# decr(name, amount=1) 整数值自减 默认自增1 返回值:修改后的int类型值
# redis_conn.set('num_2', 2)
# v = redis_conn.incr('num_2', amount=2)
# print(v)

# incrbyfloat(name, amount=1.0) 浮点数值自增 返回值：修改后的float浮点数类型
# v = redis_conn.incrbyfloat('num_2', amount=3.0)
# print(v)

# append(key, value) 后面追加value值
#       若键不存在，则设置新值
#       返回值:修改后的值长度
# length = redis_conn.append('name_5', 'append777')
# print(length)
