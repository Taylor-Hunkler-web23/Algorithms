#!/usr/bin/python


# Recipe Batches

# Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

# ```python
# {
#   'eggs': 5,
#   'butter': 10,
#   'sugar': 8,
#   'flour': 15
# }
# ```

# The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

# Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 

# For example

# ```python
# # should return 0 since we don't have enough butter!
# recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
# ```



import math

def recipe_batches(recipe, ingredients):
    whole_batch = []
#loop through recipe and ingredients
    for i in recipe:
 
 #if its not in ingredients or if recipe calls for more than is in ingredients
      if i not in ingredients or recipe[i] > ingredients[i]: 
          return 0

#how many times can each ingredients be used for the recipe, append it to whole_batch
      else:
         whole_batch.append (ingredients[i] // recipe[i])
     
  
    # return the min number to get how many total batches we can make with all ingredients
    return min(whole_batch)

    



   
   


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))