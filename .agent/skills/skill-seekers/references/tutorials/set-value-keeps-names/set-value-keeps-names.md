# How To: Set Value Keeps Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set value keeps names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign lev1 = value

```python
lev1 = ['hans', 'hans', 'hans', 'grethe', 'grethe', 'grethe']
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 2: Assign lev2 = value

```python
lev2 = ['1', '2', '3'] * 2
```

**Verification:**
```python
assert df.index.names == ('Name', 'Number')
```

### Step 3: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([lev1, lev2], names=['Name', 'Number'])
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 4: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(np.random.default_rng(2).standard_normal((6, 4)), columns=['one', 'two', 'three', 'four'], index=idx)
```

**Verification:**
```python
assert df.index.names == ('Name', 'Number')
```

### Step 5: Assign df = df.sort_index(...)

```python
df = df.sort_index()
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 6: Assign unknown = 99.34

```python
df.at[('grethe', '4'), 'one'] = 99.34
```

**Verification:**
```python
assert df._is_copy is None
```


## Complete Example

```python
# Workflow
lev1 = ['hans', 'hans', 'hans', 'grethe', 'grethe', 'grethe']
lev2 = ['1', '2', '3'] * 2
idx = MultiIndex.from_arrays([lev1, lev2], names=['Name', 'Number'])
df = pd.DataFrame(np.random.default_rng(2).standard_normal((6, 4)), columns=['one', 'two', 'three', 'four'], index=idx)
df = df.sort_index()
assert df._is_copy is None
assert df.index.names == ('Name', 'Number')
df.at[('grethe', '4'), 'one'] = 99.34
assert df._is_copy is None
assert df.index.names == ('Name', 'Number')
```

## Next Steps


---

*Source: test_get_set.py:324 | Complexity: Intermediate | Last updated: 2026-06-02*