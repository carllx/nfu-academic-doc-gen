# How To: First Subset

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test first subset

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
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((100, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=100, freq='12h'))
```

**Verification:**
```python
assert len(result) == 20
```

### Step 2: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

**Verification:**
```python
assert len(result) == 10
```

### Step 3: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((100, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=100, freq='D'))
```

### Step 4: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

### Step 5: Assign result = ts.first(...)

```python
result = ts.first('10d')
```

**Verification:**
```python
assert len(result) == 20
```

### Step 6: Assign result = ts.first(...)

```python
result = ts.first('10d')
```

**Verification:**
```python
assert len(result) == 10
```

### Step 7: Assign result = ts.first(...)

```python
result = ts.first('3ME')
```

### Step 8: Assign expected = value

```python
expected = ts[:'3/31/2000']
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 10: Assign result = ts.first(...)

```python
result = ts.first('21D')
```

### Step 11: Assign expected = value

```python
expected = ts[:21]
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 13: Assign result = unknown.first(...)

```python
result = ts[:0].first('3ME')
```

### Step 14: Call tm.assert_equal()

```python
tm.assert_equal(result, ts[:0])
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
ts = DataFrame(np.random.default_rng(2).standard_normal((100, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=100, freq='12h'))
ts = tm.get_obj(ts, frame_or_series)
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg):
    result = ts.first('10d')
    assert len(result) == 20
ts = DataFrame(np.random.default_rng(2).standard_normal((100, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=100, freq='D'))
ts = tm.get_obj(ts, frame_or_series)
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg):
    result = ts.first('10d')
    assert len(result) == 10
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg):
    result = ts.first('3ME')
    expected = ts[:'3/31/2000']
    tm.assert_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg):
    result = ts.first('21D')
    expected = ts[:21]
    tm.assert_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg):
    result = ts[:0].first('3ME')
    tm.assert_equal(result, ts[:0])
```

## Next Steps


---

*Source: test_first_and_last.py:21 | Complexity: Advanced | Last updated: 2026-06-02*