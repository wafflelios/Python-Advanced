import re

phone = {
    2: 'a-c',
    3: 'd-f',
    4: 'g-i',
    5: 'j-l',
    6: 'm-o',
    7: 'p-s',
    8: 't-v',
    9: 'w-z'}


def my_t9(numbers):
    with open('/usr/share/dict/words') as file:
        string = file.read()
        sample = ''
        for num in numbers:
            sample += '[' + phone[int(num)] + ']'
        sample = fr"\b{sample}\s"
        res_list = re.findall(sample, string)
    if not res_list:
        print('Words not found')
    else:
        for word in res_list:
            print(word[:-1])


my_t9('22736368')