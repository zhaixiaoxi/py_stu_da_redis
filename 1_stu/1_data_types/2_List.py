# coding=utf-8
# date：2022/8/25 10:30

import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1, decode_responses=True)
redis_conn = redis.Redis(connection_pool=redis_pool)

# lpush(name, *values) 列表左边添加值 多个value值时，从左到右依次向列表左边添加，类型可以不同
# rpush(name, *values) 列表右边添加值
#       键不存在时，新建一个列表
#       返回值：列表的大小
# v = redis_conn.lpush('Zarten', 1, 2, 3, 4, 5)
# print(v)

# lpushx(name, value) 键存在时，添加到列表左边
# rpushx(name, value) 键存在时，添加到列表右边
#       只有键存在时才添加 若键不存在则不添加，也不新创建列表
#       返回值为：列表大小
# v1 = redis_conn.lpush('Zarten_1', 1, 2, 3, 4, 5)
# v = redis_conn.lpushx('Zarten_1', 'hehe')
# print(v)

# llen(name) 获取所给键的列表长度
# v = redis_conn.llen('Zarten')
# print(v)

# lset(name, index, value) 列表中通过索引赋值, 索引从0开始
#       返回值：成功True 失败False
# v = redis_conn.lset('Zarten', 2, 'cc')
# print(v)

# linsert(name, where, refvalue, value) 在列表中间插入新值
#       name：键名
#       where：位置，前面BEFORE 后面AFTER
#       refvalue：指定哪个值的前后插入
#       value：插入的新值
#       返回值：插入后列表的长度，若返回-1，则refvalue不存在
# 插入前的数据：5 4 3 2 1
# 插入后的数据:5 4 before3 3 2 1
# v = redis_conn.linsert('Zarten', 'BEFORE', 1, 'before1')
# print(v)

# lindex(name, index) 通过索引获取列表值
# v = redis_conn.lindex('Zarten', 2)
# print(v)

# lrange(name, start, end) 列表中获取一段数据 包头包尾
#       返回值：List类型的一段数据
# v = redis_conn.lrange('Zarten', 2, 5)
# print(v)

# lpop(name) 删除左边的第一个值
# rpop(name) 删除右边的第一个值
#       返回值：被删除元素的值
# v = redis_conn.lpop('Zarten')
# print(v)

# blpop(keys, timeout=0) 删除并返回列表最左边的值
# brpop(keys, timeout=0) 删除并返回列表最右边的值
#       keys：给定的键
#       timeout：等待超时时间，默认为0，表示一直等待
#       返回值：tuple类型    (键名, 删除的值) (b'Zarten', b'hehe')
# v = redis_conn.blpop('Zarten', timeout=0)
# print(v)

# lrem(name, count, value) 删除列表中N个相同的值
#       name：键名
#       count：删除的个数 整数表示从左往右 负数表示从右往左 例如：2 -2
#       value：需删除的值
#       返回值：返回删除的个数
# v = redis_conn.lrem('Zarten_1', count=2, value='hehe')
# print(v)

# ltrim(name, start, end) 删除列表中范围之外的所有值 索引从0开始
#       返回值：成功True 失败False
# v = redis_conn.ltrim('Zarten_1', 3, 4)
# print(v)

# rpoplpush(src, dst) src列表中最右边值取出后 添加到dst列表的最左边
# brpoplpush(src, dst, timeout=0)为rpoplpush的阻塞版本，timeout为0时，永远阻塞
#       返回值：取出的元素值
# v = redis_conn.rpoplpush('Zarten', 'Zarten_1')
# print(v)
