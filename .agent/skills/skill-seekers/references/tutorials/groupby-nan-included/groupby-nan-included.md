# How To: Groupby Nan Included

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby nan included

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'group': ['g1', np.nan, 'g1', 'g2', np.nan], 'B': [0, 1, 2, 3, 4]}
```

**Verification:**
```python
assert np.isnan(list(result.keys())[2])
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(data)
```

**Verification:**
```python
assert list(result.keys())[0:2] == ['g1', 'g2']
```

### Step 3: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('group', dropna=False)
```

### Step 4: Assign result = value

```python
result = grouped.indices
```

### Step 5: Assign dtype = value

```python
dtype = np.intp
```

### Step 6: Assign expected = value

```python
expected = {'g1': np.array([0, 2], dtype=dtype), 'g2': np.array([3], dtype=dtype), np.nan: np.array([1, 4], dtype=dtype)}
```

**Verification:**
```python
assert np.isnan(list(result.keys())[2])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_values, expected_values)
```


## Complete Example

```python
# Workflow
data = {'group': ['g1', np.nan, 'g1', 'g2', np.nan], 'B': [0, 1, 2, 3, 4]}
df = pd.DataFrame(data)
grouped = df.groupby('group', dropna=False)
result = grouped.indices
dtype = np.intp
expected = {'g1': np.array([0, 2], dtype=dtype), 'g2': np.array([3], dtype=dtype), np.nan: np.array([1, 4], dtype=dtype)}
for result_values, expected_values in zip(result.values(), expected.values()):
    tm.assert_numpy_array_equal(result_values, expected_values)
assert np.isnan(list(result.keys())[2])
assert list(result.keys())[0:2] == ['g1', 'g2']
```

## Next Steps


---

*Source: test_groupby_dropna.py:372 | Complexity: Intermediate | Last updated: 2026-06-02*