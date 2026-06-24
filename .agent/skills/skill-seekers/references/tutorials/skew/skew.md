# How To: Skew

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skew

## Prerequisites

**Required Modules:**
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign sp_stats = pytest.importorskip(...)

```python
sp_stats = pytest.importorskip('scipy.stats')
```

**Verification:**
```python
assert np.isnan(s.skew())
```

### Step 2: Assign string_series = Series(...)

```python
string_series = Series(range(20), dtype=np.float64, name='series')
```

**Verification:**
```python
assert np.isnan(df.skew()).all()
```

### Step 3: Assign alt = value

```python
alt = lambda x: sp_stats.skew(x, bias=False)
```

**Verification:**
```python
assert 0 == s.skew()
```

### Step 4: Call self._check_stat_op()

```python
self._check_stat_op('skew', alt, string_series)
```

**Verification:**
```python
assert isinstance(s.skew(), np.float64)
```

### Step 5: Assign min_N = 3

```python
min_N = 3
```

**Verification:**
```python
assert (df.skew() == 0).all()
```

### Step 6: Assign s = Series(...)

```python
s = Series(np.ones(i))
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((i, i)))
```

**Verification:**
```python
assert np.isnan(s.skew())
```


## Complete Example

```python
# Workflow
sp_stats = pytest.importorskip('scipy.stats')
string_series = Series(range(20), dtype=np.float64, name='series')
alt = lambda x: sp_stats.skew(x, bias=False)
self._check_stat_op('skew', alt, string_series)
min_N = 3
for i in range(1, min_N + 1):
    s = Series(np.ones(i))
    df = DataFrame(np.ones((i, i)))
    if i < min_N:
        assert np.isnan(s.skew())
        assert np.isnan(df.skew()).all()
    else:
        assert 0 == s.skew()
        assert isinstance(s.skew(), np.float64)
        assert (df.skew() == 0).all()
```

## Next Steps


---

*Source: test_stat_reductions.py:233 | Complexity: Intermediate | Last updated: 2026-06-02*