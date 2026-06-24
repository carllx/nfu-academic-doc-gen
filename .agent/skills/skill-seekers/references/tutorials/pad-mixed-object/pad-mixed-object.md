# How To: Pad Mixed Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pad mixed object

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
s = Series(['a', np.nan, 'b', True, datetime.today(), 'ee', None, 1, 2.0])
```

### Step 2: Assign result = s.str.pad(...)

```python
result = s.str.pad(5, side='left')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['    a', np.nan, '    b', np.nan, np.nan, '   ee', None, np.nan, np.nan], dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.str.pad(...)

```python
result = s.str.pad(5, side='right')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['a    ', np.nan, 'b    ', np.nan, np.nan, 'ee   ', None, np.nan, np.nan], dtype=object)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.str.pad(...)

```python
result = s.str.pad(5, side='both')
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(['  a  ', np.nan, '  b  ', np.nan, np.nan, '  ee ', None, np.nan, np.nan], dtype=object)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(['a', np.nan, 'b', True, datetime.today(), 'ee', None, 1, 2.0])
result = s.str.pad(5, side='left')
expected = Series(['    a', np.nan, '    b', np.nan, np.nan, '   ee', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
result = s.str.pad(5, side='right')
expected = Series(['a    ', np.nan, 'b    ', np.nan, np.nan, 'ee   ', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
result = s.str.pad(5, side='both')
expected = Series(['  a  ', np.nan, '  b  ', np.nan, np.nan, '  ee ', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_justify.py:143 | Complexity: Advanced | Last updated: 2026-06-02*