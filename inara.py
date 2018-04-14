name = 'Inara Serradon'
character_class = 'wizard'
player_name = 'Mark'
background = "Acolyte"
race = "High-Elf"
level = 5
alignment = "Chaotic good"
xp = 6500
hp_max = 24

# Ability Scores
strength = 10
dexterity = 15
constitution = 14
intelligence = 18
wisdom = 12
charisma = 8
skill_proficiencies = [
    'arcana',
    'insight',
    'investigation',
    'perception',
    'religion',
]

# Proficiencies and languages
languages = "Common, Elvish, Draconic, Dwarvish, Goblin."

# Inventory
cp = 596
sp = 365
ep = 18
gp = 125
pp = 0
weapons = ('shortsword', 'longsword')
equipment = (
    """Gallon of ale, red-brand's cloak, shortsword, longsword, jar of
    salt, vodka (500mL), potion of vitality, wand of magic missiles
    (6/7), component pouch, spellbook, backpack, bottle of ink, ink
    pen, 10 sheets of parchment, small knife, tome of historical lore,
    holy symbol, prayer book, set of common clothes, pouch.""")

# List of known spells
spells = (
    # Start spells
    'mage hand', 'prestidigitation', 'ray of frost',
    'shocking grasp', 'burning hands', 'detect magic',
    'mage armor', 'magic missile', 'shield', 'sleep',
    # Learned at lvl 2
    'false life', 'ray of sickness',
    # Learned at lvl 3
    'blindness deafness', 'chromatic orb',
    # Learned at lvl 4
    'chill touch', "melf's acid arrow", 'phantasmal force',
    # Learned at lvl 5
    'animate dead', 'vampiric touch',
)
# Which spells have been prepared (not including cantrips)
spells_prepared = ('blindness deafness', 'false life', 'mage armor',
                   'ray of sickness', 'melfs acid arrow',
                   'chill touch', 'animate dead', 'vampiric touch',
                   'burning hands')

# Backstory
personality_traits = """I use polysyllabic words that convey the impression of
erudition. Also, I’ve spent so long in the temple that I have little
experience dealing with people on a casual basis."""

ideals = """Knowledge. The path to power and self- improvement is through
knowledge."""

bonds = """The tome I carry with me is the record of my life’s work so far,
and no vault is secure enough to keep it safe."""

flaws = """I’ll do just about anything to uncover historical secrets that
would add to my research."""

features_and_traits = (
    """Spellcasting Ability: Intelligence is your spellcasting ability for
    your spells. The saving throw DC to resist a spell you cast is
    13. Your attack bonus when you make an attack with a spell is
    +5. See the rulebook for rules on casting your spells.
    
    Arcane Recovery: You can regain some of your magical energy by
    studying your spellbook. Once per day during a short rest, you can
    choose to recover expended spell slots with a combined level equal
    to or less than half your wizard level (rounded up).
    
    Darkvision: You see in dim light within a 60-foot radius of you as
    if it were bright light, and in darkness in that radius as if it
    were dim light. You can’t discern color in darkness, only shades
    of gray.
    
    Fey Ancestry: You have advantage on saving throws against being
    charmed, and magic can’t put you to sleep.
    
    Trance: Elves don’t need to sleep. They meditate deeply, remaining
    semiconscious, for 4 hours a day and gain the same benefit a human
    does from 8 hours of sleep.
    
    Shelter of the Faithful: As a servant of Oghma, you command the
    respect of those who share your faith, and you can perform the
    rites of Oghma. You and your companions can expect to receive free
    healing and care at a temple, shrine, or other established
    presence of Oghma’s faith. Those who share your religion will
    support you (and only you) at a modest lifestyle. You also have
    ties to the temple of Oghma in Neverwinter, where you have a
    residence. When you are in Neverwinter, you can call upon the
    priests there for assistance that won’t endanger them.""")
