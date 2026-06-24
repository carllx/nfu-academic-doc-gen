# How To: Apply Funcs Over Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply funcs over empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['a', 'b', 'c'])
```

### Step 2: Assign result = df.apply(...)

```python
result = df.apply(getattr(np, func))
```

### Step 3: Assign expected = getattr(...)

```python
expected = getattr(df, func)()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = expected.astype(...)

```python
expected = expected.astype(float)
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
df = DataFrame(columns=['a', 'b', 'c'])
result = df.apply(getattr(np, func))
expected = getattr(df, func)()
if func in ('sum', 'prod'):
    expected = expected.astype(float)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*