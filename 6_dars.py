car0={
    'modeli':'lacetti',
    'yil':2017,
    'narh':12500,
    'km':123000,
    'karobka':'mexanika'
    }
car1={
    'modeli':'nexia 2',
    'yil':2009,
    'narh':9200,
    'km':165000,
    'karobka':'mexanika'
    }
car2={
    'modeli':'malibu',
    'yil':2023,
    'narh':18000,
    'km':16000,
    'karobka':'avtomat'
    }
car=car0
#print(f"{car['modeli'].title()},"
      #f"{car['yil']}-yil, {car['narh']}$")
cars=[car0, car1, car2]
for car in cars:
    print(f"{car['modeli'].title()},"
          f"{car['yil']}-yil, {car['narh']}$")






