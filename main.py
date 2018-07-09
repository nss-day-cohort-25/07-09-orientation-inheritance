# instantiate a new Dog and print out the results of making it speak
from dog import Dog
from pet import Pet

# Create an instance of the Dog class
aussie_mix = Dog("Australian Shepherd mix")
# print(f"What's that girl? {aussie_mix.speak()} Timmy's in a well? Oh no!")
# print("a dog instance", aussie_mix)

# Create an instance of the Pet class and compose the Dog instance into it by adding the dog as a property of the new Pet
murph = Pet("Murphis", aussie_mix)

# Add my family as owners by calling murph's set_owner method
murph.set_owner("The Sheps", "555-555-1234")

# Print a human-readable output thanks to our the __str__ method we defined in Pet
print(murph)
