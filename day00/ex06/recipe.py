import sys

cookbook = {
    'sandwich':{
        'ingredients':['ham', 'bread', 'cheese', 'tomatoes'],
        'meal':'lunch',
        'prep_time':10
    },
    'cake':{
        'ingredients':['flour', 'sugar', 'eggs'],
        'meal':'dessert',
        'prep_time':60
    },
    'salad':{
        'ingredients':['avocado', 'aragula', 'tomatoes', 'spinach'],
        'meal':'lunch',
        'prep_time':15
    }
}

def print_menu():
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")


def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}


def print_recipe(recipe_name):
    try:
        print("\nRecipe for {}".format(recipe_name))
        print("Ingredients list: {}".format(cookbook[recipe_name]['ingredients']))
        print("This is a recipe ideal for: {}".format(cookbook[recipe_name]['meal']))
        print("It takes {} minute(s) to cook\n".format(cookbook[recipe_name]['prep_time']))
    except:
        pass


def delete_recipe(recipe_name):
    try:
        del cookbook[recipe_name]
        print('Recipe {} deleted.'.format(recipe_name))
    except KeyError:
        print("\nCan't find this recipe in the cookbook.\n")


def print_all_recipes():
    for k in cookbook.keys():
        print_recipe(k)


if __name__ == '__main__':
    while True:
        print_menu()
        i = input()
        try:
            i = int(i)
        except ValueError:
            print("Valid inputs are 1, 2, 3, 4 or 5")
        if i == 1:
            recipe_name = input("Please enter the recipe's name: ")
            try:
                ingredients = input("Please enter the ingredients separated by spaces: ")
                ingredients = list(ingredients.split())
            except ValueError:
                print("\nInput format for ingredients is wrong. Try again.\n")
                continue
            meal = input("Please enter what kind of meal this is:")
            try:
                prep_time = input("Please enter the meal preparation time: ")
                prep_time = int(prep_time)
            except ValueError:
                print("\nInput format wrong for preparation time. Try again.\n")
                continue
            add_recipe(recipe_name, ingredients, meal, prep_time)
        if i == 2:
            recipe_name = input("Please enter the recipe you wish to delete ")
            delete_recipe(recipe_name)
        if i == 3:
            recipe_name = input("Which recipe would you like to read? ")
            print_recipe(recipe_name)
        if i == 4:
            print_all_recipes()
        if i == 5:
            print("\n Bye!! ;)\n")
            sys.exit()
