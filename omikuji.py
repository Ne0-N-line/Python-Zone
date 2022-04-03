import random
omikuji = random.randint(1,10) # 1から10の数値をランダムに生成
#print(omikuji)

if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji <= 4: # 3,4
    print("小吉")
elif omikuji <= 7: # 5,6,7
    print("凶")
else:              # 8,9,10
    print("大凶")