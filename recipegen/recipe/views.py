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

def index(request):
    #link to add delete and list, display initial list of recipes
    recipe = recipeManager('list')
    result = recipe.getRecipeList()
    template = loader.get_template('recipe/index.html')
    context = {'recipeList': result}
    return HttpResponse(template.render(context, request))

def add(request):
    return render(request, 'recipe/add2.html', {'form': AddForm})

def list(request):
    #list all recipes that match search pattern and display view button for each to display
    return render(request)

def retrieve(request):
    return render(request, 'recipe/retrieve.html', {'form': RetrieveForm})

def delete(request):
    return render(request, 'recipe/delete.html', {'form': RetrieveForm})




def newRecipe(request):

     #class for addming and maniplulating recipes. Don'think it really needs to be an object but meh.
     #create dictionary for each ingredient, then roll the ingredients up into a list.
    lIngredients = []
    for i in range(int(request.POST['ingredient'])):
        #ingredient is the number of ingredients
        print(request.POST)
        item = {'ingredient':request.POST['ingredient{}'.format(i)], 'measurement':request.POST['volume{}'.format(i)], 'unit':request.POST['metric{}'.format(i)]}
        lIngredients.append(item)

        #supply recipe name to init
    print(len(lIngredients))
    recipe = recipeManager(request.POST['name'])
    if recipe.createRecipe(lIngredients, request.POST['instructions']) == True:
        return render(request, 'recipe/add2.html')
    else:
        return HttpResponse('could not add recipe')

    #else:
     #   return render(request, 'recipe/add.html', {'form': AddForm})

def retrieveRecipe(request):
    #return the recipe details and display on web page
    form = RetrieveForm(request.POST)
    print(request.POST)
    if form.is_valid():
        recipe = recipeManager(form.cleaned_data['recipeName'])
        returnedRecipe = recipe.retrieveRecipe()
        if returnedRecipe:
            #return name, description and ingredients in a list
            returnedName = returnedRecipe[0]
            returnedDescription = returnedRecipe[1]
            returnedIngredients = returnedRecipe[2]
            context = {'returnedName':returnedName, 'returnedDescription': returnedDescription, 'returnedIngredients':returnedIngredients}
            template = loader.get_template('recipe/result.html')
            return HttpResponse(template.render(context, request))
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
            returnedRecipe = recipe.retrieveRecipe()
            if returnedRecipe:
                return HttpResponse('not deleted')
            else:
                template = loader.get_template('recipe/delete.html')
                context = {'isDeleted': True}
                return HttpResponse(template.render(context, request))

        return HttpResponse('not deleted')
