from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from api.generator import yaml_to_excalidraw
import tempfile
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/generate")
async def generate(file: UploadFile, render: str = Form("none")):
    """
    Converts a YAML/Markdown file to .excalidraw JSON.
    Optional: set render=png or render=svg to return a rendered image instead.
    """
    content = await file.read()
    excalidraw_json = yaml_to_excalidraw(content.decode())

    with tempfile.NamedTemporaryFile(delete=False, suffix=".excalidraw") as f:
        f.write(excalidraw_json.encode())
        excalidraw_path = f.name

    if render.lower() in {"png", "svg"}:
        rendered_path = excalidraw_path.replace(".excalidraw", f".{render}")
        
        subprocess_result = subprocess.run([
            "excalidraw_export",
            "--input", excalidraw_path,
            "--output", rendered_path,
            f"--{render}"
        ], capture_output=True, text=True)

        logging.info("STDOUT: %s", subprocess_result.stdout)
        logging.info("STDERR: %s", subprocess_result.stderr)
        subprocess_result.check_returncode()

        mime = "image/png" if render == "png" else "image/svg+xml"
        return FileResponse(rendered_path, media_type=mime, filename=f"output.{render}")

    # Default: return .excalidraw
    return FileResponse(excalidraw_path, media_type="application/json", filename="output.excalidraw")
