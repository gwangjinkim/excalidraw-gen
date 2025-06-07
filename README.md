# Excalidraw Generator (Docker + CLI + YAML to .excalidraw)

Generate Excalidraw diagrams automatically from text input (YAML/Markdown) using a FastAPI Docker container and a CLI tool powered by `uv`.

## Features

- Self-contained Docker container with a FastAPI backend
- Upload YAML to generate `.excalidraw` files
- Minimal CLI using `uv` and `typer`
- Clean structure for future image export and Markdown support

## Quickstart

### 1. Build and Run the Docker API

```bash
docker-compose build
docker-compose up
```

The API will be available at: http://localhost:8000

### 2. Setup the CLI using `uv`

```bash
uv venv
uv pip install -e .
```

Now use the CLI command:

```bash
exgen generate api/sample.yaml
```

The output will be saved as `output.excalidraw`.

You can open the file at https://excalidraw.com or in your self-hosted Excalidraw instance.

## Input Format

Example YAML (`sample.yaml`):

```yaml
rows:
  - text: "Hello from YAML"
  - text: "Second row"
  - text: "Another block"
```

## Project Structure

```
excalidraw-gen/
├── api/
│   ├── main.py             # FastAPI endpoint
│   ├── generator.py        # YAML to .excalidraw
│   └── sample.yaml         # Example input
├── uv_tool/
│   ├── cli.py              # CLI interface
│   └── __init__.py
├── Dockerfile              # Python + FastAPI server
├── docker-compose.yml      # Docker setup
├── pyproject.toml          # uv + CLI definition
```

## Roadmap

- Add Markdown table to diagram support
- Export `.excalidraw` to PNG (via Puppeteer or excalidraw-export)
- Add `/render` endpoint
- Interactive UI to preview generated diagrams

## License

MIT License. Not affiliated with excalidraw.com.
