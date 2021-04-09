import os
from . import molecules
from . import forcefields
from . import trajectories

data_mol_dir = os.path.dirname(molecules.__file__)
data_ff_dir = os.path.dirname(forcefields.__file__)
data_traj_dir = os.path.dirname(trajectories.__file__)
