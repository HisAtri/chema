from .computer import regular
from . import datas


class Molecule:
    def __init__(self):
        self.formula = ''
        self.smile = ''
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

    def smile(self, smile: str):
        self.smile = smile
        pass

    @staticmethod
    def simple_molecular_formula(formula: str) -> dict:
        return regular(formula)

    @staticmethod
    def molecular_weight_f(molecule: dict) -> float:
        mw = 0
        for _atom, _num in molecule.items():
            add = (datas.BALANCE.get(_atom, 0) or (datas.NUCLIDE.get(_atom, {}) or datas.NUCLIDE.get(datas.ABUNDANCE.get(_atom, {}).get("symbol"), {})).get("mass", 0)) * _num
            if not add:
                raise ValueError(f"Invalid atom '{_atom}' in formula")
            mw += add
        return mw

    @staticmethod
    def exact_mass_f(molecule: dict) -> float:
        mw = 0
        for _atom, _num in molecule.items():
            add = (datas.NUCLIDE.get(_atom, {}) or datas.NUCLIDE.get(datas.ABUNDANCE.get(_atom, {}).get("symbol"), {})).get("mass", 0) * _num
            if not add:
                raise ValueError(f"Invalid atom '{_atom}' in formula")
            mw += add
        return mw

    @staticmethod
    def simple_generate(formula: str) -> 'Molecule':
        if not formula or not isinstance(formula, str):
            raise ValueError("Invalid formula")
        r = Molecule()
        r.simple(formula)
        return r

    @staticmethod
    def smile_generate(smile: str) -> 'Molecule':
        pass
