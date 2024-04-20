username = 'Aleksei'
numbers = {1, 15, 35}
today = '03.04.2024'
userid = 123456789

message = f'Hello, {username}, ID={userid}. Your lucky numbers today, {today}, are: {numbers}.'
print(message)

# let's capitalize every word

new_message = ''
for word in message.split():
    new_message = f'{new_message} {word.capitalize()}'
new_message.strip()
print(new_message)
