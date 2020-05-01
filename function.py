##
## Personal Project made by:
## killian.fleury@epitech.eu
##
## Project Description:
## lib of function
##
message = ["bonjour", "salut", "yo", "hey"]


def reformat_user(author):
    author = str(author)
    list = []
    for i in range(0, len(author)):
        if author[i] == '#':
            break
        list.append(author[i])
    list = ''.join(list)
    return list
