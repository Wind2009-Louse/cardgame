import random

def random_from_dict(dct):
    '''
    根据给定的dict，随机返回其中一个key，其随机权重由value决定
    '''
    total_sum = sum(dct.values())
    type_rand = random.randint(0,total_sum-1)
    for result_name, result_poss in dct.items():
        if type_rand < result_poss:
            return result_name
        else:
            type_rand -= result_poss
    return ""

def normalize_random(under, upper):
    '''
    根据给定的范围，生成一个符合正态分布的随机数
    '''
    mu = (upper + under + 1) / 2
    sigma = (upper + 1 - under) / 8
    random_num = min(max(round(random.normalvariate(mu, sigma)), under), upper)
    return random_num