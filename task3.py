import re

points_en = {1:'AEIOULNSTR',
      	     2:'DG',
      	     3:'BCMP',
             4:'FHVWY',
      	     5:'K',
      	     8:'JX',
      	     10:'QZ'}

points_ru = {1:'АВЕИНОРСТ',
      	     2:'ДКЛМПУ',
      	     3:'БГЁЬЯ',
      	     4:'ЙЫ',
      	     5:'ЖЗХЦЧ',
      	     8:'ШЭЮ',
      	     10:'ФЩЪ'}

text = input("Введите слово: ").upper()
sum = 0

if re.search('[а-яА-Я]', text):    #
    for i in text:
        for b, c  in points_ru.items():
            if i in c:
                sum += b
else:
    for i in text:
        for b, c in points_en.items():
            if i in c:
                sum+= b
print(f"Стоимость слова ровна: {sum}")            
   


    






