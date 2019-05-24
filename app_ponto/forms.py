from django import forms
class FrequenciaForm(forms.Form):
    #não sei se funciona sem isso!
    #testem!!!
    def clean(self):
        dados = super().clean()
        return dados
        