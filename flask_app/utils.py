def beutify(name):
    name = name.replace("files/", "")
    name = name.replace(".pdf", "")
    words = name.split("-")
    camel_case = ' '.join(word.capitalize() for word in words[0:])
    return camel_case
