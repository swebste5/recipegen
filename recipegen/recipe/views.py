from django.shortcuts import render
from .forms import AddForm, RetrieveForm
from django.http import HttpResponse
from django.template import loader
from .RecipeGenLibary import recipeManager
# Create your views here.
"""start simple. Create flat recipe and ingredients list and pickle them. 
Then add a way to delete recipe
Once done create the meal plan generator
Then make the add page dynamic so there is no limit to number of ingredients
Once that is done structure the data into a database of some sort
Once that is done create the shopping list function"""

def add(request):
    return render(request, 'recipe/add.html', {'form': AddForm})

def list(request):
    #list all recipes that match search pattern and display view button for each to display
    return render(request)

def retrieve(request):
    return render(request, 'recipe/retrieve.html', {'form': RetrieveForm})

def delete(request):
    return render(request, 'recipe/delete.html', {'form': RetrieveForm})


def newRecipe(request):
    form = AddForm(request.POST)
    if form.is_valid():
        """class for addming and maniplulating recipes. Don'think it really needs to be an object but meh."""
    #this needs looping, create dictionary for each ingredient, then roll the ingredients up into a list.
        lIngredients = []
        #item = {'ingredient':form.cleaned_data['ingredientOne'], 'measurement':form.cleaned_data['measurementOne'], 'unit':form.cleaned_data['unitOne']}

       # lIngredients.append(item)

       # item = {'ingredient': form.cleaned_data['ingredientOne'], 'measurement': form.cleaned_data['measurementOne'],
                #'unit': form.cleaned_data['unitOne']}
       # lIngredients.append(item)

       # item = {'ingredient': form.cleaned_data['ingredientOne'], 'measurement': form.cleaned_data['measurementOne'],
                #'unit': form.cleaned_data['unitOne']}
        item = form.cleaned_data['recipeName']
        lIngredients.append(item)
        #supply recipe name to init
        recipe = recipeManager(form.cleaned_data['recipeName'])
        recipe.createRecipe(lIngredients, form.cleaned_data['recipeDescription'])

        return render(request, 'recipe/add.html', {'form': AddForm})

    else:
        return render(request, 'recipe/add.html', {'form': AddForm})



def retrieveRecipe(request):
    #return the recipe details and display on web page
    form = RetrieveForm(request.POST)
    if form.is_valid():
        recipe = recipeManager(form.cleaned_data['recipeName'])
        returnedRecipe = recipe.retrieveRecipe()
        if returnedRecipe:
            #return name, description and ingredients in a list
            returnedName = returnedRecipe[0]
            returnedDescription = returnedRecipe[1]
            returnedIngredients = returnedRecipe[2]
            return HttpResponse('{}<br>{}<br>{}br'.format(returnedName, returnedDescription, returnedIngredients))
        else:
            return HttpResponse('could not find recipe')

    else:
        return render(request, 'recipe/retrieve.html', {'form': RetrieveForm})


def deleteRecipe(request):
    #c delete the entry from db

    form =RetrieveForm(request.POST)
    if form.is_valid():
        recipe = recipeManager(form.cleaned_data['recipeName'])
        result = recipe.deleteRecipe()
        if result == True:
            return HttpResponse('deleted')

        return HttpResponse('not deleted')
