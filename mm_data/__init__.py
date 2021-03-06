from pathlib import Path

from . import molecules
from . import forcefields
from . import trajectories

exts = ("__", ".pyc", ".py", "_offsets.npz")

_mol_path = Path(molecules.__file__)
mols = {
    mol.name: str(mol)
    for mol in _mol_path.parent.glob("*")
    if (mol.is_file() and not mol.name.endswith(exts))
}

_ff_path = Path(forcefields.__file__)
ffs = {
    ff.name: str(ff)
    for ff in _ff_path.parent.glob("*")
    if (ff.is_file() and not ff.name.endswith(exts))
}

_traj_path = Path(trajectories.__file__)
trajs = {
    traj.name: str(traj)
    for traj in _traj_path.parent.glob("*")
    if (traj.is_file() and not traj.name.endswith(exts))
}
