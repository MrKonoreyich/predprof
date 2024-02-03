nproducts = open('products_new.csv', mode='w', encoding='utf-8-sig')
summary = 0
with open('products.csv', encoding='utf-8-sig') as f:
    f = f.read().split('\n')
    header = f.pop(0)+';Total\n' # delete headers
    nproducts.write(header) # adding headers to new product file
    for st in f:
        st = list(map(str,st.split(';')))
        h = int(float(st[-2]))*int(float(st[-1]))
        st += [str(h)]
        if st[0] == 'Закуски':
            summary+=h # summary of "Закуски"
        nproducts.write(';'.join(st)+'\n')
print(summary)
nproducts.close()