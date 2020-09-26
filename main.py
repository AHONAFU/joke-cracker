import discord
import random

jokes = list()

jokes = ["What do you call bears with no ears? B–", "How do you make holy water? You boil the hell out of it.",
            "I was wondering why the ball was getting bigger. Then it hit me.", "What do you call a bee that can't make up its mind? A maybe.",
            "What does a house wear? A-dress. ", "What did one ocean say to the other?Nothing, they just waved.",
            "Why does it take pirates so long to learn the alphabet? Because they could spend years at C.",
            "What do diapers and politicians have in common? They both stink and need to be changed often.",
            "Why didn’t the bike want to go anywhere?Because it was two-tired!",
            "I told my doctor that I broke my arm in two places.He told me to stop going to those places.",
            "What did the right eye say to the left eye?Honestly, between you and me something smells.",
            "Can a kangaroo jump higher than a house?Of course. A house doesn’t jump at all!",
            "What’s orange and sounds like a parrot?A carrot!",
            "What do you call a dinosaur with only one eye?A Do-you-think-he-saw-us!",
            "What do you call a fish without eyes? Fsh.",
            "What do you call an alligator detective? An investi-gator.",
            "What lights up a soccer stadium? A soccer match.",
            "What's brown and sticky? A stick.", "What kind of music do planets like? Neptunes.",
            "What kind of music do planets like? Neptunes.", "Why can’t your nose be 12 inches long? Because then it would be a foot",
            "What did the tomato say to the other tomato during a race? Ketchup.", "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "What do you call a factory that sells good products? A satisfactory.",
            "What do you call shoes made of banana peels? Slippers.", "What kind of shoes do burglars wear? Sneakers.", "Why don’t eggs tell jokes? They’d crack each other up.",
            "What’s the best way to burn 1000 calories? Leave the pizza in the oven.", "What do you call a bear without any teeth?A gummy bear!",
            "I don't trust stairs. They're always up to something.", "What do you call someone with no body and no nose? Nobody knows.",
            "This graveyard looks overcrowded. People must be dying to get in.", "How many tickles does it take to make an octopus laugh? Ten tickles.",
            "Why did the math book look so sad? Because of all of its problems!", "I made a pencil with two erasers. It was pointless.",
            "I'm reading a book about anti-gravity. It's impossible to put down!", "I've got a great joke about construction, but I'm still working on it.",
            "I used to hate facial hair...but then it grew on me.", "What do you call an elephant that doesn't matter? An irrelephant.",
            "If you see a crime at an Apple Store, does that make you an iWitness?", "I'm so good at sleeping, I can do it with my eyes closed!",
            "Can February March? No, but April May!", "What’s an astronaut’s favorite part of a computer? The space bar.", "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!",
            "I love the way the Earth rotates. It makes my day.", "What do computer eat for snacks? Microchips!", "Did you hear about the kidnapping at school?It’s okay. He woke up.",
            "Why did Adele cross the road?To sing, 'Hello from the other side!'", "What’s red and bad for your teeth? A brick.",
            " Why did Mickey Mouse take a trip into space?He wanted to find Pluto!", "Why can’t you give Elsa a balloon? Because she will let it go.",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "You're not completely useless, you can always serve as an bad example.",
            "I broke my finger last week. On the other hand I'm okay.",
            "Someone stole my Microsoft Office and the're gonna pay. You have my Word.",
            "Working in a mirror factory is something I can totally see myself doing.",
            "What did the traffic light say to the car?Don’t look! I’m about to change.",
            "Why was the little strawberry crying?His mom was in a jam.",
            "Which plant rules the garden?The dande-lion.",
            "Why did the skeleton hit the party solo?He had no body to go with him.",
            "Who does a pharaoh talk to when he’s sad?His mummy, of course.",
            "What’s the most famous creature in the ocean?The star-fish.",
            "What did one egg say to the other?Eggs-cuse me, please.",
            "What do clouds wear under their shorts?Thunderpants.",
            "What do you call a man with a rubber toe? Roberto!",
            "Where did the computer go dancing? The disc-o!",
            "Why didn't the astronaut come home to his wife? He needed his space.",
            "There's no hole in your shoe? Then how'd you get your foot in it?",
            "Why don't crabs donate? Because they're shellfish.",
            "Why don't crabs donate? Because they're shellfish.",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "You're not completely useless, you can always serve as an bad example.",
            "I broke my finger last week. On the other hand I'm okay.",
            "Someone stole my Microsoft Office and the're gonna pay. You have my Word.",
            "Working in a mirror factory is something I can totally see myself doing.",
            "What did the traffic light say to the car?Don’t look! I’m about to change.",
            "Why was the little strawberry crying?His mom was in a jam.",
            "Which plant rules the garden?The dande-lion.",
            "Why did the skeleton hit the party solo?He had no body to go with him.",
            "Who does a pharaoh talk to when he’s sad?His mummy, of course.",
            "What’s the most famous creature in the ocean?The star-fish.",
            "What did one egg say to the other?Eggs-cuse me, please.",
            "What do clouds wear under their shorts?Thunderpants.",
            "What do you call a man with a rubber toe? Roberto!",
            "Where did the computer go dancing? The disc-o!",
            "Why didn't the astronaut come home to his wife? He needed his space.",
            "There's no hole in your shoe? Then how'd you get your foot in it?",
            "Why don't crabs donate? Because they're shellfish."]



client = discord.Client()

@client.event
async def on_message(message):
    ran = random.choice(jokes)
    if message.author == client.user:
        return
    if message.content.startswith("jc!joke"):
        await message.channel.send(ran)
        await on_message()
    if message.content.startswith("jc!help"):
        await message.channel.send("Use 'jc!joke' to generate random joke. Enjoy tha bot :)")


client.run('NzU5MDcyNzg0MDY3OTg1NDA4.X24Lng.zGB2Bs9WnnOdWok60Yjf9gUUBYs')

on_message()