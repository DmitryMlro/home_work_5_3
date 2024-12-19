import string

user_text = input("Enter text to hashtag: ")
words = user_text.translate(str.maketrans('', '', string.punctuation)).split()
hashtag = "#" + "".join(word.capitalize() for word in words)
print(hashtag[:140])