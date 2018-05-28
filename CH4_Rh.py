import os
import sys

from ase import Atoms, Atom
from ase.build import molecule, fcc111, add_adsorbate
from ase.calculators.vasp import Vasp
from ase.test import must_raise

DIR_CH4 = 'mole_CH4'
DIRTEST = os.path.isdir(DIR_CH4)

if (not DIRTEST):
    os.mkdir(DIR_CH4)
os.chdir(DIR_CH4)

print(os.getcwd())
print(molecule("CH4"))
# CH4 = Atoms('CH4',pbc=True)
CH4 = molecule('CH4')

CH4.center(vacuum=10.)
# calc = Vasp()
calc = Vasp(prec='Accurate',
            xc='PBE',
            lreal=False)

CH4.set_calculator(calc)
# with must_raise(ValueError):
#     CH4.set_calculator(calc)
#     CH4.get_total_energy()

# print(CH4.get_potential_energy())
print(CH4.get_total_energy())

os.chdir("../")
print(os.getcwd())

DIR_Rh = 'slab_Rh'
DIRTEST = os.path.isdir(DIR_Rh)

if (not DIRTEST):
    os.mkdir(DIR_Rh)
os.chdir(DIR_Rh)

slab = fcc111('Rh', size=(3, 3, 4), vacuum=20.0)
calc = Vasp(prec='Accurate',
            xc='PBE',
            lreal=False,
            gamma=False, kpts=(4,4,1))
calc.write_kpoints()
#
#slab.set_calculator(calc)
#
#print(slab.get_total_energy())
#os.chdir("../")

