# SimAI Case Study: Car Spoiler Optimization

This project is a solution to a Product Specialist case study based on the SimAI platform. The goal is to assist a customer in exploring 3D simulation data, computing aerodynamic drag, understanding deep learning for CAE, and proposing an optimization workflow for car spoiler design.

---

## Project Structure

```
WORK-HOME/
├── src/
│   ├── data/
│   │   ├── surface_car.vtp
│   │   ├── surface_spoiler.vtp
│   │   ├── volume_car.vtp
│   │   └── volume_spoiler.vtu
│   ├── visualization.py         # Script to visualize 3D data
│   └── compute_surface.py       # Script to project volume data onto surface and compute drag
├── SimAI_Case_Study.ipynb # Notebook answering technical questions
├── requirements.txt             # Python dependencies
├── WorkHome_Product_Specialist.pdf # PDF encapsulating the Work@Home and questions
├── installation.md              # Setup instructions
├── README.md                    # This file
└── slides/                      # Slide decks
    ├── Introduction to PyVista.pptx
    └── SimAI introduction.pptx
```

---

## Installation & Setup

See [installation.md](installation.md) for full environment setup using either `uv` or `pip`.

---

## Use Cases & Solutions

### 3D Visualization

**Question:** How can the user visualize and explore the 3D simulation data?

**Solution:** We use [PyVista](https://docs.pyvista.org) for interactive 3D rendering of surfaces and volumes.

Run the following command from the root or `src`:
```bash
python src/visualization.py
```

---

### Computing Drag from Surface Mesh

**Question:** How can we compute the drag coefficient when the surface file lacks pressure and wall shear data?

**Solution:** Use `compute_surface.py` to:
- Load surface and volume files.
- Interpolate `pressure` and `wall_shear` from volume to surface.
- Save the enhanced surface mesh for further computation.

Run:
```bash
python src/compute_surface.py
```

---

### Explaining SimAI & Deep Learning for CAE

**Question:** How does SimAI work? What deep learning technologies are best for CAE?

**Answer:**
- SimAI uses AI models (like 3D CNNs or GNNs) to predict physics fields.
- It reduces simulation times from hours to seconds.
- Suitable models: 3D CNN, GNNs, PointNet++.
- SimAI bridges physical laws and AI for fast, accurate simulation predictions.

See the presentation in `slides/SimAI introduction.pptx`

---

### Optimizing the Spoiler

**Question:** How can the customer optimize the spoiler’s shape and position to reduce drag?

**Solution:** Use SimAI for rapid predictions in a loop driven by an optimization engine (e.g., Optuna or BoTorch).

Recommended Workflow:
- Generate design variants.
- Predict drag using SimAI.
- Use Bayesian Optimization to find the best design.

Details in `slides/SimAI introduction.pptx`

---

## FAQ

**Q: Can I run the scripts from the root folder?**
Yes. Both scripts handle relative paths using `os.path` and can be executed from root or `src`.

**Q: What formats are supported?**
This project works with `.vtp` (surface) and `.vtu`/`.vtp` (volume) formats using PyVista.

**Q: Can I reuse this for other CAE problems?**
Absolutely. Just replace the mesh files in `src/data/`.

**Q: Do I need a GPU?**
Not for this part of the project. Only CPU is needed for visualization and projection. DL training would require a GPU in real-world use.

---

## Contact
Prepared for Ansys - SimAI by Florian.

