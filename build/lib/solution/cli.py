from .skcript import Main
import click

@click.command()
@click.option('-s')
@click.option('-w')
def magic(s,w):
    try:
        output = Main().magic(s,w)
        if output:
            print ('Yes, "{word}" can be created.'.format(word=w))
        else:
            print ('No, "{word}" can be created.'.format(word=w))
    except TypeError:
        print ("Missing parameter -s or -w")

@click.command()
@click.option('-s')
def longest(s):
    try:
        output = Main().longest(s)
        print ('The longest word that can be formed with "{s}" is "{word}"'.format(s=s,word=output))
    except TypeError:
        print ("Requires -s parameter")
