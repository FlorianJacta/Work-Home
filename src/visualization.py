import pyvista as pv
from pathlib import Path

# Get the directory where the script is located
script_dir = Path(__file__).resolve().parent

# Build paths to data files relative to the script location
data_dir = script_dir / "data"
surface_car_path = data_dir / "surface_car.vtp"
volume_car_path = data_dir / "volume_car.vtp"
surface_spoiler_path = data_dir / "surface_spoiler.vtp"
volume_spoiler_path = data_dir / "volume_spoiler.vtu"


# Load and plot the car surface
surface_car = pv.read(surface_car_path)
surface_car.plot(
    scalars=None,
    show_edges=True,
)

# Load and plot the car volume
volume_car = pv.read(volume_car_path)
volume_car.plot(
    scalars="pressure",
    cmap="coolwarm",
)

# Load and plot the spoiler surface
surface_spoiler = pv.read(surface_spoiler_path)
surface_spoiler.plot(
    scalars=None,
    show_edges=True,
)

# Load and plot the spoiler volume
volume_spoiler = pv.read(volume_spoiler_path)
volume_spoiler.plot(
    scalars="pressure",
    cmap="coolwarm",
)
