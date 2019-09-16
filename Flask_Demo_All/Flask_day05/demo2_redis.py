from redis import StrictRedis


def demo():
    sr = StrictRedis(host='172.16.28.143')

    try:
        result = sr.set('name', 'itheima')
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    demo()


# redis-trib.rb create --replicas 1 172.16.28.143:7000 172.16.28.143:7001 172.16.28.143:7002 172.16.28.143:7003 172.16.28.143:7004 172.16.28.143:7005