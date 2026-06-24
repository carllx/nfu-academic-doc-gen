# How To: Agg Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test agg args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`

**Setup Required:**
```python
# Fixtures: args, kwargs, increment
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2])
```

### Step 2: Assign msg = 'in Series.agg cannot aggregate and has been deprecated. Use Series.transform to keep behavior unchanged.'

```python
msg = 'in Series.agg cannot aggregate and has been deprecated. Use Series.transform to keep behavior unchanged.'
```

### Step 3: Assign expected = value

```python
expected = s + increment
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.agg(...)

```python
result = s.agg(f, 0, *args, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: args, kwargs, increment

# Workflow
def f(x, a=0, b=0, c=0):
    return x + a + 10 * b + 100 * c
s = Series([1, 2])
msg = 'in Series.agg cannot aggregate and has been deprecated. Use Series.transform to keep behavior unchanged.'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.agg(f, 0, *args, **kwargs)
expected = s + increment
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series_apply.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*