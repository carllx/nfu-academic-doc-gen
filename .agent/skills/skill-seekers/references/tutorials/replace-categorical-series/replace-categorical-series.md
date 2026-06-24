# How To: Replace Categorical Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace categorical series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: to_replace, value, expected, flip_categories
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([1, 2, 3], dtype='category')
```

### Step 2: Assign result = ser.replace(...)

```python
result = ser.replace(to_replace, value)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(expected, dtype='category')
```

### Step 4: Call ser.replace()

```python
ser.replace(to_replace, value, inplace=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result, check_category_order=False)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, ser, check_category_order=False)
```

### Step 7: Assign expected = expected.cat.set_categories(...)

```python
expected = expected.cat.set_categories(expected.cat.categories[::-1])
```


## Complete Example

```python
# Setup
# Fixtures: to_replace, value, expected, flip_categories

# Workflow
ser = pd.Series([1, 2, 3], dtype='category')
result = ser.replace(to_replace, value)
expected = pd.Series(expected, dtype='category')
ser.replace(to_replace, value, inplace=True)
if flip_categories:
    expected = expected.cat.set_categories(expected.cat.categories[::-1])
tm.assert_series_equal(expected, result, check_category_order=False)
tm.assert_series_equal(expected, ser, check_category_order=False)
```

## Next Steps


---

*Source: test_replace.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*