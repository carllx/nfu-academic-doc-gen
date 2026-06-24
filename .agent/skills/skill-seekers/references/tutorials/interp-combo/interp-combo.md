# How To: Interp Combo

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp combo

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1.0, 2.0, np.nan, 4.0], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
```

### Step 2: Assign result = unknown.interpolate(...)

```python
result = df['A'].interpolate()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1.0, 2.0, 3.0, 4.0], name='A')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = "The 'downcast' keyword in Series.interpolate is deprecated"

```python
msg = "The 'downcast' keyword in Series.interpolate is deprecated"
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 2, 3, 4], name='A')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = unknown.interpolate(...)

```python
result = df['A'].interpolate(downcast='infer')
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1.0, 2.0, np.nan, 4.0], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
result = df['A'].interpolate()
expected = Series([1.0, 2.0, 3.0, 4.0], name='A')
tm.assert_series_equal(result, expected)
msg = "The 'downcast' keyword in Series.interpolate is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df['A'].interpolate(downcast='infer')
expected = Series([1, 2, 3, 4], name='A')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:169 | Complexity: Advanced | Last updated: 2026-06-02*