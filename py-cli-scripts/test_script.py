import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yello]")

@app.command("hello")
def sample_func(name):
    rprint("[red bold]Hello[/red bold]", name)



if __name__ == "__main__":
    app()
