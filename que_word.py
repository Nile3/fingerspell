from itertools import cycle
import cv2

def que_word(file_path_list):
    # this function should recive a word that has been split into chars.
    # those chars should be used in a key vaule style to reteave the disired images
    letter_list = [file_path_list]
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
            break