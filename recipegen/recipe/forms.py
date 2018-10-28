from django import forms


class AddForm(forms.Form):
    ingredient = []
    measurement = []
    unit = []
    recipeName = forms.CharField(label='Name', max_length=100)

    """for i in range(1, 5, 1):
        ingredient.append(forms.CharField(label='Ingredient', max_length=100))
        measurement.append(forms.CharField(label='Measurement', max_length=100))
        unit.append(forms.CharField(label='Unit', max_length=100))"""

    ingredientOne=forms.CharField(label='Ingredient', max_length=100)
    measurementOne=forms.CharField(label='Measurement', max_length=100)
    unitOne = forms.CharField(label='Unit', max_length=100)

    ingredientTwo = forms.CharField(label='Ingredient', max_length=100)
    measurementTwo = forms.CharField(label='Measurement', max_length=100)
    unitTwo= forms.CharField(label='Unit', max_length=100)

    ingredientThree = forms.CharField(label='Ingredient', max_length=100)
    measurementThree = forms.CharField(label='Measurement', max_length=100)
    unitThree = forms.CharField(label='Unit', max_length=100)

    recipeDescription = forms.CharField(widget=forms.Textarea)



class RetrieveForm(forms.Form):
    recipeName = forms.CharField(label='Name', max_length=100)
