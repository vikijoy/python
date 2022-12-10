# Задача 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('42_RLE1_decoded_in.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    str_code += str(count) + prev_char
    return str_code

str_code = encode_rle(my_text)
print(str_code)

with open('42_RLE1_decoded_out.txt', 'w') as data:
    data.write(str_code)

with open('42_RLE2_encoded_in.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print(str_decode)

with open('42_RLE2_encoded_out.txt', 'w') as data:
    data.write(str_decode)