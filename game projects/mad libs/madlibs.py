"""
Mad Libs Game

This Python program allows you to play a game of Mad Libs, a word game where players fill in the blanks of a story with different types of words (nouns, pronouns, adjectives, verbs, etc.). The program prompts the player to input specific word types and then generates a customized story by replacing the placeholders in the story template with the player's input.

Features:
- Prompts the player to input various word types to create a unique story.
- Generates a story by replacing the placeholders in the story template with the player's input.
- Provides an entertaining and creative experience with each playthrough.

How to Play:
1. Run the program and follow the instructions prompted in the console.
2. When prompted, enter a word of the requested type (noun, pronoun, adjective, verb, etc.).
3. Repeat step 2 for all the placeholders in the story template.
4. Once all the inputs are provided, the program will generate a custom Mad Libs story.
5. Enjoy reading the funny and creative story based on your inputs.
6. Play again to experience a different story by entering new words.

Tips:
- Be creative and have fun with your word choices to make the story interesting and entertaining.
- Experiment with different word types to see how they affect the overall narrative.

Author: [Olajuwon]
Date: [28-04-2022]
"""


def generate_madlib():
    noun = input('Choose a Noun: ')
    noun2 = input('Choose a second Noun: ')
    noun3 = input('Choose a third Noun: ')
    noun4 = input('Choose a fourth Noun: ')
    noun5 = input('Choose a fifth Noun: ')
    noun6 = input('Choose a sixth Noun: ')
    p_noun = input('Choose a Pronoun: ')
    P_noun2 = input('Choose a second Pronoun: ')
    p_noun3 = input('Choose a third Pronoun: ')
    adjective = input('Choose an Adjective: ')
    adjective2 = input('Choose another Adjective: ')
    verb = input('Choose a Verb: ')
    verb2 = input('Choose another Verb: ')
    verb3 = input('Choose a third Verb: ')
    verb4 = input('Choose a fourth Verb: ')
    pronoun = input('Choose a Pronoun: ')
    adverb = input('Choose an Adverb: ')
    adverb2 = input('Choose another Adverb: ')


    madlib = f"Once upon a time, in a peaceful kingdom, there was a courageous knight named {noun}. He was known throughout the land for his bravery and unwavering loyalty to his kingdom. One day, as he ventured into the enchanted forest, he stumbled upon a hidden {noun2}. Intrigued by its mysterious aura, he approached it cautiously. \
\nTo his surprise, the {noun2} emitted a soft, golden glow, revealing a magical key. The knight's curiosity got the better of him, and he decided to unlock the ancient {noun3} that stood nearby. As the {noun3} creaked open, a burst of vibrant colors enveloped the knight, transporting him to a magnificent realm filled with mythical creatures and breathtaking landscapes. \
\nIn this new world, the knight encountered {noun4}, {noun5}, and {noun6}, who were all seeking the same treasure—the legendary {noun}. Determined to claim it for his kingdom, the knight formed an alliance with his newfound companions. Together, they embarked on a perilous quest, facing treacherous {adjective} mountains, crossing turbulent rivers, and braving the scorching desert sands. \
\nTheir journey demanded courage, wit, and unwavering friendship. Along the way, they encountered numerous challenges, but their collective strength and the power of their {noun} helped them overcome every obstacle. They fought fierce {noun5} and {noun6}, using their combined skills to {verb}, {verb2}, and {verb3} their way to the treasure's elusive location. \
\nFinally, after an arduous adventure, they reached the heart of the enchanted land. The knight and his companions stood before the towering entrance of the grand castle, where the treasure awaited. With {adverb} precision, the knight inserted the magical key into the lock, turning it with a resolute {adverb2}. \
\nAs the castle gates swung open, revealing the glittering riches within, the knight couldn't help but feel an overwhelming sense of accomplishment. He had not only found the legendary {noun} but had also discovered the true meaning of friendship, courage, and perseverance. With hearts full of triumph and memories to cherish, they returned to their kingdom, forever changed by their extraordinary adventure. \
\nAnd so, the tale of the brave knight, the mythical realm, and the legendary treasure became a cherished legend, inspiring future generations to embrace their own quests and uncover the hidden treasures within themselves."

    return madlib

print(generate_madlib())

    

    
     