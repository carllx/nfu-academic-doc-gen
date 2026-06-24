# How To: Putmask Multiindex Other

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test putmask multiindex other

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = MultiIndex.from_tuples(...)

```python
left = MultiIndex.from_tuples([(np.nan, 6), (np.nan, 6), ('a', 4)])
```

### Step 2: Assign right = MultiIndex.from_tuples(...)

```python
right = MultiIndex.from_tuples([('a', 1), ('a', 1), ('d', 1)])
```

### Step 3: Assign mask = np.array(...)

```python
mask = np.array([True, True, False])
```

### Step 4: Assign result = left.putmask(...)

```python
result = left.putmask(mask, right)
```

### Step 5: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([right[0], right[1], left[2]])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = MultiIndex.from_tuples([(np.nan, 6), (np.nan, 6), ('a', 4)])
right = MultiIndex.from_tuples([('a', 1), ('a', 1), ('d', 1)])
mask = np.array([True, True, False])
result = left.putmask(mask, right)
expected = MultiIndex.from_tuples([right[0], right[1], left[2]])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*