# How To: Less Precise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test less precise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data1, data2, dtype, decimals
```

## Step-by-Step Guide

### Step 1: Assign rtol = value

```python
rtol = 10 ** (-decimals)
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series([data1], dtype=dtype)
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series([data2], dtype=dtype)
```

### Step 4: Assign msg = 'Series values are different'

```python
msg = 'Series values are different'
```

### Step 5: Call _assert_series_equal_both()

```python
_assert_series_equal_both(s1, s2, rtol=rtol)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s2, rtol=rtol)
```


## Complete Example

```python
# Setup
# Fixtures: data1, data2, dtype, decimals

# Workflow
rtol = 10 ** (-decimals)
s1 = Series([data1], dtype=dtype)
s2 = Series([data2], dtype=dtype)
if decimals in (5, 10) or (decimals >= 3 and abs(data1 - data2) >= 0.0005):
    msg = 'Series values are different'
    with pytest.raises(AssertionError, match=msg):
        tm.assert_series_equal(s1, s2, rtol=rtol)
else:
    _assert_series_equal_both(s1, s2, rtol=rtol)
```

## Next Steps


---

*Source: test_assert_series_equal.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*