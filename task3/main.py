with open('products.csv', encoding='utf-8-sig') as f:
    product = ''
    while True:
        min = float('inf')
        x = input()
        if x == 'молоко': exit()
        f = [i for i in f.read().split('\n') if x in i.split(';')[0]]
        if len(f)==0:
            print('Такой категории не существует в нашей БД')
        for i in f:
            ls = list(map(str,i.split(';')))
            count = int(float(ls[-1]))
            if count < min:
                min = count
                product = ls[1]
    print(f'В категории {x} товар: {product} был куплен {count} раз')