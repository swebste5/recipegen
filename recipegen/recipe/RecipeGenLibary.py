
"""classes to be used in app. not convinced this is the way to do it."""
import json
import shelve
class recipeManager(object):
    def __init__(self, recipeName):
        self.recipeName = recipeName


    def createRecipe(self, recipeIngredients, recipeDescription):
        self.recipeIngredients = recipeIngredients
        self.recipeDescription = recipeDescription

        #recipe ingredients is a list of dictionaries, one for each ingredient

        #self.storeRecipeJson(self.recipeName, self.recipeIngredients, self.recipeDescription )
        self.storeRecipeShelve()


    def retrieveRecipe(self):
        #retrieve reciple via named supplied by init or argument
        result = self.getRecipeExists()
        if result == False:
            return False

        result= self.getRecipeShelve()
        if result:
            #packup attributes and return in a list. Could access directly from view but meh
           # self.recipeName = result.recipeName
           # self.recipeDescription = result.recipeDescription
           # self.recipeIngredients = result.recipeIngredients
            self.lResult = [result.recipeName, result.recipeDescription, result.recipeIngredients]
            print(self.lResult)
            return self.lResult
        else:
            return False

    def deleteRecipe(self):
        result = self.getRecipeExists()
        if result == False:
            return False
        database = shelve.open('recipes')
        del database[self.recipeName]

        return True


    # delete reciple via named supplied by init or argument but only if ardgument and init match



    ###we need to access and retrieve from there outside of the object
    def storeRecipeJson(recipeName,recipeIngredients, recipeDescription):
        #create json for each recipe. Could either use pickle to file, shelve to flat db
        #json can be read and used by other apps.

        json_dict = {}
        json_dict['name']= recipeName
        json_dict['ingredients'] = recipeIngredients
        json_dict['description'] = recipeDescription

        with open(self.recipeName, 'w') as outfile:
            json.dump(json_dict, outfile)


    def getRecipeJson(recipeName):
        #retrieve details from json for recipe and load into dict. Could either use pickle to file, shelve to flat db
        #json can be read and used by other apps.



        with open(self.recipeName, 'r') as infile:
            json_dict = json.load(infile)
            return json_dict


    def storeRecipeShelve(self):
        #Use shelve as all of the recipes will be kept in single flat file

        database = shelve.open('recipes')
        #supply the full object to shelf?
        database[self.recipeName]= self



        print(database[self.recipeName])
        database.close()

    def getRecipeExists(self):
        # pull file and except exception if problem
        database = shelve.open('recipes')
        try:
            returnedRecipe=database[self.recipeName]
        except KeyError:
            print('key doesnt exist')
            database.close()
            return False
        database.close()
        return True

    def getRecipeShelve(self):
        #Use shelve as all of the recipes will be kept in single flat file
        #big guess here but retrieve the object in shelf and make self= it to override. then return the attributes of it
        database = shelve.open('recipes')
        #supply the full object to shelf?
        #change this to manually unpack and try updating self.parameters manually.
        returnedRecipe = database[self.recipeName]

        #need some sort of catch here for if you send wrong name

        database.close()
        return returnedRecipe
