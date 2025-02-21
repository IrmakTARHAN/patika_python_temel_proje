#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

import ast

def flatten(lst): # Bu fonksiyon, parametre olarak bir liste alır ve bu listeyi düzleştirerek geri döndürür.
    flat_list = []
    
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item)) #extend ile istediğin her şeyi ekleyebilirisin
        else:
            flat_list.append(item) #append tek bir eleman ekler
    return flat_list

input_str = input("Lütfen bir liste giriniz: ")

input_list = ast.literal_eval(input_str)

output_list = flatten(input_list)

print("Düzleştirilmiş liste: ", output_list)


