def decrypt(enter_info):
    data = enter_info.split('..')
    not_empty_index = 0
    for counter in range(0, len(data) - 1):
        if data[counter + 1] != '' and data[counter] != '':
            data[counter] = data[counter][:-1]
            not_empty_index = counter
        else:
            data[not_empty_index] = data[not_empty_index][:-1]
    res = ''.join(data).replace('.', '')
    return res