from django import forms

choice_method = [
  ('booleen', 'Booléen'),
  ('vectoriel', 'Vectoriel'),
  ('probabiliste', 'Probabiliste'),
]

choice_appariement = [
  ('prod_intern','Produit Interne'),
  ('coef_dice','Coef de Dice'),
  ('cosinus','Cosinus'),
  ('jaccard','Jaccard'),
]


class searchForm(forms.Form):
  requete = forms.CharField(label="Requête", max_length="100")
  method = forms.ChoiceField(choices=choice_method, widget=forms.RadioSelect())
  appariement = forms.ChoiceField(choices=choice_appariement, widget=forms.RadioSelect())

class evaluteForm(forms.Form):
  pertinent = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())