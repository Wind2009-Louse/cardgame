# 基本属性，用与运算抹除
BASE_TYPE = 127
# 与属性相关
ATTR_RELATED = 128
# 与状态相关
STATUS_RELATED = 256
# 被弃置时相关
DROP_EFF = 512
# 被弃置时不能适用的效果
DROP_FORBIDDEN = 1024
# 效果被附加上弃置效果的概率
DROP_APPEAR = 0.1
# 随机相关
RANDOMLY_EFF = 2048
# 无法被逆转
REVERSELESS = 4096
# 效果被逆转的概率
REVERSE_APPEAR = 0.05
# 一张卡上最多拥有的效果
MAX_EFFECT_COUNT = 4

# 普通攻击
ATTACK = 1
# 无视防御伤害
ATTACK_IGNORE = 2
# 属性伤害
ATTR_ATTACK = 3 | ATTR_RELATED
# 属性特攻
ATTR_ATTACK_APPEND = 4 | ATTR_RELATED
# 攻击力上升状态
ATTACK_UP = 5 | STATUS_RELATED
# 攻击力下降状态
ATTACK_DOWN = 6 | STATUS_RELATED
# 属性攻击力上升状态
ATTR_ATTACK_UP = 7 | ATTR_RELATED | STATUS_RELATED
# 属性攻击力下降状态
ATTR_ATTACK_DOWN = 8 | ATTR_RELATED | STATUS_RELATED
# 防御力上升状态
DEF_UP = 9 | STATUS_RELATED
# 防御力下降状态
DEF_DOWN = 10 | STATUS_RELATED
# 属性防御力上升状态
ATTR_DEF_UP = 11 | ATTR_RELATED | STATUS_RELATED
# 属性防御力下降状态
ATTR_DEF_DOWN = 12 | ATTR_RELATED | STATUS_RELATED

# 生命恢复
HP_HEAL = 13
# 生命自动恢复
HP_AUTOHEAL = 14 | STATUS_RELATED

# 抽卡
DRAW = 15
# 随机弃置手卡
DISCARD_RANDOM = 16 | RANDOMLY_EFF
# 确认手卡并由对方弃置手卡
DISCARD_CONFIRM = 17
# 自己弃置卡片
DISCARD_SELF = 18

# 驱逐自身
BANISH_SELF = 19 | DROP_FORBIDDEN | REVERSELESS
# 驱逐手卡
BANISH_HAND = 20
# 驱逐弃置区
BANISH_GRAVE = 21
# 驱逐卡组（随机）
BANISH_DECK = 22

# 额外出牌机会
EXTRA_CHANCE = 23 | REVERSELESS

TARGET_SELF = 0
TARGET_ENEMY = 1

ATTACK_EFFECT = {
    ATTACK: 50,
    ATTACK_IGNORE: 5,
    ATTR_ATTACK: 30,
    ATTR_ATTACK_APPEND: 5
}

'''
卡片效果说明
可选内容：-target, -value, -attr, -turn
效果内容：
name: 效果的名称
desp: 效果的描述
base_power: 效果的基本power
default_target: 效果默认的对象(0:自己, 1:对方)
power_addition_range: 效果的附加power值范围
random_type: 附加power值范围的随机方式(Normalize: 正态分布; Random: 随机分布)
'''
EFFECT_INFO = {
    ATTACK:{
        "name":["攻击",10],
        "desp":"对-target造成-value点伤害。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTACK_IGNORE:{
        "name": ["破击",10],
        "desp":"对-target造成-value点无视防御伤害。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_ATTACK:{
        "name":["-attr击",10],
        "desp":"对-target造成-value点-attr属性伤害。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_ATTACK_APPEND:{
        "name":["-attr暴击",10],
        "desp":"对-target造成-value点-attr属性暴击。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTACK_UP:{
        "name":["力量",5],
        "desp":"-target的攻击力在-turn回合内上升-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTACK_DOWN:{
        "name":["虚弱",5],
        "desp":"-target的攻击力在-turn回合内下降-value点。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    DEF_UP:{
        "name":["专注",5],
        "desp":"-target的防御力在-turn回合内上升-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    DEF_DOWN:{
        "name":["弱点",5],
        "desp":"-target的防御力在-turn回合内下降-value点。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_ATTACK_UP:{
        "name":["-attr力量",5],
        "desp":"-target的-attr属性攻击力在-turn回合内上升-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_ATTACK_DOWN:{
        "name":["-attr虚弱",5],
        "desp":"-target的-attr属性攻击力在-turn回合内下降-value点。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_DEF_UP:{
        "name":["-attr专注",5],
        "desp":"-target的-attr属性防御力在-turn回合内上升-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    ATTR_DEF_DOWN:{
        "name":["-attr弱点",5],
        "desp":"-target的-attr属性防御力在-turn回合内下降-value点。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },

    HP_HEAL:{
        "name":["回复",5],
        "desp":"-target的生命值回复-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },
    HP_AUTOHEAL:{
        "name":["恢复",5],
        "desp":"-target的生命值在-turn回合内回复-value点。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,999],
        "random_type":"Normalize"
    },

    DRAW:{
        "name":["贪欲",5],
        "desp":"-target从牌堆抽-value张牌。",
        "base_power":5,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,7],
        "random_type":"Random"
    },
    DISCARD_RANDOM:{
        "name":["手牌破坏",5],
        "desp":"-target随机弃置-value张手牌。",
        "base_power":5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },
    DISCARD_CONFIRM:{
        "name":["心灵透视",5],
        "desp":"确认-target手卡并弃置-value张手牌。",
        "base_power":8,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },
    DISCARD_SELF:{
        "name":["自我破坏",5],
        "desp":"-target自身弃置-value张手牌。",
        "base_power":-5,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },

    BANISH_SELF:{
        "name":["销毁",5],
        "desp":"这张卡使用后被驱逐。",
        "base_power":-10,
        "default_target":TARGET_SELF,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },
    BANISH_HAND:{
        "name":["手牌销毁",5],
        "desp":"驱逐-target的-value张手牌。",
        "base_power":15,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },
    BANISH_GRAVE:{
        "name":["弃置销毁",5],
        "desp":"驱逐-target的-value张弃置区的牌。",
        "base_power":10,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },
    BANISH_DECK:{
        "name":["牌堆销毁",5],
        "desp":"驱逐-target的-value张牌堆的牌。",
        "base_power":10,
        "default_target":TARGET_ENEMY,
        "power_addition_range":[0,0],
        "random_type":"Random"
    },

    EXTRA_CHANCE:{
        "name":["机会",5],
        "desp":"出牌阶段增加一次出牌机会。",
        "base_power":10,
        "default_target":0,
        "power_addition_range":[0,0],
        "random_type":"Random"
    }
}

# 不同种类效果的出现概率
APPEAR_CHANCE = {
    ATTACK: 100,
    ATTACK_IGNORE: 10,
    ATTR_ATTACK: 50,
    ATTR_ATTACK_APPEND: 10,
    ATTACK_UP: 30,
    ATTACK_DOWN: 30,
    DEF_UP: 30,
    DEF_DOWN: 30,
    ATTR_ATTACK_UP: 30,
    ATTR_ATTACK_DOWN: 30,
    ATTR_DEF_UP: 30,
    ATTR_DEF_DOWN: 30,

    HP_HEAL: 30,
    HP_AUTOHEAL: 30,

    DRAW: 30,
    DISCARD_RANDOM: 30,
    DISCARD_CONFIRM: 30,
    DISCARD_SELF: 30,

    BANISH_SELF: 30,
    BANISH_HAND: 30,
    BANISH_GRAVE: 30,
    BANISH_DECK: 30,

    EXTRA_CHANCE: 50
}