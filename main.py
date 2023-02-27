import random
import cv2
from itertools import cycle


# this is the vocabulary list that the words will be pulled from
vocabulary_list = ['active', 'adventure', 'alarm', 'annual', 'balloon', 'basket', 'beach', 'beautiful', 'believe',
                   'bicycle',
                   'bird', 'boat', 'book', 'breeze', 'bright', 'bubble', 'butterfly', 'candle', 'captain', 'carpet',
                   'celebrate',
                   'chase', 'cheerful', 'chocolate', 'climb', 'cloud', 'comfortable', 'comical', 'compassion',
                   'concert', 'confident',
                   'connect', 'conversation', 'cool', 'corn', 'costume', 'courage', 'creative', 'cuddle', 'curious',
                   'dance', 'decorate',
                   'delightful', 'determine', 'discover', 'dream', 'drizzle', 'eager', 'ear', 'enchanting', 'energy',
                   'enjoy', 'enthusiastic',
                   'explore', 'famous', 'fantastic', 'farm', 'feather', 'festival', 'flame', 'flower', 'flutter',
                   'focus', 'forest', 'fresh',
                   'friend', 'frost', 'funny', 'garden', 'gentle', 'gift', 'giggle', 'glow', 'grace', 'grand', 'grass',
                   'green', 'greet', 'grow',
                   'happy', 'harmony', 'heart', 'helpful', 'hero', 'honor', 'hug', 'humor', 'ice', 'idea', 'imagine',
                   'important', 'innocent',
                   'inspire', 'involve', 'joyful', 'jump', 'kind', 'kiss', 'laugh', 'leaf', 'learn', 'light', 'listen',
                   'lively', 'love',
                   'magic', 'marvelous', 'meadow', 'memory', 'merry', 'mischief', 'moon', 'music', 'nature', 'noble',
                   'nurture', 'ocean', 'optimistic', 'orchard', 'paint', 'parade', 'party', 'passion', 'peaceful',
                   'play',
                   'pleasure', 'pop', 'power', 'pretty', 'pride', 'proud', 'puppy', 'puzzle', 'rain', 'rainbow',
                   'rejoice',
                   'relax', 'renew', 'rescue', 'rest', 'reward', 'rhythm', 'ride', 'river', 'romantic', 'sail',
                   'satisfy', 'scary',
                   'sculpture', 'season', 'secret', 'serene', 'share', 'shimmer', 'shiver', 'silly', 'simplicity',
                   'smile', 'song',
                   'sparkle', 'spectacular', 'spirit', 'splendid', 'sport', 'sprinkle', 'star', 'storybook',
                   'strawberry', 'succeed',
                   'sunny', 'surprise', 'swim', 'tasty', 'team', 'thankful', 'thoughtful', 'thrill', 'thunder', 'tidy',
                   'together',
                   'touch', 'treasure', 'treat', 'triumph', 'trust', 'twinkle', 'vacation', 'valiant', 'value',
                   'venture', 'victory',
                   'view', 'visit', 'vivid', 'wander', 'warm', 'wave', 'whimsical', 'whistle', 'wild']

# this dictionary hold the file paths that lead to the ASL hand shape images
asl_letters = {
    'a': 'images/a.png',
    'b': 'images/b.png',
    'c': 'images/c.png',
    'd': 'images/d.png',
    'e': 'images/e.png',
    'f': 'images/f.png',
    'g': 'images/g.png',
    'h': 'images/h.png',
    'i': 'images/i.png',
    'j': 'images/j.png',
    'k': 'images/k.png',
    'l': 'images/l.png',
    'm': 'images/m.png',
    'n': 'images/n.png',
    'o': 'images/o.png',
    'p': 'images/p.png',
    'q': 'images/q.png',
    'r': 'images/r.png',
    's': 'images/s.png',
    't': 'images/t.png',
    'u': 'images/u.png',
    'v': 'images/v.png',
    'w': 'images/w.png',
    'x': 'images/x.png',
    'y': 'images/y.png',
    'z': 'images/z.png',

}

# this variable holds the current word that is being Displayed in the UI
current_word = random.choice(vocabulary_list)


# this function should convert the letters of the vocabulry word into a list of file paths
def collect_file_paths():
    file_list = []
    for char in current_word:
        formatted_file_name = f"{asl_letters[char]}"
        file_list.append(formatted_file_name)
    return file_list


file_path_list = collect_file_paths()


# This action should display the current word in ASL finger spelling

def que_word(file_path_list):
    # this function should receive a word that has been split into chars.
    # those chars should be used in a key value style to retrieve the desired images
    letter_list = file_path_list
    letters_shown = 0
    letters_to_show = len(letter_list)

    for (image_filename) in cycle(letter_list):
        image = cv2.imread(image_filename, 0)
        cv2.imshow('image', image)

        # Pause here 1 seconds.
        k = cv2.waitKey(1000)

        #
        letters_shown += 1
        if letters_shown == letters_to_show:
            cv2.destroyAllWindows()
            break


que_word(file_path_list)


# this function will promt the user to spell the that was fingerspelled to them in english
def get_user_answer():
    user_guess = input("spell the word you saw: ")
    return user_guess


user_answer = get_user_answer()

print(user_answer)


# This function will check the users answer against the current word
def check_answer(user_answer, current_word):
    if user_answer == current_word:
        print("Booyah!")
        print("correct")
    else:
        print("incorect")
        print(f"the corect word was {current_word}")


check_answer(current_word=current_word, user_answer=user_answer)
