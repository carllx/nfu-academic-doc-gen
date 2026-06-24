# How To: Cache Updating

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cache updating

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.random(...)

```python
a = np.random.default_rng(2).random((10, 3))
```

**Verification:**
```python
assert df.loc[(0, 0), 'z'] == df_original.loc[0, 'z']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(a, columns=['x', 'y', 'z'])
```

**Verification:**
```python
assert result == 1
```

### Step 3: Assign df_original = df.copy(...)

```python
df_original = df.copy()
```

**Verification:**
```python
assert result == 2
```

### Step 4: Assign tuples = value

```python
tuples = [(i, j) for i in range(5) for j in range(2)]
```

### Step 5: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 6: Assign df.index = index

```python
df.index = index
```

### Step 7: Assign unknown = 2

```python
df.loc[(0, 0), 'z'] = 2
```

### Step 8: Assign result = value

```python
result = df.loc[(0, 0), 'z']
```

**Verification:**
```python
assert result == 2
```

### Step 9: Assign unknown = 1.0

```python
df.loc[0]['z'].iloc[0] = 1.0
```

**Verification:**
```python
assert df.loc[(0, 0), 'z'] == df_original.loc[0, 'z']
```

### Step 10: Assign result = value

```python
result = df.loc[(0, 0), 'z']
```

**Verification:**
```python
assert result == 1
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
a = np.random.default_rng(2).random((10, 3))
df = DataFrame(a, columns=['x', 'y', 'z'])
df_original = df.copy()
tuples = [(i, j) for i in range(5) for j in range(2)]
index = MultiIndex.from_tuples(tuples)
df.index = index
with tm.raises_chained_assignment_error():
    df.loc[0]['z'].iloc[0] = 1.0
if using_copy_on_write:
    assert df.loc[(0, 0), 'z'] == df_original.loc[0, 'z']
else:
    result = df.loc[(0, 0), 'z']
    assert result == 1
df.loc[(0, 0), 'z'] = 2
result = df.loc[(0, 0), 'z']
assert result == 2
```

## Next Steps


---

*Source: test_chaining_and_caching.py:47 | Complexity: Advanced | Last updated: 2026-06-02*