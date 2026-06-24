# How To: Access By Position

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test access by position

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_flat
```

## Step-by-Step Guide

### Step 1: Assign index = index_flat

```python
index = index_flat
```

**Verification:**
```python
assert index[0] == series.iloc[0]
```

### Step 2: Assign series = Series(...)

```python
series = Series(index)
```

**Verification:**
```python
assert index[5] == series.iloc[5]
```

### Step 3: Assign size = len(...)

```python
size = len(index)
```

**Verification:**
```python
assert index[-1] == series.iloc[-1]
```

### Step 4: Assign msg = value

```python
msg = f'index {size} is out of bounds for axis 0 with size {size}'
```

**Verification:**
```python
assert index[-1] == index[size - 1]
```

### Step 5: Assign msg = 'single positional indexer is out-of-bounds'

```python
msg = 'single positional indexer is out-of-bounds'
```

### Step 6: Call pytest.skip()

```python
pytest.skip("Test doesn't make sense on empty data")
```

### Step 7: Assign msg = 'index out of bounds'

```python
msg = 'index out of bounds'
```

### Step 8: index[size]

```python
index[size]
```

### Step 9: series.iloc[size]

```python
series.iloc[size]
```


## Complete Example

```python
# Setup
# Fixtures: index_flat

# Workflow
index = index_flat
if len(index) == 0:
    pytest.skip("Test doesn't make sense on empty data")
series = Series(index)
assert index[0] == series.iloc[0]
assert index[5] == series.iloc[5]
assert index[-1] == series.iloc[-1]
size = len(index)
assert index[-1] == index[size - 1]
msg = f'index {size} is out of bounds for axis 0 with size {size}'
if isinstance(index.dtype, pd.StringDtype) and index.dtype.storage == 'pyarrow':
    msg = 'index out of bounds'
with pytest.raises(IndexError, match=msg):
    index[size]
msg = 'single positional indexer is out-of-bounds'
with pytest.raises(IndexError, match=msg):
    series.iloc[size]
```

## Next Steps


---

*Source: test_misc.py:169 | Complexity: Advanced | Last updated: 2026-06-02*