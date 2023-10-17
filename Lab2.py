

quests = [ "Маловесное ( по отношению к постоянной памяти )", "Бесплатное", "Кросс-платформенное", "Потянут слабые ПК", "Написана на С++" ]
for num, i in enumerate(quests):
    print(str(num + 1) + ")", i)
print("=" * 15, "\n")


GraphicProgram = dict()
GraphicProgram["paint"] = [1, 1, 0, 1, 0]
GraphicProgram["photoshop"] = [0, 0, 0, 0, 1]
GraphicProgram["coreldraw"] = [0, 0, 1, 0, 1]



print("Таблица отнощений вопроса к данному существу: ")


# нахожу максимальный по длине ключ из словаря для учёта отступов
tabs = 3
max_len = 0
for i in GraphicProgram:
    max_len = max( max_len, len(i) )


# вывод номера вопроса с учётом отступов
print( " " * ( max_len + tabs ), end = " " )
for i in range(1, len(quests) + 1):
    print(i, end = " ")
print()


for NowEntity in GraphicProgram:
    print( NowEntity + " " * (max_len + tabs - len( str(NowEntity) ) - 1 ), end = "| " )
    for i in GraphicProgram[NowEntity]:
        print(i, end = " ")
    print()

print()
user = (input(f"Введите 2-х животных из списка через пробел {GraphicProgram.keys()}: ")).lower().split(" ")

result = list()

for i in range( 0, len( GraphicProgram[ user[0] ] ) ):
    if GraphicProgram[ user[0] ][i] == GraphicProgram[ user[1] ][i]:
        result.append(0)
    else:
        result.append(1)


print( "Разница "+ user[0] + " и " + user[1] + " : ", end = "")
for i in result:
    print(i, end = " ")


if( sum(result) > len( quests ) // 2 ):
    print(f"\n{user[0]} и {user[1]} абсолютно разные, между ними имеются большинство различий")
else:
    print(f"\n{user[0]} и {user[1]} почти похожи, используйте что вам удобно :)")



print()



