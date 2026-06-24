# How To: Tz Localize

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2011', periods=100, freq='h')
```

**Verification:**
```python
assert result.index.tz is timezone.utc
```

### Step 2: Assign obj = DataFrame(...)

```python
obj = DataFrame({'a': 1}, index=rng)
```

### Step 3: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 4: Assign result = obj.tz_localize(...)

```python
result = obj.tz_localize('utc')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': 1}, rng.tz_localize('UTC'))
```

### Step 6: Assign expected = tm.get_obj(...)

```python
expected = tm.get_obj(expected, frame_or_series)
```

**Verification:**
```python
assert result.index.tz is timezone.utc
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2011', periods=100, freq='h')
obj = DataFrame({'a': 1}, index=rng)
obj = tm.get_obj(obj, frame_or_series)
result = obj.tz_localize('utc')
expected = DataFrame({'a': 1}, rng.tz_localize('UTC'))
expected = tm.get_obj(expected, frame_or_series)
assert result.index.tz is timezone.utc
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_tz_localize.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*