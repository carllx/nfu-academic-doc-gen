# How To: Last Subset

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test last subset

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
ts = DataFrame(np.random.default_rng(2).standard_normal((30, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=30, freq='D'))
```

### Step 4: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

**Verification:**
```python
assert len(result) == 10
```

### Step 5: Assign expected = value

```python
expected = ts['2000-01-10':]
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign expected = value

```python
expected = ts[-21:]
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(result, ts[:0])
```

### Step 10: Assign result = ts.last(...)

```python
result = ts.last('10d')
```

### Step 11: Assign result = ts.last(...)

```python
result = ts.last('10d')
```

### Step 12: Assign result = ts.last(...)

```python
result = ts.last('21D')
```

### Step 13: Assign result = ts.last(...)

```python
result = ts.last('21D')
```

### Step 14: Assign result = unknown.last(...)

```python
result = ts[:0].last('3ME')
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
ts = DataFrame(np.random.default_rng(2).standard_normal((100, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=100, freq='12h'))
ts = tm.get_obj(ts, frame_or_series)
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg):
    result = ts.last('10d')
assert len(result) == 20
ts = DataFrame(np.random.default_rng(2).standard_normal((30, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=30, freq='D'))
ts = tm.get_obj(ts, frame_or_series)
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg):
    result = ts.last('10d')
assert len(result) == 10
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg):
    result = ts.last('21D')
expected = ts['2000-01-10':]
tm.assert_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg):
    result = ts.last('21D')
expected = ts[-21:]
tm.assert_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg):
    result = ts[:0].last('3ME')
tm.assert_equal(result, ts[:0])
```

## Next Steps


---

*Source: test_first_and_last.py:77 | Complexity: Advanced | Last updated: 2026-06-02*