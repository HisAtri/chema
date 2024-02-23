# Explaintions

## Mol.Wt and Exact Mass

### Mol.Wt

The average mass taking into account the abundance of isotopes in nature.

### Exact Mass

The mass of the most stable isotope.

## Data Source

- [International Atomic Energy Agency (IAEA)](https://www-nds.iaea.org/)
- [International Union of Pure and Applied Chemistry (IUPAC)](https://www.iupac.org/)

# Usage

## Install

```bash
pip install chemax
```

## Import

```python
from chemax import Molecule
```

## Create Molecule Object

```python
from chemax import Molecule

molecule = Molecule.simple_generate('H2O')
print(molecule.mol_wt)
print(molecule.exact_mass)
print(molecule.electric_charge)
```

## Accepted Formula

- Simple Formula: `H2O`
- Structural Formula: `CH3CH2OH`, `CH3(CH2)2OH`
- Hydrogen Isotopes: `D2O`, `T2O`, `CDCl3`(Chloroform-d)
- Ionic Formula: `{COO}-`, `{CH2(COO)2}2-`
