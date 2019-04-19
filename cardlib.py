import constant_value
import randomlib
import effectlib
import re

class Card():
    def __init__(self, owner=0):
        self.uuid = 0
        self.visible = False
        self.owner = owner
        self.effect = []
    def effect_desp(self):
        result = ""
        for eff in self.effect:
            result += eff.effect_desp()
        return result
    def name(self):
        if len(self.effect) == 0:
            return "未知卡片"
        else:
            names = []
            for effect in self.effect:
                effect_type = effect.etype
                # 洗除附加效果
                for extra_append in [constant_value.card.DROP_EFF]:
                    effect_type -= (effect.etype & extra_append)
                effect_name = constant_value.card.EFFECT_INFO[effect_type]["name"].copy()
                effect_attr = constant_value.attribute.ATTR_NAME[effect.attr]
                effect_name[0] = re.sub(r"-attr", r"%s"%effect_attr, effect_name[0])
                names.append(effect_name)
            # 根据权重排序
            names.sort(key=lambda x: x[1])
            return "·".join([n[0] for n in names])

def make_desp(card):
    '''
    根据输入的卡片生成效果文本

    输入的card应可以通过 card["effect"]读取到效果的list。
    '''
    if "visible" in card and card["visible"] == False:
        return ""
    if "effect" not in card:
        return ""
    else:
        effects = []
        for effect in card["effect"]:
            effect_type = effect["type"]
            effects.append(constant_value.card.EFFECT_INFO[effect_type]["name"])
        # 根据权重排序
        effects.sort(key=lambda x: x[1])
        return "\n".join([eff[0] for eff in effects])

def make_card(power, attack_guarantee=False):
    '''
    根据给定的power值生成卡片

    若attack_guarantee为True，则至少包含一个攻击效果
    '''
    original_power = power
    while(True):
        # 生成错误三次即重新生成
        retry = 3
        effect_list = {}
        while(retry and power and len(effect_list) < constant_value.card.MAX_EFFECT_COUNT):
            # 获得效果
            new_effect = None
            while(True):
                if attack_guarantee and len(effect_list) == 0:
                    new_effect = randomlib.random_from_dict(constant_value.card.ATTACK_EFFECT)
                else:
                    new_effect = randomlib.random_from_dict(constant_value.card.APPEAR_CHANCE)
                if new_effect in effect_list.keys():
                    continue
                break
            # 获取基本强度
            base_power = constant_value.card.EFFECT_INFO[new_effect]["base_power"]
            # 过强
            if base_power > power:
                # 判断能否将剩余数值赋予给其它属性
                remain_effect = list(effect_list.keys())
                add_effect = remain_effect[randomlib.random.randint(0, len(remain_effect)-1)]
                new_effect_power = power + effect_list[add_effect][0] - constant_value.card.EFFECT_INFO[add_effect]["base_power"]
                if power+effect_list[add_effect][0] <= constant_value.card.EFFECT_INFO[add_effect]["power_addition_range"][1] \
                    and not effect_list[add_effect][1]:
                    effect_list[add_effect][0] = new_effect_power + constant_value.card.EFFECT_INFO[add_effect]["base_power"]
                    power = 0
                    break
                else:
                    retry -= 1
                    continue
            # 获取随机数值
            under = constant_value.card.EFFECT_INFO[new_effect]["power_addition_range"][0]
            upper = min(constant_value.card.EFFECT_INFO[new_effect]["power_addition_range"][1], power - base_power)
            random_type = constant_value.card.EFFECT_INFO[new_effect]["random_type"]
            if random_type == "Normalize":
                random_power = base_power + randomlib.normalize_random(under, upper)
            else:
                random_power = base_power + randomlib.random.randint(under, upper)

            reverse_value = False
            # 判断是否为惩罚属性
            if not new_effect & constant_value.card.REVERSELESS and randomlib.random.random() < constant_value.card.REVERSE_APPEAR:
                reverse_value = True
            power -= random_power * (-1 if reverse_value else 1)

            effect_list[new_effect] = [random_power, reverse_value]
        # 判断是否生成完毕
        if power != 0:
            power = original_power
            continue
        else:
            break
    new_card = Card()
    for eff_type in effect_list.keys():
        new_eff = effectlib.Card_Effect()
        new_eff.set(eff_type, effect_list[eff_type][0], effect_list[eff_type][1])
        new_card.effect.append(new_eff)
    return new_card