# How To: Dti Business Getitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti business getitem

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign rng = bdate_range(...)

```python
rng = bdate_range(START, END, freq=freq)
```

**Verification:**
```python
assert smaller.freq == exp.freq
```

### Step 2: Assign smaller = value

```python
smaller = rng[:5]
```

**Verification:**
```python
assert smaller.freq == rng.freq
```

### Step 3: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex(rng.view(np.ndarray)[:5], freq=freq)
```

**Verification:**
```python
assert sliced.freq == to_offset(freq) * 5
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(smaller, exp)
```

**Verification:**
```python
assert len(fancy_indexed) == 5
```

### Step 5: Assign sliced = value

```python
sliced = rng[::5]
```

**Verification:**
```python
assert isinstance(fancy_indexed, DatetimeIndex)
```

### Step 6: Assign fancy_indexed = value

```python
fancy_indexed = rng[[4, 3, 2, 1, 0]]
```

**Verification:**
```python
assert fancy_indexed.freq is None
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
rng = bdate_range(START, END, freq=freq)
smaller = rng[:5]
exp = DatetimeIndex(rng.view(np.ndarray)[:5], freq=freq)
tm.assert_index_equal(smaller, exp)
assert smaller.freq == exp.freq
assert smaller.freq == rng.freq
sliced = rng[::5]
assert sliced.freq == to_offset(freq) * 5
fancy_indexed = rng[[4, 3, 2, 1, 0]]
assert len(fancy_indexed) == 5
assert isinstance(fancy_indexed, DatetimeIndex)
assert fancy_indexed.freq is None
assert rng[4] == rng[np_long(4)]
```

## Next Steps


---

*Source: test_indexing.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*