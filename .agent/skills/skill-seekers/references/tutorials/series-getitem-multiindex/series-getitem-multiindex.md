# How To: Series Getitem Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series getitem multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`

**Setup Required:**
```python
# Fixtures: access_method, level1_value, expected
```

## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 1)], names=['A', 'B'])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], index=mi)
```

### Step 3: Assign expected.index.name = 'A'

```python
expected.index.name = 'A'
```

### Step 4: Assign result = access_method(...)

```python
result = access_method(ser, level1_value)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: access_method, level1_value, expected

# Workflow
mi = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 1)], names=['A', 'B'])
ser = Series([1, 2, 3], index=mi)
expected.index.name = 'A'
result = access_method(ser, level1_value)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*