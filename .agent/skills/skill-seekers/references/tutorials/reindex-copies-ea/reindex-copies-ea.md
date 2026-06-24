# How To: Reindex Copies Ea

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex copies ea

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert np.shares_memory(result[0].array._data, df[0].array._data)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((N * 10, N)), dtype='Float64')
```

**Verification:**
```python
assert not np.shares_memory(result[0].array._data, df[0].array._data)
```

### Step 3: Assign cols = np.arange(...)

```python
cols = np.arange(N)
```

**Verification:**
```python
assert np.shares_memory(result2[0].array._data, df[0].array._data)
```

### Step 4: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(cols)
```

**Verification:**
```python
assert not np.shares_memory(result2[0].array._data, df[0].array._data)
```

### Step 5: Assign result = df.reindex(...)

```python
result = df.reindex(columns=cols, copy=True)
```

### Step 6: Assign result2 = df.reindex(...)

```python
result2 = df.reindex(columns=cols, index=df.index, copy=True)
```

**Verification:**
```python
assert np.shares_memory(result[0].array._data, df[0].array._data)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
N = 10
df = DataFrame(np.random.default_rng(2).standard_normal((N * 10, N)), dtype='Float64')
cols = np.arange(N)
np.random.default_rng(2).shuffle(cols)
result = df.reindex(columns=cols, copy=True)
if using_copy_on_write:
    assert np.shares_memory(result[0].array._data, df[0].array._data)
else:
    assert not np.shares_memory(result[0].array._data, df[0].array._data)
result2 = df.reindex(columns=cols, index=df.index, copy=True)
if using_copy_on_write:
    assert np.shares_memory(result2[0].array._data, df[0].array._data)
else:
    assert not np.shares_memory(result2[0].array._data, df[0].array._data)
```

## Next Steps


---

*Source: test_reindex.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*