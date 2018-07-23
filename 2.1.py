from pprint import pprint

cook_book = {}


def get_ingredients():
	dish_name = line.strip()
	number_of_ingredients = int(f.readline().strip())
	counter = 0
	ingredients = []
	ingredients_list = []
	ingredient_dict = {}
	ingredients_dict = {}

	while number_of_ingredients > counter:
		ingredient = f.readline().strip().split(" | ")
		ingredients.append(ingredient)
		counter += 1
	f.readline()  # пустая строка
	for ingredient in ingredients:
		ingredient_dict.update({"ingridient_name":ingredient[0]})
		ingredient_dict.update({"quantity": int(ingredient[1])})
		ingredient_dict.update({"measure": ingredient[2]})
		ingredients_list.append(ingredient_dict.copy())  # не понимаю почему без .copy не работает
	ingredients_dict.update({dish_name:ingredients_list})
	cook_book.update(ingredients_dict)


def get_person_count():
	person_count = input("Введите количество гостей:")
	try:
		person_count = int(person_count)
	except:
		print("Похоже, вы ввели неправильное значение")
	return person_count


def get_dishes():
	dishes = []
	user_input = input("Введите список блюд через запятую:")
	user_input = user_input.split(",")
	for i in user_input:
		i = i.strip()
		dishes.append(i)
	return dishes


def get_shop_list_by_dishes(dishes, person_count):
	ingridient_name_list = []
	ingredients_dict = {}
	for dish in dishes:
		if dish in cook_book.keys():
			for i in cook_book.get(dish):
				dish_quantity = i.get("quantity")
				ingridient = i.get("ingridient_name")
				measure = i.get("measure")

				ingridient_name_list.append(ingridient)
				ingredients_dict.update({ingridient: {"measure": measure, "quantity": dish_quantity*person_count}})

		# for ing in ingridient_name_list:
		# 	print(ing)
		# 	if ingridient in ing:
		# 		print(ingridient)
		# 		print(dish_quantity)
		# 		dish_quantity += dish_quantity
		# 		print(dish_quantity)
		# 		ingredients_dict.update({ingridient: {"quantity": dish_quantity * person_count}})

	pprint(ingredients_dict)




with open("data.txt") as f:
	for line in f:
		get_ingredients()


pprint(cook_book)

get_shop_list_by_dishes(get_dishes(), get_person_count())
