regim = input('режим копоратора,сравнивание - "1" или вачитание - "2":')

if not (regim == '1' or regim == '2'):
    print('введёная вами операция не верная, попробуй "1" или "2" =)')
else:
    sig_a = int(input("1 значение (число):"))
    sig_b = int(input("2 значение (число):"))
    if regim == '1':
        if sig_a >= sig_b:
            print(sig_a)        #добрый майнкрафтер +rep
        else:
            print("0")
    else:
        raznost = sig_a - sig_b
        if raznost >= 0:
            print(raznost)
        else:
            print("0")
                      
