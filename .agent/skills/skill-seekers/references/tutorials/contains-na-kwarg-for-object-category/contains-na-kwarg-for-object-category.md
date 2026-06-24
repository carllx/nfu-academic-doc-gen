# How To: Contains Na Kwarg For Object Category

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains na kwarg for object category

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas.tests.strings`


## Step-by-Step Guide

### Step 1: Assign values = Series(...)

```python
values = Series(['a', 'b', 'c', 'a', np.nan], dtype='category')
```

### Step 2: Assign result = values.str.contains(...)

```python
result = values.str.contains('a', na=True)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, True])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = values.str.contains(...)

```python
result = values.str.contains('a', na=False)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, False])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign values = Series(...)

```python
values = Series(['a', 'b', 'c', 'a', np.nan])
```

### Step 9: Assign result = values.str.contains(...)

```python
result = values.str.contains('a', na=True)
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, True])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = values.str.contains(...)

```python
result = values.str.contains('a', na=False)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, False])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
values = Series(['a', 'b', 'c', 'a', np.nan], dtype='category')
result = values.str.contains('a', na=True)
expected = Series([True, False, False, True, True])
tm.assert_series_equal(result, expected)
result = values.str.contains('a', na=False)
expected = Series([True, False, False, True, False])
tm.assert_series_equal(result, expected)
values = Series(['a', 'b', 'c', 'a', np.nan])
result = values.str.contains('a', na=True)
expected = Series([True, False, False, True, True])
tm.assert_series_equal(result, expected)
result = values.str.contains('a', na=False)
expected = Series([True, False, False, True, False])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_find_replace.py:135 | Complexity: Advanced | Last updated: 2026-06-02*