# How To: Map Category Numeric

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map category numeric

## Prerequisites

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series(['a', 'b', 'c', 'd'])
```

### Step 2: Assign b = Series(...)

```python
b = Series([1, 2, 3, 4], index=pd.CategoricalIndex(['b', 'c', 'd', 'e']))
```

### Step 3: Assign c = Series(...)

```python
c = Series([1, 2, 3, 4], index=Index(['b', 'c', 'd', 'e']))
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([np.nan, 1, 2, 3])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(a.map(b), exp)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series([np.nan, 1, 2, 3])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(a.map(c), exp)
```


## Complete Example

```python
# Workflow
a = Series(['a', 'b', 'c', 'd'])
b = Series([1, 2, 3, 4], index=pd.CategoricalIndex(['b', 'c', 'd', 'e']))
c = Series([1, 2, 3, 4], index=Index(['b', 'c', 'd', 'e']))
exp = Series([np.nan, 1, 2, 3])
tm.assert_series_equal(a.map(b), exp)
exp = Series([np.nan, 1, 2, 3])
tm.assert_series_equal(a.map(c), exp)
```

## Next Steps


---

*Source: test_map.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*