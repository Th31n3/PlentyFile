""" This is my first Module. """

def opp():
    """Defining the function opp with a nested with
    statement, to write to a file, return and print
    what was written.
    """
    fil_text = 'Hope this works.'
    fil_text_1 = '\nand this too.'

    with open('touch.txt', 'w+') as fil:
        fil.write(fil_text)
        fil.write(fil_text_1)
        fil.close()
        return fil_text_1, fil_text
    print(end='\n')

def opp2():
    """ Same as the top^^^^ """

    fil_text = 'Hope this works.'
    fil_text_1 = '\nand this too.'

    with open('click.txt', 'w+') as fil_2:
        fil_2.write(fil_text)
        fil_2.write(fil_text_1)
        fil_2.close()
        return fil_text_1, fil_text
    print(end='\n')

opp()
opp2()
