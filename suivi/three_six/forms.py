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

    """ EXERCICES PRELIMINAIRES """

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

    """ SOIN DU MILEU INTERIEUR """

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

    """ SOIN DE LA PERSONNE"""

    frame_press_studs = forms.ChoiceField(label="Cadre à boutons pressions",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_big_studs = forms.ChoiceField(label="Cadre à gros boutons", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_small_studs = forms.ChoiceField(label="Cadre à petits boutons",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_slide = forms.ChoiceField(label="Cadre à glissière", choices=LEVEL_CHOICES,
                                          widget=forms.RadioSelect())
    frame_staple = forms.ChoiceField(label="Cadre à agrafes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_loop = forms.ChoiceField(label="Cadre à boucles", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_safety_pin = forms.ChoiceField(label="Cadre à épingles à nourrice",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_node = forms.ChoiceField(label="Cadre à noeuds", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    frame_lacing = forms.ChoiceField(label="Cadre à laçage", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    wash_hands = forms.ChoiceField(label="Se laver les mains", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    shine_shoes = forms.ChoiceField(label="Cirer ses chaussures", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sew = forms.ChoiceField(label="Coudre", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_personal_care = forms.CharField(label="Observations soin de la personne",
                                                 widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ JEUX COLLECTIFS"""

    walk_line = forms.ChoiceField(label="Marcher sur la ligne", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    lesson_silence = forms.ChoiceField(label="Leçon de silence", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_collective_games = forms.CharField(label="Observations jeux collectifs",
                                                    widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    class Meta:
        model = PracticalLife


class SensoryMaterialForm(forms.Form):
    LEVEL_CHOICES = (
        ('PRESENTED', 'Présentée'),
        ('PROCESSING', "En cours d'acquisition"),
        ('ACQUIRED', 'Acquise')
    )

    cylindrical_sockets_1 = forms.ChoiceField(label="Emboitements cylindriques 1",
                                              choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    cylindrical_sockets_2 = forms.ChoiceField(label="Emboitements cylindriques 2", choices=LEVEL_CHOICES,
                                              widget=forms.RadioSelect())
    cylindrical_sockets_3 = forms.ChoiceField(label="Emboitements cylindriques 3", choices=LEVEL_CHOICES,
                                              widget=forms.RadioSelect())
    cylindrical_sockets_4 = forms.ChoiceField(label="Emboitements cylindriques 4", choices=LEVEL_CHOICES,
                                              widget=forms.RadioSelect())
    pink_tower = forms.ChoiceField(label="La tour rose", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    brown_staircase = forms.ChoiceField(label="L'escalier marron", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    red_bars = forms.ChoiceField(label="Les barres rouges", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    color_table_1 = forms.ChoiceField(label="Les tables des couleurs 1", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    color_table_2 = forms.ChoiceField(label="Les tables des couleurs 2", choices=LEVEL_CHOICES,
                                      widget=forms.RadioSelect())
    color_table_3 = forms.ChoiceField(label="Les tables des couleurs 3", choices=LEVEL_CHOICES,
                                      widget=forms.RadioSelect())
    geometry_tray = forms.ChoiceField(label="Le cabinet de géométrie/plateau", choices=LEVEL_CHOICES,
                                      widget=forms.RadioSelect())
    geometry_drawers = forms.ChoiceField(label="Le cabinet de géométrie/tiroirs", choices=LEVEL_CHOICES,
                                         widget=forms.RadioSelect())
    geometry_maps = forms.ChoiceField(label="Le cabinet de géométrie/cartes", choices=LEVEL_CHOICES,
                                      widget=forms.RadioSelect())
    smooth_rough = forms.ChoiceField(label="Lisse et rugeux", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    smooth_rough_table = forms.ChoiceField(label="Lisse et rugeux : les tablettes",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    fabrics = forms.ChoiceField(label="Les étoffes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    geometric_solids = forms.ChoiceField(label="Les solides géométriques",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    mystery_bag = forms.ChoiceField(label="Le sac à mystères", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    stereognostic_bag = forms.ChoiceField(label="Les sacs stéréognostiques",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    seed_sorting = forms.ChoiceField(label="Le tri des graines", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    baryque_tablets = forms.ChoiceField(label="Les tablettes baryques",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    noise_boxes = forms.ChoiceField(label="Les boites à bruits", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    flavours = forms.ChoiceField(label="Les saveurs", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    thermal_bottles = forms.ChoiceField(label="Les bouteilles thermiques",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    thermal_tablets = forms.ChoiceField(label="Les tablettes thermiques",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_1 = forms.ChoiceField(label="Les triangles constructeurs 1",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_2 = forms.ChoiceField(label="Les triangles constructeurs 2",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_3 = forms.ChoiceField(label="Les triangles constructeurs 3",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_4 = forms.ChoiceField(label="Les triangles constructeurs 4",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_5 = forms.ChoiceField(label="Les triangles constructeurs 5",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    constructor_triangles_6 = forms.ChoiceField(label="Les triangles constructeurs 6",
                                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    superimposed_figures = forms.ChoiceField(label="Les figures superposées",
                                             choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    binomial_cube = forms.ChoiceField(label="Le cube du binôme", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    trinomial_cube = forms.ChoiceField(label="Le cube du trinôme", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    pythagore_table = forms.ChoiceField(label="La table de Pythagore", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    colored_cylinders = forms.ChoiceField(label="Les cylindres de couleur", choices=LEVEL_CHOICES,
                                          widget=forms.RadioSelect())
    botanical_tray = forms.ChoiceField(label="Le cabinet de botaniques/plateau", choices=LEVEL_CHOICES,
                                       widget=forms.RadioSelect())
    botanical_maps = forms.ChoiceField(label="Le cabinet de botaniques/cartes", choices=LEVEL_CHOICES,
                                       widget=forms.RadioSelect())
    bells = forms.ChoiceField(label="Les clochettes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    smooth_rough_globe = forms.ChoiceField(label="Le globe lisse et rugeux",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    planisphere = forms.ChoiceField(label="Le planisphère", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    puzzles_continents = forms.ChoiceField(label="Les puzzles des continents",
                                           choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    flags = forms.ChoiceField(label="Les drapeaux", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    flags_1 = forms.ChoiceField(label="Les drapeaux : nomenclature classifiée",
                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    land_water = forms.ChoiceField(label="Les contrastes de la terre et de l'eau",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    europe = forms.ChoiceField(label="La carte de l'Europe", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    art = forms.ChoiceField(label="Introduction à l'art", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sink_float = forms.ChoiceField(label="Les objects qui coulent, qui flottent",
                                   choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    horizontal_water = forms.ChoiceField(label="l'eau qui s'équilibre sur un plan horizontal",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    north = forms.ChoiceField(label="La direction du nord", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    water_air_1 = forms.ChoiceField(label="L'eau et l'air 1", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    water_air_2 = forms.ChoiceField(label="L'eau et l'air 3", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    water_air_3 = forms.ChoiceField(label="L'eau et l'air 3", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    electricity = forms.ChoiceField(label="L'électricité", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    magnets_1 = forms.ChoiceField(label="Les aimants 1", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    magnets_2 = forms.ChoiceField(label="Les aimants 2", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    roman_arch = forms.ChoiceField(label="L'arche romane", choices=LEVEL_CHOICES, widget=forms.RadioSelect())

    observations = forms.CharField(label="Observations", widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    class Meta:
        model = SensoryMaterial

