# How To: Center Ljust Rjust Mixed Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test center ljust rjust mixed object

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', np.nan, 'b', True, datetime.today(), 'c', 'eee', None, 1, 2.0])
```

### Step 2: Assign result = s.str.center(...)

```python
result = s.str.center(5)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['  a  ', np.nan, '  b  ', np.nan, np.nan, '  c  ', ' eee ', None, np.nan, np.nan], dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.str.ljust(...)

```python
result = s.str.ljust(5)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['a    ', np.nan, 'b    ', np.nan, np.nan, 'c    ', 'eee  ', None, np.nan, np.nan], dtype=object)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.str.rjust(...)

```python
result = s.str.rjust(5)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(['    a', np.nan, '    b', np.nan, np.nan, '    c', '  eee', None, np.nan, np.nan], dtype=object)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(['a', np.nan, 'b', True, datetime.today(), 'c', 'eee', None, 1, 2.0])
result = s.str.center(5)
expected = Series(['  a  ', np.nan, '  b  ', np.nan, np.nan, '  c  ', ' eee ', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
result = s.str.ljust(5)
expected = Series(['a    ', np.nan, 'b    ', np.nan, np.nan, 'c    ', 'eee  ', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
result = s.str.rjust(5)
expected = Series(['    a', np.nan, '    b', np.nan, np.nan, '    c', '  eee', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_justify.py:235 | Complexity: Advanced | Last updated: 2026-06-02*