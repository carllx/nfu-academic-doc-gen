# How To: Var Std

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test var std

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign result = datetime_frame.std(...)

```python
result = datetime_frame.std(ddof=4)
```

**Verification:**
```python
assert not (result < 0).any()
```

### Step 2: Assign expected = datetime_frame.apply(...)

```python
expected = datetime_frame.apply(lambda x: x.std(ddof=4))
```

**Verification:**
```python
assert not (result < 0).any()
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 4: Assign result = datetime_frame.var(...)

```python
result = datetime_frame.var(ddof=4)
```

### Step 5: Assign expected = datetime_frame.apply(...)

```python
expected = datetime_frame.apply(lambda x: x.var(ddof=4))
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Assign arr = np.repeat(...)

```python
arr = np.repeat(np.random.default_rng(2).random((1, 1000)), 1000, 0)
```

### Step 8: Assign result = nanops.nanvar(...)

```python
result = nanops.nanvar(arr, axis=0)
```

**Verification:**
```python
assert not (result < 0).any()
```

### Step 9: Assign result = nanops.nanvar(...)

```python
result = nanops.nanvar(arr, axis=0)
```

**Verification:**
```python
assert not (result < 0).any()
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame

# Workflow
result = datetime_frame.std(ddof=4)
expected = datetime_frame.apply(lambda x: x.std(ddof=4))
tm.assert_almost_equal(result, expected)
result = datetime_frame.var(ddof=4)
expected = datetime_frame.apply(lambda x: x.var(ddof=4))
tm.assert_almost_equal(result, expected)
arr = np.repeat(np.random.default_rng(2).random((1, 1000)), 1000, 0)
result = nanops.nanvar(arr, axis=0)
assert not (result < 0).any()
with pd.option_context('use_bottleneck', False):
    result = nanops.nanvar(arr, axis=0)
    assert not (result < 0).any()
```

## Next Steps


---

*Source: test_reductions.py:527 | Complexity: Advanced | Last updated: 2026-06-02*