# How To: Na Levels

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na levels

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

### Step 1: Assign result = MultiIndex(...)

```python
result = MultiIndex(levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[0, -1, 1, 2, 3, 4]])
```

### Step 2: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[-1, -1, -1, -1, 3, 4]])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign result = MultiIndex(...)

```python
result = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[0, -1, 1, 2, 3, 4]])
```

### Step 5: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[-1, -1, 1, -1, 3, -1]])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = MultiIndex.set_levels(...)

```python
result = MultiIndex(levels=[[1, 2, 3, 4, 5]], codes=[[0, -1, 1, 2, 3, 4]]).set_levels([[np.nan, 's', pd.NaT, 128, None]])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = MultiIndex.set_codes(...)

```python
result = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[1, 2, 2, 2, 2, 2]]).set_codes([[0, -1, 1, 2, 3, 4]])
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = MultiIndex(levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[0, -1, 1, 2, 3, 4]])
expected = MultiIndex(levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[-1, -1, -1, -1, 3, 4]])
tm.assert_index_equal(result, expected)
result = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[0, -1, 1, 2, 3, 4]])
expected = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[-1, -1, 1, -1, 3, -1]])
tm.assert_index_equal(result, expected)
result = MultiIndex(levels=[[1, 2, 3, 4, 5]], codes=[[0, -1, 1, 2, 3, 4]]).set_levels([[np.nan, 's', pd.NaT, 128, None]])
tm.assert_index_equal(result, expected)
result = MultiIndex(levels=[[np.nan, 's', pd.NaT, 128, None]], codes=[[1, 2, 2, 2, 2, 2]]).set_codes([[0, -1, 1, 2, 3, 4]])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:107 | Complexity: Advanced | Last updated: 2026-06-02*