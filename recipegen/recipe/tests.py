from django.test import TestCase, Client
from random import randint
from .RecipeGenLibary import recipeManager



# Create your tests here.
class RecipeManagement(TestCase):


    def setUp(self):
        self.lIngredients = []
        self.recipeName = 'beans'
        self.recipeDescription = 'put beans in pan. Put toast in toaster then mix'
        for i in range(randint(0, 9)):
            item = {'ingredient': 'beans',
                    'measurement': '100', 'unit': 'tonnes'}
            self.lIngredients.append(item)

    def test_RecipeAdd(self):
        #that the data gets added
        print('test adding data')
        recipe = recipeManager(self.recipeName)
        result = recipe.createRecipe(self.lIngredients, self.recipeDescription)
        self.assertEqual(result, True)

        """the class returns the requested recipe and the data matches"""
        print('test checking data')
        returnedRecipe = recipe.retrieveRecipe()
        print('returned recipe is {}'.format(returnedRecipe))
        self.assertTrue(returnedRecipe)
            #return name, description and ingredients in a list
        returnedName = returnedRecipe[0]
        returnedDescription = returnedRecipe[1]
        returnedIngredients = returnedRecipe[2]

        #if (returnedName == self.recipeName) and (returnedDescription == self.recipeDescription):
            #print('name and description match')
            #if cmp(self.lIngredients, returnedIngredients):
        self.assertEqual(returnedName, self.recipeName)
        self.assertEqual(returnedDescription, self.recipeDescription)
        self.assertEqual(returnedIngredients, self.lIngredients)



        print('test deleting data')
        """Animals that can speak are correctly identified"""
        result = recipe.deleteRecipe()

        self.assertEqual(result, True)


        #a non existing entry is handled correctly
        print('test checking data deleted')
        returnedRecipe = recipe.retrieveRecipe()
        self.assertFalse(returnedRecipe)


    def test_RecipeAddExisting(self):
        #that the data gets added
        print('test adding data')
        recipe = recipeManager(self.recipeName)
        result = recipe.createRecipe(self.lIngredients, self.recipeDescription)
        self.assertEqual(result, True)

        """the class returns the requested recipe and the data matches"""
        print('test checking data')
        returnedRecipe = recipe.retrieveRecipe()
        print('returned recipe is {}'.format(returnedRecipe))
        self.assertTrue(returnedRecipe)
            #return name, description and ingredients in a list
        returnedName = returnedRecipe[0]
        returnedDescription = returnedRecipe[1]
        returnedIngredients = returnedRecipe[2]

        #if (returnedName == self.recipeName) and (returnedDescription == self.recipeDescription):
            #print('name and description match')
            #if cmp(self.lIngredients, returnedIngredients):
        self.assertEqual(returnedName, self.recipeName)
        self.assertEqual(returnedDescription, self.recipeDescription)
        self.assertEqual(returnedIngredients, self.lIngredients)

        print('test adding duplicate data')
        recipe = recipeManager(self.recipeName)
        result = recipe.createRecipe(self.lIngredients, self.recipeDescription)
        self.assertEqual(result, False)

        print('test deleting data')
        """Animals that can speak are correctly identified"""
        result = recipe.deleteRecipe()

        self.assertEqual(result, True)


        #a non existing entry is handled correctly
        print('test checking data deleted')
        returnedRecipe = recipe.retrieveRecipe()
        self.assertFalse(returnedRecipe)


class RecipeView(TestCase):
    #add recipe. Verify its added
    #check added recipe matches what was added
    #delete recipe check delete happened


    def test_WebRecipeAdd(self):

        c = Client()
        paremeters= {}
        paremeters['instructions'] = 'beans'
        paremeters['csrfmiddlewaretoken'] = 'b4FuTtgiAGBmhzx97e7DKdR0buUB13Wf7YOWkeb2hYXlUl7RBwz8YLxFWnvbefhN'
        paremeters['name'] = 'beans'
        compareIngredientsList = []

        for i in range(randint(0, 9)):
            paremeters['volume{}'.format(i)] = '100'
            paremeters['metric{}'.format(i)] = 'tonnes'
            paremeters['ingredient{}'.format(i)] = 'beans'

            #create list of dictionaries for checking later
            compareParameters = {'measurement': paremeters['volume{}'.format(i)], 'unit':paremeters['metric{}'.format(i)], 'ingredient':paremeters['ingredient{}'.format(i)]}
            compareIngredientsList.append(compareParameters)
        #number of ingredients but need to add an extra for the count to work out
        paremeters['ingredient'] = i +1

        print('adding recipe from form')

        """response = c.post('/recipe/newRecipe/', {'instructions': ['beans'],
                    'csrfmiddlewaretoken': ['b4FuTtgiAGBmhzx97e7DKdR0buUB13Wf7YOWkeb2hYXlUl7RBwz8YLxFWnvbefhN'],
                    'name': ['beans'], 'volume0': ['100'], 'metric0': ['tonnes'], 'ingredient0': ['beans'],
                    'ingredient': ['1']})
        self.assertEqual(response.status_code, 200)"""
        response = c.post('/recipe/newRecipe/', paremeters)
        self.assertEqual(response.status_code, 200)

        print('finding recipe from form')
        response = c.post('/recipe/retrieveRecipe/', {'recipeName' : 'beans', 'csrfmiddlewaretoken' :'b4FuTtgiAGBmhzx97e7DKdR0buUB13Wf7YOWkeb2hYXlUl7RBwz8YLxFWnvbefhN'})
        self.assertEqual(response.status_code, 200)

        result = response.context

        #for i in result:
         #   print(i)

        self.assertEqual(result['returnedDescription'], paremeters['instructions'] )
        self.assertEqual(result['returnedName'], paremeters['name'])
        print('returned ingredient list')

        print(result['returnedIngredients'])
        print('origional ingredient list')
        print(compareIngredientsList)

        #print('checking result')
        #print(result)
        self.assertEqual(result['returnedIngredients'], compareIngredientsList)

        response = c.post('/recipe/deleteRecipe/', {'recipeName' : 'beans', 'csrfmiddlewaretoken' :'b4FuTtgiAGBmhzx97e7DKdR0buUB13Wf7YOWkeb2hYXlUl7RBwz8YLxFWnvbefhN'})
        self.assertTrue(response.context['isDeleted'])
    def tearDown(self):

        recipe = recipeManager('beans')
        result = recipe.deleteRecipe()