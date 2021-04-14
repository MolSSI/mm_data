from pathlib import Path

from . import molecules
from . import forcefields
from . import trajectories

_mol_path = Path(molecules.__file__)
mols = {mol.name: mol for mol in _mol_path.parent.glob("*") if mol.is_file}

_ff_path = Path(forcefields.__file__)
ffs = {ff.name: ff for ff in _ff_path.parent.glob("*") if ff.is_file}

_traj_path = Path(trajectories.__file__)
trajs = {traj.name: traj for traj in _traj_path.parent.glob("*") if traj.is_file}
