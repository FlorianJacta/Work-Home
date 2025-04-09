# Installation Guide for SimAI Case Study

This guide provides multiple methods for setting up your development environment for the SimAI Case Study project. You can choose between `uv`, `pip`, or `conda`—whichever best suits your workflow.

---

## Prerequisites

- Python >= 3.9
- Recommended: Create a virtual environment

---

## Option 1: Using `uv` to install packages (Fast and Modern Python Toolchain)

### Step 1: Create a Virtual Environment
```bash
uv sync
```
### Step 2: Run scripts:
```bash
uv run src/visualization.py
uv run src/compute_surface.py
```

Or activate the .venv:
```bash
source .venv/bin/activate
python src/visualization.py
python src/compute_surface.py
```

---

## Option 2: Using `pip` and `venv`

### Step 1: Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 2: Install Requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Option 3: Using `conda`

### Step 1: Create a New Environment
```bash
conda create -n simai-case python=3.9
conda activate simai-case
```

### Step 2: Install Packages
```bash
pip install -r requirements.txt
```

---

## Run the Scripts
From the root directory:
```bash
python src/visualization.py
python src/compute_surface.py
```

Or from inside `src/`:
```bash
cd src
python visualization.py
python compute_surface.py
```

---

## Note
- The project uses PyVista, which may require additional dependencies (like `vtk`) that are handled automatically by `pip` or `uv`.
- Some 3D rendering may require an OpenGL-compatible display or X server on Linux systems.


