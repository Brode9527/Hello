import random
start = int(input('請輸入數字範圍起始值：'))
end = int(input('請輸入結束值：'))

r = random.randint(start, end)
count = 0
while True:
    count += 1 
    num = input('請猜數字：')
    num = int(num)
    if num == r:
        print('恭喜你，你猜對了！')
        print('總共花了', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')