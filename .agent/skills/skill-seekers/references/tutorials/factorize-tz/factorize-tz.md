# How To: Factorize Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture, index_or_series
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

**Verification:**
```python
assert res.freq == expected.freq
```

### Step 2: Assign base = date_range(...)

```python
base = date_range('2016-11-05', freq='h', periods=100, tz=tz)
```

### Step 3: Assign idx = base.repeat(...)

```python
idx = base.repeat(5)
```

### Step 4: Assign exp_arr = np.arange.repeat(...)

```python
exp_arr = np.arange(100, dtype=np.intp).repeat(5)
```

### Step 5: Assign obj = index_or_series(...)

```python
obj = index_or_series(idx)
```

### Step 6: Assign unknown = obj.factorize(...)

```python
arr, res = obj.factorize()
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 8: Assign expected = base._with_freq(...)

```python
expected = base._with_freq(None)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```

**Verification:**
```python
assert res.freq == expected.freq
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, index_or_series

# Workflow
tz = tz_naive_fixture
base = date_range('2016-11-05', freq='h', periods=100, tz=tz)
idx = base.repeat(5)
exp_arr = np.arange(100, dtype=np.intp).repeat(5)
obj = index_or_series(idx)
arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
expected = base._with_freq(None)
tm.assert_index_equal(res, expected)
assert res.freq == expected.freq
```

## Next Steps


---

*Source: test_factorize.py:74 | Complexity: Advanced | Last updated: 2026-06-02*