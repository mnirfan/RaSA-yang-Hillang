def list2int(list_number):
    string = "1"
    for i in list_number:
        string += ''.join(format(i, '016b'))
    #binary_list = ''.join(format(x, '016b') for x in list_number)
    print("bentuk biner :",string)
    return int(string, 2)

def int2list(int_number):
    binary_list = bin(int_number)[3:]
    string = []
    for i in range(int(len(binary_list)/16)):
        number = int(binary_list[0:16], 2)
        string.append(number)
        binary_list = binary_list[16:]

    return string


"""
==============
Daftar pustaka
==============

convert string to binary [https://stackoverflow.com/questions/18815820/convert-string-to-binary-in-python#18815890]
convert binary to int [https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int]

convert int to binary [https://stackoverflow.com/questions/699866/python-int-to-binary#699891]
convert int to ascii and vice versa [https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python#3673447]

"""
