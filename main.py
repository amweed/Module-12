per_cent= {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit=[]
for i in  per_cent:
    deposit.append(per_cent[i]*money/100)
print(deposit)
print("Max=",max(deposit))


