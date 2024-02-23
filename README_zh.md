# 说明

## 摩尔质量和精确质量

### 摩尔质量

考虑到自然界同位素丰度的平均质量。

### 精确质量

按照最稳定的核素取值。

## 数据来源

- [国际原子能机构（IAEA）](https://www-nds.iaea.org/)
- [国际纯粹与应用化学联合会（IUPAC）](https://www.iupac.org/)

# 使用方法

## 安装

```bash
pip install chemax
```

## 引入

```python
from chemax import Molecule
```

## 创建分子对象

```python
from chemax import Molecule

molecule = Molecule.simple_generate('H2O')
print(molecule.mol_wt)
print(molecule.exact_mass)
print(molecule.electric_charge)
```

## 接受的分子式

- 简单分子式：`H2O`
- 结构简式：`CH3CH2OH`，`CH3(CH2)2OH`
- 氢同位素：`D2O`，`T2O`，`CDCl3`(氘代氯仿)
- 离子式: `{COO}-`, `{CH2(COO)2}2-`
