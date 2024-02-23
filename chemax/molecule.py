from .computer import regular
from . import datas as atom


class Molecule:
    def __init__(self):
        self.formula = ''
        self.atoms = {}
        self.mol_wt = 0.0
        self.exact_mass = 0.0
        self.electric_charge = 0

    def __str__(self):
        return self.formula

    def simple(self, formula: str):
        self.formula = formula
        self.electric_charge, self.atoms = self.simple_molecular_formula(formula)
        self.mol_wt = self.molecular_weight_f(self.atoms)
        self.exact_mass = self.exact_mass_f(self.atoms)

    @staticmethod
    def simple_molecular_formula(formula: str) -> dict:
        return regular(formula)

    @staticmethod
    def molecular_weight_f(molecule: dict) -> float:
        mw = 0
        for _atom, _num in molecule.items():
            add = (atom.BALANCE.get(_atom, 0) or (atom.NUCLIDE.get(_atom, {}) or atom.NUCLIDE.get(atom.ABUNDANCE.get(_atom, {}).get("symbol"), {})).get("mass", 0)) * _num
            if not add:
                raise ValueError(f"Invalid atom '{_atom}' in formula")
            mw += add
        return mw

    @staticmethod
    def exact_mass_f(molecule: dict) -> float:
        mw = 0
        for _atom, _num in molecule.items():
            add = (atom.NUCLIDE.get(_atom, {}) or atom.NUCLIDE.get(atom.ABUNDANCE.get(_atom, {}).get("symbol"), {})).get("mass", 0) * _num
            if not add:
                raise ValueError(f"Invalid atom '{_atom}' in formula")
            mw += add
        return mw

    @staticmethod
    def simple_generate(formula: str) -> 'Molecule':
        r = Molecule()
        r.simple(formula)
        return r
