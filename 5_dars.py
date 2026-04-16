#LUG'ATLAR
car_0={'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
#print(car_0['rang'])

en_uz={'apple':'olma','car':'avtomobil','pen':'ruchka'}
#print(en_uz['apple'])
#print(en_uz['car'])

mevalar={'olma':'10000','banan':'15000','kivi':'27000'}
#print(f'Olma narhi {mevalar['olma']} so\'m')
#print(f'Kivi narhi {mevalar['kivi']} so\'m')

talaba_0={'ism_familya':'mansurov bunyod','yosh':'18','t_yili':'2000'}
#print(f'{talaba_0['ism_familya'].title()},\
#{talaba_0['yosh']} yoshda, {talaba_0['t_yili']}-yilda tug\'ilgan')
#talaba_0['kurs']=1
#talaba_0['fakultet']='axborot xafsizligi'
#print(talaba_0)
#o'chirish maqsadida [del] funksiyasidan foydalanamiz
#del talaba_0['yosh']

#BO'SH LUG'AT
talaba_1={}
talaba_1['ism']='bunyod'
talaba_1['kurs']=1
talaba_1['yosh']=18
#print(talaba_1)
#print(f'Talabaning ismi {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda\
#o\'qiydi va u {talaba_1['yosh']} da')

telefon={
    'ali':'iPhone 11 pro',
    'javohir':'iPhone17',
    'olim':'mi not 10 pro'
    }
#print(f'Ali {telefon['ali']} rusumli telefon ishlatadi')
#phone=telefon.get('hasan','Bunday ism mavjud emas')
#print(phone)

#LUG'AT QO'SHIMCHALARI

talaba_2={
    'ism':'Bunyod',
    'familya':'Mansurov',
    'yosh':18,
    'fakultet':'axborot xafsizligi',
    'kurs':1
    }
#print(talaba_2.items())  #.items- elementlar

#for kalit, qiymat in talaba_2.items():
    #print(f'Kalit:{kalit}')
    #print(f'Qiymat:{qiymat}\n')


#for k, q in telefon.items():
    #print(f'{k.title()}ning telefoni {q}')
  
#.keys()-lug'at ichidagi kalitni qaytaradi
mahsulotlar_0={
    'uzum':10000,
    'anor':7500,
    'non':4200,
    'baliq':14200
    }
#print(mahsulotlar_0.keys())
#print('Do\'kondagi mahsulotlar:')
#for mahsulot in mahsulotlar_0.keys():
    #print(mahsulot.title())


bozorlik=['uzum','non','go\'sht','yog\'']
#for mahsulot in mahsulotlar_0:
    #if mahsulot in bozorlik:
        #print(f'{mahsulot.title()} {mahsulotlar_0[mahsulot]} so\'m')
        
#print('Do\'konimizdagi mahsulotlar:')
#for mahsulot in sorted(mahsulotlar_0):
    #print(mahsulot.title())

telefon_0={
    'ali':'iPhone 11 pro',
    'javohir':'iPhone17',
    'olim':'mi not 10 pro',
    'bobur':'iPhone 11 pro',
    'jalil':'mi not 10 pro'
    }
#print(telefon.values())
#print('Bizda quyidagi telefonlar bor:')
#for tel in telefon.values():
    #print(tel)

#set- bir nechtani bita qiladi
#for tel in set(telefon_0.values()):
    #print(tel)

#toys={'ball','car','lamp','ball'}




