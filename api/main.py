
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from api.generator import yaml_to_excalidraw

import tempfile

app = FastAPI()

@app.post("/generate")
async def generate(file: UploadFile):
    content = await file.read()
    excalidraw_json = yaml_to_excalidraw(content.decode())

    with tempfile.NamedTemporaryFile(delete=False, suffix=".excalidraw") as f:
        f.write(excalidraw_json.encode())
        path = f.name

    return FileResponse(path, media_type="application/json", filename="output.excalidraw")
