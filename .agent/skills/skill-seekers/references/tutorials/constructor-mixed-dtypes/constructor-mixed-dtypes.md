# How To: Constructor Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor mixed dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`

**Setup Required:**
```python
# Fixtures: typ, ad
```

## Step-by-Step Guide

### Step 1: Call ad.update()

```python
ad.update(dict(zip(dtypes, arrays)))
```

**Verification:**
```python
assert a.dtype == d
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(ad)
```

**Verification:**
```python
assert df.dtypes[d] == d
```

### Step 3: Assign dtypes = value

```python
dtypes = MIXED_FLOAT_DTYPES + MIXED_INT_DTYPES
```

### Step 4: Assign dtypes = MIXED_INT_DTYPES

```python
dtypes = MIXED_INT_DTYPES
```

### Step 5: Assign arrays = value

```python
arrays = [np.array(np.random.default_rng(2).random(10), dtype=d) for d in dtypes]
```

**Verification:**
```python
assert a.dtype == d
```

### Step 6: Assign dtypes = MIXED_FLOAT_DTYPES

```python
dtypes = MIXED_FLOAT_DTYPES
```

### Step 7: Assign arrays = value

```python
arrays = [np.array(np.random.default_rng(2).integers(10, size=10), dtype=d) for d in dtypes]
```

**Verification:**
```python
assert df.dtypes[d] == d
```


## Complete Example

```python
# Setup
# Fixtures: typ, ad

# Workflow
if typ == 'int':
    dtypes = MIXED_INT_DTYPES
    arrays = [np.array(np.random.default_rng(2).random(10), dtype=d) for d in dtypes]
elif typ == 'float':
    dtypes = MIXED_FLOAT_DTYPES
    arrays = [np.array(np.random.default_rng(2).integers(10, size=10), dtype=d) for d in dtypes]
for d, a in zip(dtypes, arrays):
    assert a.dtype == d
ad.update(dict(zip(dtypes, arrays)))
df = DataFrame(ad)
dtypes = MIXED_FLOAT_DTYPES + MIXED_INT_DTYPES
for d in dtypes:
    if d in df:
        assert df.dtypes[d] == d
```

## Next Steps


---

*Source: test_constructors.py:393 | Complexity: Intermediate | Last updated: 2026-06-02*