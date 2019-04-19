import constant_value
import cardlib
import randomlib

if __name__ == "__main__":
    with open("cardtexts.csv","w") as f:
        f.write("卡名,效果\n")
        for i in range(1000):
            maked_card = cardlib.make_card(15, attack_guarantee=(i%10==0))
            f.write(maked_card.name()+','+maked_card.effect_desp()+"\n")
    print("输出卡名测试文件。")