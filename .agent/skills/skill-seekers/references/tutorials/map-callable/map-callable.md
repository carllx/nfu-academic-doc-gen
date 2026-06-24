# How To: Map Callable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map callable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Call tm.assert_series_equal()

```python
tm.assert_series_equal(datetime_series.map(math.exp), np.exp(datetime_series))
```

**Verification:**
```python
assert s is not rs
```

### Step 2: Assign s = Series(...)

```python
s = Series(dtype=object, name='foo', index=Index([], name='bar'))
```

**Verification:**
```python
assert s.index is rs.index
```

### Step 3: Assign rs = s.map(...)

```python
rs = s.map(lambda x: x)
```

**Verification:**
```python
assert s.dtype == rs.dtype
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, rs)
```

**Verification:**
```python
assert s.name == rs.name
```

### Step 5: Assign s = Series(...)

```python
s = Series(index=[1, 2, 3], dtype=np.float64)
```

### Step 6: Assign rs = s.map(...)

```python
rs = s.map(lambda x: x)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, rs)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(datetime_series.map(np.sqrt), np.sqrt(datetime_series))
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
with np.errstate(all='ignore'):
    tm.assert_series_equal(datetime_series.map(np.sqrt), np.sqrt(datetime_series))
tm.assert_series_equal(datetime_series.map(math.exp), np.exp(datetime_series))
s = Series(dtype=object, name='foo', index=Index([], name='bar'))
rs = s.map(lambda x: x)
tm.assert_series_equal(s, rs)
assert s is not rs
assert s.index is rs.index
assert s.dtype == rs.dtype
assert s.name == rs.name
s = Series(index=[1, 2, 3], dtype=np.float64)
rs = s.map(lambda x: x)
tm.assert_series_equal(s, rs)
```

## Next Steps


---

*Source: test_map.py:35 | Complexity: Advanced | Last updated: 2026-06-02*