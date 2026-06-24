# How To: Add Categories Losing Dtype Information

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add categories losing dtype information

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(Series([1, 2], dtype='Int64'))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([4], dtype='Int64')
```

### Step 3: Assign result = cat.add_categories(...)

```python
result = cat.add_categories(ser)
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(Series([1, 2], dtype='Int64'), categories=Series([1, 2, 4], dtype='Int64'))
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 6: Assign cat = Categorical(...)

```python
cat = Categorical(Series(['a', 'b', 'a'], dtype=StringDtype()))
```

### Step 7: Assign ser = Series(...)

```python
ser = Series(['d'], dtype=StringDtype())
```

### Step 8: Assign result = cat.add_categories(...)

```python
result = cat.add_categories(ser)
```

### Step 9: Assign expected = Categorical(...)

```python
expected = Categorical(Series(['a', 'b', 'a'], dtype=StringDtype()), categories=Series(['a', 'b', 'd'], dtype=StringDtype()))
```

### Step 10: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(Series([1, 2], dtype='Int64'))
ser = Series([4], dtype='Int64')
result = cat.add_categories(ser)
expected = Categorical(Series([1, 2], dtype='Int64'), categories=Series([1, 2, 4], dtype='Int64'))
tm.assert_categorical_equal(result, expected)
cat = Categorical(Series(['a', 'b', 'a'], dtype=StringDtype()))
ser = Series(['d'], dtype=StringDtype())
result = cat.add_categories(ser)
expected = Categorical(Series(['a', 'b', 'a'], dtype=StringDtype()), categories=Series(['a', 'b', 'd'], dtype=StringDtype()))
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_api.py:194 | Complexity: Advanced | Last updated: 2026-06-02*