import random
animals = ["elephant", "bear", "cheetah", "giraffe", "wolf", "tiger", "penguin",
                        "rabbit", "lion", "monkey", "rhinoceros", "sheep", "kangaroo", "zebra",
           "jaguar", "flamingo", "sloth", "horse", "dog", "cat", "bat", "camel", "mouse",
           "raccoon", "squirrel", "chimpanzee", "koala", "hedgehog", "hippopotamus"]

fruits = ["apple", "banana", "grapes", "mango", "lime", "watermelon", "strawberry",
                       "guava", "orange", "papaya", "pear", "peach", "pomegranate", "jackfruit",
          "apricot", "melon", "cherry", "blackberry", "blueberry", "durian", "dragonfruit",
          "grapefruit", "figs", "kiwi", "persimmon", "pineapple", "plum"]

stationary = ["pencil", "eraser", "sharpener", "envelope", "gluestick", "paper",
                           "stapler", "folder", "marker", "calculator", "notebook", "scissors",
              "mechanical-pencil", "ballpoint-pen", "thumbtacks", "correction-tape", "graphing-paper",
              "colored-paper", "staple-pins", "post-it-notes", "duct-tape", "protractor"]


def choose_random():
    word_list = animals + fruits + stationary
    random_word = random.choice(word_list)
    return random_word

