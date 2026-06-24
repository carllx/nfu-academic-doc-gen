# How To: Set Inplace

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set inplace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `functools`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._optional`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.core.computation.engines`
- `pandas.core.computation.expr`
- `pandas.core.computation.expressions`
- `pandas.core.computation.ops`
- `pandas.core.computation.scope`
- `pandas.util.version`
- `pandas.core.computation.eval`
- `numexpr`
- `numexpr`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
```

### Step 2: Assign result_view = value

```python
result_view = df[:]
```

### Step 3: Assign ser = value

```python
ser = df['A']
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [11, 13, 15], 'B': [4, 5, 6], 'C': [7, 8, 9]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Call df.eval()

```python
df.eval('A = B + C', inplace=True)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected['A'])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_view['A'], expected['A'])
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([1, 2, 3], name='A')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_view['A'], expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
result_view = df[:]
ser = df['A']
with tm.assert_cow_warning(warn_copy_on_write):
    df.eval('A = B + C', inplace=True)
expected = DataFrame({'A': [11, 13, 15], 'B': [4, 5, 6], 'C': [7, 8, 9]})
tm.assert_frame_equal(df, expected)
if not using_copy_on_write:
    tm.assert_series_equal(ser, expected['A'])
    tm.assert_series_equal(result_view['A'], expected['A'])
else:
    expected = Series([1, 2, 3], name='A')
    tm.assert_series_equal(ser, expected)
    tm.assert_series_equal(result_view['A'], expected)
```

## Next Steps


---

*Source: test_eval.py:1981 | Complexity: Advanced | Last updated: 2026-06-02*