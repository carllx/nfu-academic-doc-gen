# How To: From Arrays Index Series Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from arrays index series categorical

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = pd.CategoricalIndex(...)

```python
idx1 = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=False)
```

### Step 2: Assign idx2 = pd.CategoricalIndex(...)

```python
idx2 = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=True)
```

### Step 3: Assign result = MultiIndex.from_arrays(...)

```python
result = MultiIndex.from_arrays([idx1, idx2])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(0), idx1)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(1), idx2)
```

### Step 6: Assign result2 = MultiIndex.from_arrays(...)

```python
result2 = MultiIndex.from_arrays([Series(idx1), Series(idx2)])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(0), idx1)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2.get_level_values(1), idx2)
```

### Step 9: Assign result3 = MultiIndex.from_arrays(...)

```python
result3 = MultiIndex.from_arrays([idx1.values, idx2.values])
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result3.get_level_values(0), idx1)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result3.get_level_values(1), idx2)
```


## Complete Example

```python
# Workflow
idx1 = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=False)
idx2 = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=True)
result = MultiIndex.from_arrays([idx1, idx2])
tm.assert_index_equal(result.get_level_values(0), idx1)
tm.assert_index_equal(result.get_level_values(1), idx2)
result2 = MultiIndex.from_arrays([Series(idx1), Series(idx2)])
tm.assert_index_equal(result2.get_level_values(0), idx1)
tm.assert_index_equal(result2.get_level_values(1), idx2)
result3 = MultiIndex.from_arrays([idx1.values, idx2.values])
tm.assert_index_equal(result3.get_level_values(0), idx1)
tm.assert_index_equal(result3.get_level_values(1), idx2)
```

## Next Steps


---

*Source: test_constructors.py:251 | Complexity: Advanced | Last updated: 2026-06-02*