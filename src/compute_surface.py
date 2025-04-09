import pyvista as pv
import numpy as np
from pathlib import Path

# Get the directory where the script is located
script_dir = Path(__file__).resolve().parent
data_dir = script_dir / "data"

# Define file paths relative to script location
volume_path = data_dir / "volume_car.vtp"  # or use volume_spoiler.vtu
surface_path = data_dir / "surface_car.vtp"
output_path = data_dir / "surface_car_with_vars.vtp"

# Load the volume and surface mesh
volume = pv.read(volume_path)
surface = pv.read(surface_path)

# Interpolate volume scalars onto the surface points
interpolated_surface = surface.sample(volume)

# Save the new surface mesh with interpolated fields
interpolated_surface.save(output_path)
print(f"Surface file with projected variables saved to: {output_path}")

# Compute drag (sum of pressure + wall_shear across all surface nodes)
# Make sure both fields exist
if "pressure" not in interpolated_surface.array_names:
    raise ValueError("'pressure' field not found in volume data.")
if "wall_shear" not in interpolated_surface.array_names:
    print("'wall_shear' field not found. Assuming zero wall shear.")
    wall_shear = np.zeros_like(interpolated_surface["pressure"])
else:
    wall_shear = interpolated_surface["wall_shear"]

pressure = interpolated_surface["pressure"]
drag_values = pressure + wall_shear

# Estimate drag as the total sum (approximation)
estimated_drag = np.sum(drag_values)
print(f"Estimated Drag (approximated by sum of values): {estimated_drag:.4f}")
