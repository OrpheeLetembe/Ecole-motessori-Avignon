from django import forms
from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter
from students.models import Students


class StudentForm(forms.ModelForm):
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
        fields = ['image', 'first_name', 'last_name', 'date_of_birth', 'reference_phone', 'ambiance']


class PracticalLifeForm(forms.ModelForm):
    LEVEL_CHOICES = (
        ('Présentée', 'Présentée'),
        ("En cours d'acquisition", "En cours d'acquisition"),
        ('Acquise', 'Acquise')

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
        exclude = ('student',)


class SensoryMaterialForm(forms.Form):
    LEVEL_CHOICES = (
        ('Présentée', 'Présentée'),
        ("En cours d'acquisition", "En cours d'acquisition"),
        ('Acquise', 'Acquise')

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
    smooth_rough = forms.ChoiceField(label="Lisse et rugueux", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    smooth_rough_table = forms.ChoiceField(label="Lisse et rugueux : les tablettes",
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
    smooth_rough_globe = forms.ChoiceField(label="Le globe lisse et rugueux",
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
        fields = '__all__'


class MathForm(forms.Form):
    LEVEL_CHOICES = (
        ('Présentée', 'Présentée'),
        ("En cours d'acquisition", "En cours d'acquisition"),
        ('Acquise', 'Acquise')

    )

    """ GROUPE 1 NUMERATION DE 1 A 10"""

    number_bars = forms.ChoiceField(label="Les barres numériques", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    rough_numbers = forms.ChoiceField(label="Les chiffres rugueux", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    bars_numbers = forms.ChoiceField(label="Association barres et chiffres",
                                     choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    spindles = forms.ChoiceField(label="Les fuseaux", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    token_game = forms.ChoiceField(label="Le jeu des jetons", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    memory_game = forms.ChoiceField(label="Le jeu de mémoire", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_1 = forms.CharField(label="Observations groupe 1 : numérotation 1 a 10",
                                                 widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ GROUPE 2 INTRODUCTION AU SYSTEME DECIMAL ET AUX OPERATIONS"""

    sd_quantity = forms.ChoiceField(label="SD : 1ère présentation, quantités",
                                    choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sd_symbol = forms.ChoiceField(label="SD : 1ère présentation, symboles",
                                    choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sd_number = forms.ChoiceField(label="SD : formation des grands nombres",
                                  choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    add_sd = forms.ChoiceField(label="Addition statique/dynamique",
                               choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sous_sd = forms.ChoiceField(label="Soustraction statique/dynamique",
                                choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    multi_sd = forms.ChoiceField(label="Multiplication statique/dynamique",
                                 choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    div_sd = forms.ChoiceField(label="Division statique/dynamique", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    stamps_add = forms.ChoiceField(label="Les timbres : addition S/D", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    stamps_sous = forms.ChoiceField(label="Les timbres : soustraction S/D", choices=LEVEL_CHOICES,
                                    widget=forms.RadioSelect())
    stamps_multi = forms.ChoiceField(label="Les timbres : multiplication S/D", choices=LEVEL_CHOICES,
                                     widget=forms.RadioSelect())
    stamps_div = forms.ChoiceField(label="Les timbres : division S/D", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    points_tables = forms.ChoiceField(label="La table des points", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_2 = forms.CharField(label="Observations groupe 2 : "
                                                 "introduction au système décimal et aux opérations",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ GROUPE 3 NUMERATION DE 11 A L'INFINI """

    quantity_11_19 = forms.ChoiceField(label="11 à 19 : les quantités",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    seguin_11_19 = forms.ChoiceField(label="11 à 19 : la 1ère table de Seguin",
                                     choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    quantity_symbol_11_19 = forms.ChoiceField(label="11 à 19 : asso quantités symboles",
                                              choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    seguin_11_99 = forms.ChoiceField(label="11 à 19 : asso quantités symboles",
                                     choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    chain_100 = forms.ChoiceField(label="La chaîne de 100", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    chain_1000 = forms.ChoiceField(label="La chaîne de 1000", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    chain_square = forms.ChoiceField(label="La chaîne du carré", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    chain_cube = forms.ChoiceField(label="La chaîne du cube", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_3 = forms.CharField(label="Observations groupe 3 : ""numération de 11 à l'infini",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ GROUPE 4 11 A 19 ASSOCIATION QUANTITES SYMBOLES"""

    snake_game_add = forms.ChoiceField(label="Le jeu du serpent de l'addition",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    add_table = forms.ChoiceField(label="Le tableau de l'addition", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    memo_add_table = forms.ChoiceField(label="Tables mémo addition 1, 2, 3, 4",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    snake_game_sous = forms.ChoiceField(label="Le jeu du serpent de la soustraction",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sous_table = forms.ChoiceField(label="Le tableau de la soustraction",
                                   choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    emo_sous_table = forms.ChoiceField(label="Tables mémo soustraction 1, 2",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    memo_multi = forms.ChoiceField(label="Mémo multiplication : perles couleur",
                                   choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    multi_table = forms.ChoiceField(label="Le tableau de la multiplication",
                                    choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    memo_multi_table = forms.ChoiceField(label="Tables mémo multiplication 1, 2, 3",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    div_table = forms.ChoiceField(label="Le tableau de la division", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    memo_div_table = forms.ChoiceField(label="Tables mémo division 1, 2",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_4 = forms.CharField(label="Observations groupe 4 : 11 a 19 : association quantités symboles",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ GROUPE 5 LE PASSAGE A L'ABSTRACTION """

    little_abacus = forms.ChoiceField(label="Petit boulier : présentation",
                                      choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    little_abacus_add_sd = forms.ChoiceField(label="Petit boulier : addition S/D",
                                             choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    little_abacus_sous_sd = forms.ChoiceField(label="Petit boulier : soustraction S/D",
                                              choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    little_abacus_multi_sd = forms.ChoiceField(label="Petit boulier : multiplication S/D",
                                               choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    hierarchies_quantity_symbol = forms.ChoiceField(label="Hiérarchies : quantités, symboles, association",
                                                    choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    large_abacus = forms.ChoiceField(label="Grand boulier : présentation",
                                     choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    large_add_sd = forms.ChoiceField(label="Grand boulier : addition S/D",
                                     choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    large_sous_sd = forms.ChoiceField(label="Grand boulier : soustraction S/D",
                                      choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    large_multi_sd = forms.ChoiceField(label="Grand boulier : multiplication S/D",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    div_tube = forms.ChoiceField(label="La grande division avec tubes",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_5 = forms.CharField(label="Observations groupe 5 : le passage à l'abstraction",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ GROUPE 6 LES FRACTIONS """

    div_name = forms.ChoiceField(label="Les nommer", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    div_write = forms.ChoiceField(label="Les écrire", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    find_equivalences = forms.ChoiceField(label="Rechercher les équivalences",
                                          choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    make_operations = forms.ChoiceField(label="Faire des opérations", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_group_6 = forms.CharField(label="Observations groupe 6 : les fractions",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    class Meta:
        model = Math
        fields = '__all__'


class LangageForm(forms.Form):
    LEVEL_CHOICES = (
        ('Présentée', 'Présentée'),
        ("En cours d'acquisition", "En cours d'acquisition"),
        ('Acquise', 'Acquise')

    )

    """ ENRICHISSEMENT DU VOCABULAIRE"""

    img_before_read = forms.ChoiceField(label="Images classifiées avant lecture",
                                        choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    stories_told = forms.ChoiceField(label="Histoires racontées", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    libraries = forms.ChoiceField(label="Bibliothèques", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    farm = forms.ChoiceField(label="La ferme", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    nomenclature_before_read = forms.ChoiceField(label="Nomenclature avant lecture",
                                                 choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    question_game = forms.ChoiceField(label="Le jeu des questions", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_1 = forms.CharField(label="Observations Enrichissement du vocabulaire",
                                           widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ PREPARATION ECRITURE ET LECTURE """

    sound_analysis_game = forms.ChoiceField(label="Le jeu d'analyse des sons",
                                            choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    rough_letters_diagrams = forms.ChoiceField(label="Les lettres et diagrammes rugeux",
                                               choices=LEVEL_CHOICES, widget=forms.RadioSelect())

    design_shapes = forms.ChoiceField(label="Les formes à dessins", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    mobile_alphabets_1_2 = forms.ChoiceField(label="Les alphabets mobiles 1 & 2",
                                             choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    slates = forms.ChoiceField(label="Les ardoises", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    write_different_media = forms.ChoiceField(label="Ecrire : différents supports",
                                              choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    box_objects_1 = forms.ChoiceField(label="La 1ère boite d'objets", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    box_objects_2 = forms.ChoiceField(label="La 2ème boite d'objets", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    homophony_covers = forms.ChoiceField(label="Les pochettes d'homophonies",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    img_after_read = forms.ChoiceField(label="Images classifiées après lecture",
                                       choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    read_different_media = forms.ChoiceField(label="Lire : différents supports",
                                             choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_2 = forms.CharField(label="Observations préparation écriture et lecture",
                                     widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ LA NATURE DES MOTS """

    article = forms.ChoiceField(label="L'article", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    adjective = forms.ChoiceField(label="L'adjectif", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    logical_adjective_game = forms.ChoiceField(label="Le jeu de l'adjectif logique",
                                               choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    detective_game = forms.ChoiceField(label="Le jeu du détective", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    conjunction = forms.ChoiceField(label="La conjonction", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    preposition = forms.ChoiceField(label="La préposition", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    logical_preposition_game = forms.ChoiceField(label="Le jeu de la préposition logique",
                                                 choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    verb = forms.ChoiceField(label="Le verbe : différents aspects", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    adverb = forms.ChoiceField(label="L'adverbe", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    logical_adverb_game = forms.ChoiceField(label="Le jeu de l'adverbe logique",
                                            choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    orders_123 = forms.ChoiceField(label="Les ordres 1, 2, 3", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_3 = forms.CharField(label="Observations la nature des mots",
                                     widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ANALYSE DE LA LECTURE"""

    sentence_analysis_1 = forms.ChoiceField(label="Analyse de la phrase, stade 1",
                                            choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sentence_analysis_2 = forms.ChoiceField(label="Analyse de la phrase, stade 2",
                                            choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    observations_4 = forms.CharField(label="Observations analyse de la lecture",
                                     widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    """ MUSIQUE """

    name_bells = forms.ChoiceField(label="Le nom des clochettes", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    sharp_flat = forms.ChoiceField(label="Dièse et bémol", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    read_write_music = forms.ChoiceField(label="Lecture et écriture musicale",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    bass_clef = forms.ChoiceField(label="La clé de Fa", choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    read_sheet_music = forms.ChoiceField(label="Lecture de partitions",
                                         choices=LEVEL_CHOICES, widget=forms.RadioSelect())

    observations_5 = forms.CharField(label="Observations musique",
                                     widget=forms.Textarea(attrs={"rows": 5, "cols": 81}))

    class Meta:
        model = Langage
        fields = '__all__'


class LetterForm(forms.Form):
    CHOICES = (
        ('Présentée', 'Présentée'),
        ('Entendue', "Entendue"),
        ('Lue', 'Lue'),
        ('Ecrite', 'Ecrite')

    )
    letter_a = forms.ChoiceField(label="A", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_b = forms.ChoiceField(label="B", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_c = forms.ChoiceField(label="C", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_d = forms.ChoiceField(label="D", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_e = forms.ChoiceField(label="E", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_f = forms.ChoiceField(label="F", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_g = forms.ChoiceField(label="G", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_h = forms.ChoiceField(label="H", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_i = forms.ChoiceField(label="I", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_j = forms.ChoiceField(label="J", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_k = forms.ChoiceField(label="K", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_l = forms.ChoiceField(label="L", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_m = forms.ChoiceField(label="M", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_n = forms.ChoiceField(label="N", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_o = forms.ChoiceField(label="O", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_p = forms.ChoiceField(label="P", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_q = forms.ChoiceField(label="Q", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_r = forms.ChoiceField(label="R", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_s = forms.ChoiceField(label="S", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_t = forms.ChoiceField(label="T", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_u = forms.ChoiceField(label="U", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_v = forms.ChoiceField(label="V", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_w = forms.ChoiceField(label="W", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_x = forms.ChoiceField(label="X", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_y = forms.ChoiceField(label="Y", choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    letter_z = forms.ChoiceField(label="Z", choices=CHOICES, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Letter
        exclude = ('student',)







