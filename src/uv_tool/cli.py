
import typer
import requests
from pathlib import Path

app = typer.Typer()

@app.command()
def generate(file: Path=typer.Argument(..., help="YAML or Markdown file"):
    """Send YAML/Markdown file to Excalidraw generator container."""
    with open(file, "rb") as f:
        res = requests.post("http://localhost:8000/generate", files={"file": f})
    out = Path("output.excalidraw")
    out.write_bytes(res.content)
    typer.echo(f"✅ File saved as: {out.resolve()}")
