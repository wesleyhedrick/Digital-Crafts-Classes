person = "You"
today = "day"
emotion = "concerned"


first_result = 'Hello ' + person + ',\nI hope that your ' + today + ' is going well.\nI\'m personally really ' + emotion+'.'
second_result = 'Hello %s,\nI hope that your %s is going well.\nI\'m personally really %s.' %(person, today, emotion)
third_result = f'Hello {person},\nI hope that your {today} is going well.\nI\'m personally really {emotion}.'


print(first_result)
print(second_result)
print(third_result)