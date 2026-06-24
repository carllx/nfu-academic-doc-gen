# How To: Searchsorted Monotonic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test searchsorted monotonic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_flat, request
```

## Step-by-Step Guide

### Step 1: Assign index = index_flat

```python
index = index_flat
```

**Verification:**
```python
assert expected_left == ssm_left
```

### Step 2: Assign value = value

```python
value = index[0]
```

**Verification:**
```python
assert expected_right == ssm_right
```

### Step 3: Assign unknown = value

```python
expected_left, expected_right = (0, (index == value).argmin())
```

**Verification:**
```python
assert expected_left == ss_left
```

### Step 4: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='IntervalIndex.searchsorted does not support Interval arg', raises=NotImplementedError)
```

**Verification:**
```python
assert expected_right == ss_right
```

### Step 5: Call request.applymarker()

```python
request.applymarker(mark)
```

**Verification:**
```python
assert expected_left == ssm_left
```

### Step 6: Call pytest.skip()

```python
pytest.skip('Skip check for empty Index')
```

**Verification:**
```python
assert expected_right == ssm_right
```

### Step 7: Assign expected_right = len(...)

```python
expected_right = len(index)
```

### Step 8: Assign ssm_left = index._searchsorted_monotonic(...)

```python
ssm_left = index._searchsorted_monotonic(value, side='left')
```

**Verification:**
```python
assert expected_left == ssm_left
```

### Step 9: Assign ssm_right = index._searchsorted_monotonic(...)

```python
ssm_right = index._searchsorted_monotonic(value, side='right')
```

**Verification:**
```python
assert expected_right == ssm_right
```

### Step 10: Assign ss_left = index.searchsorted(...)

```python
ss_left = index.searchsorted(value, side='left')
```

**Verification:**
```python
assert expected_left == ss_left
```

### Step 11: Assign ss_right = index.searchsorted(...)

```python
ss_right = index.searchsorted(value, side='right')
```

**Verification:**
```python
assert expected_right == ss_right
```

### Step 12: Assign ssm_left = index._searchsorted_monotonic(...)

```python
ssm_left = index._searchsorted_monotonic(value, side='left')
```

**Verification:**
```python
assert expected_left == ssm_left
```

### Step 13: Assign ssm_right = index._searchsorted_monotonic(...)

```python
ssm_right = index._searchsorted_monotonic(value, side='right')
```

**Verification:**
```python
assert expected_right == ssm_right
```

### Step 14: Assign msg = 'index must be monotonic increasing or decreasing'

```python
msg = 'index must be monotonic increasing or decreasing'
```

### Step 15: Call index._searchsorted_monotonic()

```python
index._searchsorted_monotonic(value, side='left')
```


## Complete Example

```python
# Setup
# Fixtures: index_flat, request

# Workflow
index = index_flat
if isinstance(index, pd.IntervalIndex):
    mark = pytest.mark.xfail(reason='IntervalIndex.searchsorted does not support Interval arg', raises=NotImplementedError)
    request.applymarker(mark)
if index.empty:
    pytest.skip('Skip check for empty Index')
value = index[0]
expected_left, expected_right = (0, (index == value).argmin())
if expected_right == 0:
    expected_right = len(index)
if index.is_monotonic_increasing:
    ssm_left = index._searchsorted_monotonic(value, side='left')
    assert expected_left == ssm_left
    ssm_right = index._searchsorted_monotonic(value, side='right')
    assert expected_right == ssm_right
    ss_left = index.searchsorted(value, side='left')
    assert expected_left == ss_left
    ss_right = index.searchsorted(value, side='right')
    assert expected_right == ss_right
elif index.is_monotonic_decreasing:
    ssm_left = index._searchsorted_monotonic(value, side='left')
    assert expected_left == ssm_left
    ssm_right = index._searchsorted_monotonic(value, side='right')
    assert expected_right == ssm_right
else:
    msg = 'index must be monotonic increasing or decreasing'
    with pytest.raises(ValueError, match=msg):
        index._searchsorted_monotonic(value, side='left')
```

## Next Steps


---

*Source: test_common.py:252 | Complexity: Advanced | Last updated: 2026-06-02*