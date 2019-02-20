# Tuples

# 1. Simple Example
cakeRecIngredients = ('Baking Soda', 'Flour', 'Egg', 'Sugar')

# 2. Tuple of lists
cakeRecDetailedIngredients = (['Baking Soda', 'One Spoon'], ['Flour', 'One Cup'], ['Egg', 'Two'])

# 2.1 Operations on the tuple of lists
test = cakeRecDetailedIngredients.__contains__(['Egg','Two'])
print(test)

print(len(cakeRecIngredients))



# Lists
computerSciCourses = ['OS', 'Programming', 'AI', 'DB']
del computerSciCourses[0]
print(computerSciCourses)