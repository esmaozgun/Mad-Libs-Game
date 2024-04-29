def madlibs():
    print("Welcome to the Madlibs game!")
    print("Please fill in the blanks in the story by answering the following questions.\n")

    name = input("Enter a name: ")
    verb_past = input("Enter a verb (past tense): ")
    adjective = input("Enter an adjective: ")
    noun_plural = input("Enter a plural noun: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")
    emotion = input("Enter an emotion: ")

    story = f"""
    One day, {name} was walking in {place} when they saw a {animal}. 
    The {animal} looked at {name} and said "{emotion}!". 
    Surprised, {name} {verb_past} away quickly. 
    Later, they realized they had dropped their {noun_plural} behind. 
    The {animal} was actually trying to return it, along with a piece of {food}. 
    {name} felt {adjective} and thanked the {animal} for its kindness.
    """
    
    madlibs()
