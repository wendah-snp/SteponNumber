#list angka
list_awal = [
    [4,2],
    [6,6],
    [3,4]
]

def steponNumber(daftar):
    for i in list_awal: #looping penambahan list dalam list
        result = list_awal[i] + list_awal[i+1]
    return result

print(steponNumber(list_awal))