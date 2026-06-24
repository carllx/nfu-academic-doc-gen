# How To: Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = pd.Series(...)

```python
s = pd.Series([[0, 1, 2], np.nan, [], (3, 4)], name='foo', index=pd.MultiIndex.from_product([list('ab'), range(2)], names=['foo', 'bar']))
```

### Step 2: Assign result = s.explode(...)

```python
result = s.explode()
```

### Step 3: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples([('a', 0), ('a', 0), ('a', 0), ('a', 1), ('b', 0), ('b', 1), ('b', 1)], names=['foo', 'bar'])
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=index, dtype=object, name='foo')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = pd.Series([[0, 1, 2], np.nan, [], (3, 4)], name='foo', index=pd.MultiIndex.from_product([list('ab'), range(2)], names=['foo', 'bar']))
result = s.explode()
index = pd.MultiIndex.from_tuples([('a', 0), ('a', 0), ('a', 0), ('a', 1), ('b', 0), ('b', 1), ('b', 1)], names=['foo', 'bar'])
expected = pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=index, dtype=object, name='foo')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_explode.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*