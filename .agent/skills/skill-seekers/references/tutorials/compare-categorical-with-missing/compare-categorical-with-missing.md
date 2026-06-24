# How To: Compare Categorical With Missing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare categorical with missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: a1, a2, categories
```

## Step-by-Step Guide

### Step 1: Assign cat_type = CategoricalDtype(...)

```python
cat_type = CategoricalDtype(categories)
```

### Step 2: Assign result = value

```python
result = Series(a1, dtype=cat_type) != Series(a2, dtype=cat_type)
```

### Step 3: Assign expected = value

```python
expected = Series(a1) != Series(a2)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = Series(a1, dtype=cat_type) == Series(a2, dtype=cat_type)
```

### Step 6: Assign expected = value

```python
expected = Series(a1) == Series(a2)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: a1, a2, categories

# Workflow
cat_type = CategoricalDtype(categories)
result = Series(a1, dtype=cat_type) != Series(a2, dtype=cat_type)
expected = Series(a1) != Series(a2)
tm.assert_series_equal(result, expected)
result = Series(a1, dtype=cat_type) == Series(a2, dtype=cat_type)
expected = Series(a1) == Series(a2)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:190 | Complexity: Intermediate | Last updated: 2026-06-02*