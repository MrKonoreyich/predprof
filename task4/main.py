def generate(name,date) -> str:
    """Генерирует промокод
        name - название продукта
        date - дата постулпления
    """
    date = date.split('.')
    return name[:2].upper() + date[0] + ''.join(reversed(name[-2:])).upper() + ''.join(reversed(date[1]))
f = [x for x in open('products.csv', encoding='utf-8-sig').read().split('\n')]
finallist = []
headers = f.pop(0)+';promocode\n'
for i in f:
    ls = list(map(str,i.split(';')))
    s = generate(ls[1],ls[2])
    finallist += [[ls[0],ls[1],ls[2],ls[3],ls[4], s]]
promofile = open('product_promo.csv',encoding='utf-8-sig',mode='w')
promofile.write(headers)
for i in finallist:
    promofile.write(';'.join(i)+'\n')