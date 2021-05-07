"""This file describes the heroic adventurer Cleric1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Ralvira Aleshank"
player_name = "Mark"

# Be sure to list Primary class first
classes = ['Cleric']
levels = [5]
subclasses = ["Life Domain"]
background = "Guild Artisan"
race = "Hill Dwarf"
alignment = "Lawful good"

xp = 0
hp_max = 8 + 5 * (levels[0] - 1) + 2 * (levels[0])
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 13
dexterity = 11
constitution = 14
intelligence = 10
wisdom = 18
charisma = 10

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('insight', 'medicine', 'acrobatics', 'performance', 'perception')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ("brewer's tools",) # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, dwarvish, one of your choice."""

# Inventory
# TODO: Get yourself some money
cp = 5
sp = 8
gp = 109
ep = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ('warhammer', "light crossbow")  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "chain mail"  # Eg "light leather armor"
shield = "shield"  # Eg "shield"

equipment = """Hearth flame pendant, backpack, blanket, candles (10), tinderbox, alms box, incense (2 blocks), censer, vestments, rations (10 days), waterskin, guild letter, traveler's clothes, coin pouch, brewer's tools."""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ("thaumaturgy", "guidance", "sacred flame", "resistance", # Cleric cantrips
                   "sanctuary", "inflict wounds", "command", "guiding bolt", # Level 1 Cleric Spells
                   "augury", "prayer of healing", "hold person", # Level 2 Cleric Spells
                   "animate dead", "tongues", # Level 3 cleric spells
                   "bless", "cure wounds", # Divine spells
                   "lesser restoration", "spiritual weapon",
                   "beacon of hope", "revivify")

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = """Dargrin is a warm and friendly fellow, always willing to take time
to listen to a fellow adventurer woes."""

ideals = """Dargrin strongly believes in the power of drink to bring people
together, often offering his own brews as a sign of his good
intentions."""

bonds = """Serves Boldrei, goddess of community and home. Boldrei is concerned
about the growing discord and division in the world, which threaten
the communal bonds from which she draws power."""

flaws = """Dargrin is naive, and easily blinded to people's malevolent
intentions."""

features_and_traits = """"""
