
country = str(input()).title()

Capitals = dict()
Capitals["Россия"]="Москва"
Capitals["Германия"]="Берлин"
Capitals["Финляндия"]="Хельсинки"

if country in Capitals:
    print("Столица: ", Capitals[country])
else:
    print("Страна неизвестна")

