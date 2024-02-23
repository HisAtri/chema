"""
Data Sources
ATOMIC WEIGHTS OF THE ELEMENTS 2021 (IUPAC / Atomic Weight) https://iupac.qmul.ac.uk/AtWt/
Atomic Mass Evaluation (International Atomic Energy Agency) https://www-nds.iaea.org/amdc/
"""

from . import balance, nuclide, abundant_nuclide

__all__ = ['NUCLIDE', 'BALANCE', 'ABUNDANCE']

NUCLIDE = nuclide.MASS
BALANCE = balance.ATOM
ABUNDANCE = abundant_nuclide.ABU
