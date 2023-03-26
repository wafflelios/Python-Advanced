import json
import re

critical_five, count_dog = 0, 0
debug, info, warnings, error, critical = 0, 0, 0, 0, 0
lines, logs_per_hour, warnings_word = [], {}, {}
with open('skillbox_json_messages.log') as file:
    for line in file:
        lines.append(json.loads(line))

for line in lines:
    if 'dog' in line['message']:
        count_dog += 1
    if line['time'].split(':')[0] not in logs_per_hour.keys():
        logs_per_hour[line['time'].split(':')[0]] = 1
    else:
        logs_per_hour[line['time'].split(':')[0]] += 1
    if line['level'] == 'DEBUG':
        debug += 1
    elif line['level'] == 'INFO':
        info += 1
    elif line['level'] == 'WARNING':
        for word in re.findall(r'\w+', line['message']):
            if word not in warnings_word.keys():
                warnings_word[word] = 1
            else:
                warnings_word[word] += 1
        warnings += 1
    elif line['level'] == 'ERROR':
        error += 1
    else:
        if line['time'].split(':')[0] == '05' and 0 <= int(line['time'].split(':')[1]) <= 20:
            critical_five += 1
        critical += 1
logs_per_hour = sorted(logs_per_hour.items(), key=lambda item: item[1], reverse=True)
warnings_word = sorted(warnings_word.items(), key=lambda item: item[1], reverse=True)

print(f'Количество сообщений уровня DEBUG: {debug}\n'
      f'Количество сообщений уровня INFO: {info}\n'
      f'Количество сообщений уровня WARNING: {warnings}\n'
      f'Количество сообщений уровня ERROR: {error}\n'
      f'Количество сообщений уровня CRITICAL: {critical}\n'
      f'\n'
      f'В {int(logs_per_hour[0][0])} часов было больше всего логов.\n'
      f'\n'
      f'В период с 05:00:00 по 05:20:00 было {critical_five} логов уровня CRITICAL.\n'
      f'\n'
      f'{count_dog} сообщений содержат слово dog.\n'
      f'\n'
      f'Слово {warnings_word[0][0]} встречалось чаще всего в сообщениях уровня WARNING.')