# How To: Lower Upper Mixed Object

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lower upper mixed object

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
s = Series(['a', np.nan, 'b', True, datetime.today(), 'foo', None, 1, 2.0])
```

### Step 2: Assign result = s.str.upper(...)

```python
result = s.str.upper()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['A', np.nan, 'B', np.nan, np.nan, 'FOO', None, np.nan, np.nan], dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.str.lower(...)

```python
result = s.str.lower()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['a', np.nan, 'b', np.nan, np.nan, 'foo', None, np.nan, np.nan], dtype=object)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(['a', np.nan, 'b', True, datetime.today(), 'foo', None, 1, 2.0])
result = s.str.upper()
expected = Series(['A', np.nan, 'B', np.nan, np.nan, 'FOO', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
result = s.str.lower()
expected = Series(['a', np.nan, 'b', np.nan, np.nan, 'foo', None, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_justify.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*