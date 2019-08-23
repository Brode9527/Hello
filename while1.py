while True:
    mode = input('請輸入遊戲模式：')
    if mode == 'q':
        break
    elif mode == '1':
        print('遊戲模式一')
    elif mode == '2':
        print('遊戲模式二')
    else:
        print('請輸入 1/2/q')
