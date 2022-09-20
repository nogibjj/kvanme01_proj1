import click
import pandas as pd

# read in csv data
df = pd.read_csv("wnbadraft.csv")

# create a random starting lineup
lineup = df.sample(n=5)

@click.command()
@click.option('--name', prompt='Enter your team name to generate a starting lineup',
              help='Enter a name.')
def team_maker(name):
    """Simple program that prints the randomly generate starting lineup."""
    print(lineup)

if __name__ == '__main__':
    team_maker()
