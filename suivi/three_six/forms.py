from django import forms
from .models import PracticalLife, SensoryMaterial, Math, Letter
from students.model import Students


class StudentForm(forms.Form):
    ENVIRONMENT_CHOICES = [
        ('Bois', 'Bois'),
        ('terre', 'Terre'),

    ]

    image = forms.ImageField(label="", widget=forms.FileInput())
    first_name = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"size": 60}))
    last_name = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"size": 60}))
    date_of_birth = forms.DateField(label="Dta de naissance", widget=forms.DateInput())
    reference_phone = forms.CharField(label="Numéro de téléphone", widget=forms.TextInput(attrs={"size": 60}))
    ambiance = forms.ChoiceField(label='Ambiance', choices=ENVIRONMENT_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Students


class PracticalLifeForm(forms.Form):
    LEVEL_CHOICES = (
        ('PRESENTED', 'Présentée'),
        ('PROCESSING', "En cours d'acquisition"),
        ('ACQUIRED', 'Acquise')
    )

    move_mood = forms.ChoiceField(label="Se déplacer dans l'ambiance", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    carry_table = forms.ChoiceField(label="Porter une table seul, à deux", choices=LEVEL_CHOICES,
                                    widget=forms.RadioSelect())
    Carry_tray = forms.ChoiceField(label="Porter un plateau", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    Carrying_mat = forms.ChoiceField(label="Porter, dérouler et rouler un tapis", choices=LEVEL_CHOICES,
                                     widget=forms.RadioSelect())
    open_close_door = forms.ChoiceField(label="Ouvrir et fermer une porte",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    open_close_window = forms.ChoiceField(label="Ouvrir et fermer une fenêtre, un tiroir",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_preliminary_exercises = forms.CharField(label="Observations exercices préliminaires",
                                                         widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))
    squeeze_sponge = forms.ChoiceField(label="Presser une éponge", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    Screw_bolts = forms.ChoiceField(label="Visser, dévisser des boulons",
                                    choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    open_close_padlock = forms.ChoiceField(label="Ouvrir et fermer un cadenas",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    use_clothes_pegs = forms.ChoiceField(label="Se servir de pinces à linge",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    open_close_boxes = forms.ChoiceField(label="Ouvrir et fermer des boites",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    open_close_bottles = forms.ChoiceField(label="Ouvrir et fermer des flacons",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    fold_fabrics = forms.ChoiceField(label="Plier des étoffes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    fold_paper = forms.ChoiceField(label="Plier du papier", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    cut_paper_scissors = forms.ChoiceField(label="Couper du papier avec des ciseaux",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    paste_paper = forms.ChoiceField(label="Coller du papier", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    dust = forms.ChoiceField(label="Epousseter avec un chiffon, un plumeau",
                             choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sweep = forms.ChoiceField(label="Balayer", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    brush_carpet = forms.ChoiceField(label="Brosser un tapis", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    transfer_spoon = forms.ChoiceField(label="Transvaser avec une cuillère",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    pour_rice = forms.ChoiceField(label="Verser du riz", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    pour_sand = forms.ChoiceField(label="Verser du sable", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    pour_water = forms.ChoiceField(label="Verser de l'eau", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    pour_water_glasses = forms.ChoiceField(label="Verser de l'eau dans des verres",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    clean_mirror = forms.ChoiceField(label="Nettoyer un miroir", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    polish_brass = forms.ChoiceField(label="Astiquer les cuivres", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    take_care_plants = forms.ChoiceField(label="Soigner les plantes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    chang_flower_water = forms.ChoiceField(label="Changer l'eau des fleurs",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    wash_table = forms.ChoiceField(label="Laver la table", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    wash_clothes = forms.ChoiceField(label="Laver du linge", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_care_interior = forms.CharField(label="Observations soin du milieu intérieur ",
                                                         widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))


