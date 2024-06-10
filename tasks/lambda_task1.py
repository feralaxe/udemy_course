def greet(greeting):
    return lambda name: f'{greeting}, {name}!'


morning_greet = greet('Good morning')
print(morning_greet('Lesha'))

evening_greet = greet('Good evening')
print(evening_greet('Lesha'))
