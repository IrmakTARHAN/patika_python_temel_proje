#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

def reverse_list(input_list):
    if not input_list:
        return []

    reversed_list=[]
    for item in input_list:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list[::-1]

input_data = eval(input("lütfen liste giriniz: "))
output_data = reverse_list(input_data) 
print("Ters çevrilmiş hali: ",output_data)    