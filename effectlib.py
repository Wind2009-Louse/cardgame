import constant_value
import random
import re

class Card_Effect():
    def __init__(self, target=0, value=0, attr=-1, turn=0, etype=0):
        self.owner = 0

        self.target = target
        self.value = value
        self.attr = attr
        self.turn = turn
        self.etype = etype

    def set(self, etype, epower, target_reverse):
        '''根据给定的数据，生成效果
        
        etype: 该效果的类型
        
        epower: 该效果的power值
        
        target_reverse: 该效果的对象是否反转'''

        self.etype = etype
        self.target = constant_value.card.EFFECT_INFO[etype]["default_target"]

        # 判断是否能在弃置时发动效果
        if not etype & constant_value.card.DROP_FORBIDDEN and random.random() < constant_value.card.DROP_APPEAR:
            self.etype |= constant_value.card.DROP_EFF

        # 判断是否反转对象
        if target_reverse:
            epower = round(epower * 0.8)
            self.target = 1 - self.target
        
        # 判断是否带有属性
        if etype & constant_value.card.ATTR_RELATED:
            self.attr = random.randint(0, constant_value.attribute.ATTR_SIZE-1)
        
        # 判断是否附加状态
        if etype & constant_value.card.STATUS_RELATED:
            status_turn = random.randint(1,3)
            # 修正能力
            value_power = 2 - 0.5 * status_turn
            if self.target == constant_value.card.TARGET_ENEMY:
                status_turn += 1
            self.turn = status_turn
            self.value = round(epower * value_power)
        else:
            self.value = epower
            # 能力削弱
            if etype in [constant_value.card.DISCARD_SELF, constant_value.card.DISCARD_CONFIRM, constant_value.card.DISCARD_RANDOM,
                        constant_value.card.DRAW]:
                self.value = max(1, self.value // 6)
            if etype in [constant_value.card.BANISH_DECK, constant_value.card.BANISH_GRAVE, constant_value.card.BANISH_HAND,
                        constant_value.card.BANISH_SELF]:
                self.value = 1
            if etype in [constant_value.card.ATTACK_IGNORE, constant_value.card.ATTR_ATTACK_APPEND]:
                self.value = max(1, self.value // 3)

    def dict_dump(self):
        '''将数据转化为dict格式'''
        result_dict = self.__dict__.copy()
        result_dict.remove('owner')
        return result_dict
    
    def dict_read(self, dct):
        self.__dict__ = dct
        self.owner = 0
    
    def effect_desp(self):
        '''
        根据给定的效果产生描述
        '''
        # 除去弃置标识
        effect_id = (self.etype | constant_value.card.DROP_EFF) - constant_value.card.DROP_EFF
        # 获取描述
        string = constant_value.card.EFFECT_INFO[effect_id]["desp"]
        for key in self.__dict__:
            if key == "owner":
                continue
            value = self.__dict__[key]
            if key == "target":
                value = "自己" if value == constant_value.card.TARGET_SELF else "对方"
            if key == "attr":
                value = constant_value.attribute.ATTR_NAME[self.attr]
            if type(value) != type("str"):
                value = str(value)
            string = re.sub(r"-%s"%key, r'%s'%value, string)
        if self.etype & constant_value.card.DROP_EFF:
            string = "这张卡被弃置时，" + string
        return string