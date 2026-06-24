# How To: Unique Bad Unicode

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unique bad unicode

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign uval = '\ud83d'

```python
uval = '\ud83d'
```

### Step 2: Assign obj = index_or_series(...)

```python
obj = index_or_series([uval] * 2, dtype=object)
```

### Step 3: Assign result = obj.unique(...)

```python
result = obj.unique()
```

### Step 4: Assign expected = pd.Index(...)

```python
expected = pd.Index(['\ud83d'], dtype=object)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array(['\ud83d'], dtype=object)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
uval = '\ud83d'
obj = index_or_series([uval] * 2, dtype=object)
result = obj.unique()
if isinstance(obj, pd.Index):
    expected = pd.Index(['\ud83d'], dtype=object)
    tm.assert_index_equal(result, expected, exact=True)
else:
    expected = np.array(['\ud83d'], dtype=object)
    tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_unique.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*