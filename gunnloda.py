"""This file describes the heroic adventurer Gunnloda Wavesplitter.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.5.0"

name = 'Gunnloda Wavesplitter'
character_class = 'Druid'
player_name = 'Mark'
background = "Sailor"
race = "Hill Dwarf"
level = 3
alignment = "Lawful good"
xp = 900
hp_max = 30

# Ability Scores
strength = 10
dexterity = 14
constitution = 17
intelligence = 11
wisdom = 17
charisma = 13
skill_proficiencies = ('nature', 'insight', 'athletics', 'perception')

# Proficiencies and languages
proficiencies_extra = ("brewer's supplies", "navigator's tools", "vehicles (water)")
languages = "Common, Dwarvish, Druidic"

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 75
pp = 0

weapons = ('scimitar', 'quarterstaff') # Example: ('shortsword', 'longsword')
armor = "Leather armor" # Eg "light leather armor"
shield = "wooden shield" # Eg "shield"

equipment = """ash quarterstaff (druidic focus), backpack, bedroll, mess kit (2),
tinderbox, rations (9 days), waterskin, 50 feet of hemp rope, rolling
pin, a belaying pin (club), 50 feet of silk rope, a book that tells
the story of a hero ridding the world of undead evil with the help of
a magic relic (the last chapter is missing), a set of common dothes, a
belt pouch, cloak of protection, potion of healing, chain shirt, flask
of alchemist fire, lantern, thieves tools, spellbook, gold ring, blank
book, moss agate (2), a black cloth, candles (2)."""

attacks_and_spellcasting = ""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
# spells = (
#     # Cantrips 
#     'shillelagh', 'poison spray', 'druidcraft',
#     # Prepared spells
#     'speak with animals', 'entangle', 'cure wounds', 'create or destroy water')
# Which spells have been prepared (not including cantrips)
spells_prepared = (
    # Cantrips
    'shillelagh', 'poison spray', 'druidcraft',
    # First level spells
    'charm person', 'faerie fire', 'thunderwave',
    # Second level spells
    'locate animals or plants', 'flaming sphere',
)
wild_shapes = ('rat', 'spider', 'swarm of rats', 'wolf')

# Backstory
personality_traits = """I am quick to accept new friends, but quick to judge and will
easily punish trangressions. My true friends know they can rely on my
no matter what. You will not struggle to know which category you fall
into."""

ideals = """I am driven to restore the life to my home city of Ironforge. A
rift formed near my town while I was delivering ore, and an undead
army was unleashed on my town, killing all my kin. I heard rumors of a
magic relic that can banish the rift and allow me to restore Ironforge
to its former glory. Once restored, I will buy my own ship, find a
crew, and sail the ocean under my own terms."""

bonds = """I am especially eager to commune with animals. I often find
humanoids fickle and boring, though will always be polite. I mistrust
those that seek to employ me, due to a series of trade deals that went
south when the other side failed to uphold their end."""

flaws = """I am impatient with those that are slow to understand. I am also
quick to judge the strong dullard as not worthy of my
acquantance. Despite my calculating nature, I cannot resist a tempting
gamble, even if the odds are not in my favor."""

features_and_traits = """4'0" 140 lbs. 55 years old

**Darkvision.**

**Dwarven Resilience.** You have advantage on saving
throws against poison, and you have resistance against poison
damage.

**Stoneeunning.** Whenever you make an Intelligence
(History) check related to the origin of stonework, you
are considered proficient in the History skill and add
double your proficiency bonus to the check, instead of
your normal proficiency bonus.

**Dwarven Toughness.** Your hit point maximum
increases by 1, and it increases by 1 every time you
gain a leveI.

**Ship's Passage.** When you need to, you can secure free passage on a
sailing ship for yourself and your adventuring companions. You might
sail on the ship you served on, or another ship you have good
relations with (perhaps one captained bye former crewmate). Because
you're calling in a favor, you can't be certain of a schedule or route
that wiII meet your every need. Your Dungeon Master will determine how
long it takes to get where you need to go. In return for your free
passage, you and your companions are expected to assist the crew
during the voyage."""

