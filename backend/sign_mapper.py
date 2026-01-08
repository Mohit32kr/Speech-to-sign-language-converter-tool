SIGN_DICTIONARY = {
    "hello": "hello.mp4",
    "i": "i.mp4",
    "go": "go.mp4",
    "school": "school.mp4"
}

def map_to_signs(sentence):
    signs = []
    for word in sentence.split():
        signs.append(SIGN_DICTIONARY.get(word, "unknown.mp4"))
    return signs
