# How To: Multiindex Dtype Preservation

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex dtype preservation

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('A', 'B')], names=['lvl1', 'lvl2'])
```

**Verification:**
```python
assert isinstance(df_no_multiindex['B'].dtype, CategoricalDtype)
```

### Step 2: Assign df = DataFrame.astype(...)

```python
df = DataFrame(['value'], columns=columns).astype('category')
```

**Verification:**
```python
assert isinstance(df['bools'].dtype, BooleanDtype)
```

### Step 3: Assign df_no_multiindex = value

```python
df_no_multiindex = df['A']
```

**Verification:**
```python
assert isinstance(df_no_multiindex['B'].dtype, CategoricalDtype)
```

### Step 4: Assign df = DataFrame.assign(...)

```python
df = DataFrame([[1, 0], [0, 1]], columns=[['foo', 'foo'], ['location', 'location'], ['x', 'y']]).assign(bools=Series([True, False], dtype='boolean'))
```

**Verification:**
```python
assert isinstance(df['bools'].dtype, BooleanDtype)
```


## Complete Example

```python
# Workflow
columns = MultiIndex.from_tuples([('A', 'B')], names=['lvl1', 'lvl2'])
df = DataFrame(['value'], columns=columns).astype('category')
df_no_multiindex = df['A']
assert isinstance(df_no_multiindex['B'].dtype, CategoricalDtype)
df = DataFrame([[1, 0], [0, 1]], columns=[['foo', 'foo'], ['location', 'location'], ['x', 'y']]).assign(bools=Series([True, False], dtype='boolean'))
assert isinstance(df['bools'].dtype, BooleanDtype)
```

## Next Steps


---

*Source: test_multiindex.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*