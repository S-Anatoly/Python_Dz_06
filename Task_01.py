list_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def get_sign(a):
    if a[0] in '+-':
        return a[0]

i = 0
while i < len(list_data):
    sign = get_sign(list_data[i])
    if list_data[i].isdigit() == True or (sign and list_data[i][1:].isdigit()):
        if sign:
            list_data[i] = sign + list_data[i][1:].zfill(2)
        else:
            list_data[i] = list_data[i].zfill(2)
        list_data.insert(i, '"')
        list_data.insert(i + 2, '"')
        i += 2
    i += 1

print(' '.join(list_data))
# в " 05 " часов " 17 " минут температура воздуха была " +05 " градусов
