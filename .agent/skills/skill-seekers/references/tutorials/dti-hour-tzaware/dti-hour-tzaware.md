# How To: Dti Hour Tzaware

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti hour tzaware

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: prefix
```

## Step-by-Step Guide

### Step 1: Assign strdates = value

```python
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
```

**Verification:**
```python
assert (rng.hour == 0).all()
```

### Step 2: Assign rng = DatetimeIndex(...)

```python
rng = DatetimeIndex(strdates, tz=prefix + 'US/Eastern')
```

**Verification:**
```python
assert (rng.hour == 0).all()
```

### Step 3: Assign dr = date_range(...)

```python
dr = date_range('2011-10-02 00:00', freq='h', periods=10, tz=prefix + 'America/Atikokan')
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(np.arange(10, dtype=np.int32))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(dr.hour, expected)
```


## Complete Example

```python
# Setup
# Fixtures: prefix

# Workflow
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
rng = DatetimeIndex(strdates, tz=prefix + 'US/Eastern')
assert (rng.hour == 0).all()
dr = date_range('2011-10-02 00:00', freq='h', periods=10, tz=prefix + 'America/Atikokan')
expected = Index(np.arange(10, dtype=np.int32))
tm.assert_index_equal(dr.hour, expected)
```

## Next Steps


---

*Source: test_scalar_compat.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*