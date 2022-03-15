hello = 'Hello,'
name = input("What's your name?\n")
greeting = hello + ' ' + name
print(greeting)
age = int(input("How old are you?\n"))
decades = str(age//10)
years = str(age%10)
response = name + " you are " + decades + " decades and " + years + " years old."
print(response)