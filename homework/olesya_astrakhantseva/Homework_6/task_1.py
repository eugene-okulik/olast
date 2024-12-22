text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero").split()

rez = []
for word in text:
    if word[-1] in ',.':
        rez.append(word[:-1] + 'ing' + word[-1])
    else:
        rez.append(word + 'ing')

print(' '.join(rez))
