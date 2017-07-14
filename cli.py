from skcript import Main
import click

@click.command()
@click.option('-s')
@click.option('-w')
def magic(s,w):
	output = Main().magic(s,w)
	if output:
		print ('Yes, "{word}" can be created.'.format(word=w))
	else:
		print ('No, "{word}" can be created.'.format(word=w))


@click.command()
@click.option('-s')
def longest(s):
	output = Main().longest(s)
	print ('The longest word in enable1.txt that can be formed with "{s}" is "{word}"'.format(s=s,word=output))
	