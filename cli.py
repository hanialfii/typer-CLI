import typer

app= typer.Typer()
@app.command()
def greeting(name:str):
    print(f"hello {name}👋")

if __name__ == "__main__":
    app()
