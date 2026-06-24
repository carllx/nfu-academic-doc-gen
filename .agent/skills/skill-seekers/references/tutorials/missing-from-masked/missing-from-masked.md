# How To: Missing From Masked

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing from masked

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core.interchange.column`
- `pandas.core.interchange.dataframe_protocol`
- `pandas.core.interchange.from_dataframe`
- `pandas.core.interchange.utils`
- `pyarrow.interchange`
- `pyarrow.compute`
- `pyarrow.interchange`
- `pyarrow.interchange`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'x': np.array([1.0, 2.0, 3.0, 4.0, 0.0]), 'y': np.array([1.5, 2.5, 3.5, 4.5, 0]), 'z': np.array([1.0, 0.0, 1.0, 1.0, 1.0])})
```

**Verification:**
```python
assert df2.get_column_by_name('x').null_count == dict_null['x']
```

### Step 2: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(2)
```

**Verification:**
```python
assert df2.get_column_by_name('y').null_count == dict_null['y']
```

### Step 3: Assign dict_null = value

```python
dict_null = {col: rng.integers(low=0, high=len(df)) for col in df.columns}
```

**Verification:**
```python
assert df2.get_column_by_name('z').null_count == dict_null['z']
```

### Step 4: Assign df2 = df.__dataframe__(...)

```python
df2 = df.__dataframe__()
```

**Verification:**
```python
assert df2.get_column_by_name('x').null_count == dict_null['x']
```

### Step 5: Assign null_idx = value

```python
null_idx = df.index[rng.choice(np.arange(len(df)), size=num_nulls, replace=False)]
```

### Step 6: Assign unknown = None

```python
df.loc[null_idx, col] = None
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'x': np.array([1.0, 2.0, 3.0, 4.0, 0.0]), 'y': np.array([1.5, 2.5, 3.5, 4.5, 0]), 'z': np.array([1.0, 0.0, 1.0, 1.0, 1.0])})
rng = np.random.default_rng(2)
dict_null = {col: rng.integers(low=0, high=len(df)) for col in df.columns}
for col, num_nulls in dict_null.items():
    null_idx = df.index[rng.choice(np.arange(len(df)), size=num_nulls, replace=False)]
    df.loc[null_idx, col] = None
df2 = df.__dataframe__()
assert df2.get_column_by_name('x').null_count == dict_null['x']
assert df2.get_column_by_name('y').null_count == dict_null['y']
assert df2.get_column_by_name('z').null_count == dict_null['z']
```

## Next Steps


---

*Source: test_impl.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*