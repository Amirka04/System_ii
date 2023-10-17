print("Вопросы по которым состовлялась таблица:")
print("1) Язык для разработки игр")
print("2) Язык для разработки сайтов")
print("3) Процедурный язык программирования")
print("4) В ЯП есть ООП")
print("5) Сложный ЯП\n\n")
print("=" * 15)


ProgrammingLanguage = dict()
ProgrammingLanguage["Pascal"]       =   [0, 0, 1, 1, 0]
ProgrammingLanguage["C++"]          =   [1, 0, 0, 1, 1]
ProgrammingLanguage["PHP"]          =   [0, 1, 0, 1, 1]
ProgrammingLanguage["JS"]           =   [1, 1, 0, 1, 1]
ProgrammingLanguage["Assembler"]    =   [0, 0, 1, 0, 1]

print("Таблица отнощений вопроса к ЯП: ")

tabs = 3
for Language in ProgrammingLanguage:
    print(Language + " " * (len("Assembler") + tabs - len(str(Language))) + str(ProgrammingLanguage[Language]))

ProgKeys = list()
for i in ProgrammingLanguage:
    ProgKeys.append(i)
print(*ProgKeys)

user_input = (input(f"Введите любые 2 ЯП из перечисленных далее {ProgKeys}\n$: ")).split()
result = list()
for i in range(0, len( ProgrammingLanguage[ user_input[0] ] ) ):
    if( ProgrammingLanguage[ user_input[ 0 ] ][i] == ProgrammingLanguage[ user_input[ 1 ] ][i]):
        result.append(0)
    else:
        result.append(1)

print("Разность между " + user_input[0]+ " и " + user_input[1] + " : ", result)