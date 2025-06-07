
import yaml
import json

def yaml_to_excalidraw(yaml_text: str) -> str:
    data = yaml.safe_load(yaml_text)

    elements = []
    for i, row in enumerate(data.get("rows", [])):
        text = row.get("text", "")
        elements.append({
            "type": "text",
            "version": 1,
            "versionNonce": 123,
            "isDeleted": False,
            "id": f"text-{i}",
            "fillStyle": "hachure",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "angle": 0,
            "x": 100,
            "y": 100 + i * 50,
            "width": 100,
            "height": 20,
            "seed": 123,
            "groupIds": [],
            "text": text,
            "fontSize": 20,
            "fontFamily": 1,
            "textAlign": "left",
            "verticalAlign": "top",
            "baseline": 14,
            "containerId": None,
            "originalText": text
        })

    document = {
        "type": "excalidraw",
        "version": 2,
        "source": "cli-generated",
        "elements": elements,
        "appState": {},
        "files": {}
    }

    return json.dumps(document, indent=2)
