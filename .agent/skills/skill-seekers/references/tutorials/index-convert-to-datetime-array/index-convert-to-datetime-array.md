# How To: Index Convert To Datetime Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index convert to datetime array

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('20090415', '20090519')
```

**Verification:**
```python
assert isinstance(converted, np.ndarray)
```

### Step 2: Assign rng_eastern = date_range(...)

```python
rng_eastern = date_range('20090415', '20090519', tz='US/Eastern')
```

**Verification:**
```python
assert isinstance(x, datetime)
```

### Step 3: Assign rng_utc = date_range(...)

```python
rng_utc = date_range('20090415', '20090519', tz='utc')
```

**Verification:**
```python
assert x == stamp.to_pydatetime()
```

### Step 4: Call _check_rng()

```python
_check_rng(rng)
```

**Verification:**
```python
assert x.tzinfo == stamp.tzinfo
```

### Step 5: Call _check_rng()

```python
_check_rng(rng_eastern)
```

### Step 6: Call _check_rng()

```python
_check_rng(rng_utc)
```

### Step 7: Assign converted = rng.to_pydatetime(...)

```python
converted = rng.to_pydatetime()
```

**Verification:**
```python
assert isinstance(converted, np.ndarray)
```


## Complete Example

```python
# Workflow
def _check_rng(rng):
    converted = rng.to_pydatetime()
    assert isinstance(converted, np.ndarray)
    for x, stamp in zip(converted, rng):
        assert isinstance(x, datetime)
        assert x == stamp.to_pydatetime()
        assert x.tzinfo == stamp.tzinfo
rng = date_range('20090415', '20090519')
rng_eastern = date_range('20090415', '20090519', tz='US/Eastern')
rng_utc = date_range('20090415', '20090519', tz='utc')
_check_rng(rng)
_check_rng(rng_eastern)
_check_rng(rng_utc)
```

## Next Steps


---

*Source: test_astype.py:239 | Complexity: Intermediate | Last updated: 2026-06-02*