from django import forms


class AddForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #ingredients = kwargs.pop('ingredients')

        super(AddForm, self).__init__(*args, **kwargs)
        counter = 1
        #or q in ingredients:
        self.fields['recipeName'] = forms.CharField(label='Name', max_length=100)
        self.fields['recipeDescription'] = forms.CharField(widget=forms.Textarea)
        for q in range(0, 100, 1):
            self.fields['ingredient-' + str(counter)] = forms.CharField(label='Ingredient', max_length=100)
            self.fields['measurement-' + str(counter)] = forms.CharField(label='Measurement', max_length=100)
            self.fields['unit-' + str(counter)] = forms.CharField(label='Unit', max_length=100)
            counter += 1

    #ingredient = []
    #measurement = []
    #unit = []

        """for i in range(0, 100, 1):
            ingredient.append(forms.CharField(label='Ingredient', max_length=100))
             measurement.append(forms.CharField(label='Measurement', max_length=100))
            unit.append(forms.CharField(label='Unit', max_length=100))"""









class RetrieveForm(forms.Form):
    recipeName = forms.CharField(label='Name', max_length=100)
