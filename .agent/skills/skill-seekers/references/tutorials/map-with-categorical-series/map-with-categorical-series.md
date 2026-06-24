# How To: Map With Categorical Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map with categorical series

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Index(...)

```python
a = Index([1, 2, 3, 4])
```

### Step 2: Assign b = Series(...)

```python
b = Series(['even', 'odd', 'even', 'odd'], dtype='category')
```

### Step 3: Assign c = Series(...)

```python
c = Series(['even', 'odd', 'even', 'odd'])
```

### Step 4: Assign exp = CategoricalIndex(...)

```python
exp = CategoricalIndex(['odd', 'even', 'odd', np.nan])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(a.map(b), exp)
```

### Step 6: Assign exp = Index(...)

```python
exp = Index(['odd', 'even', 'odd', np.nan])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(a.map(c), exp)
```


## Complete Example

```python
# Workflow
a = Index([1, 2, 3, 4])
b = Series(['even', 'odd', 'even', 'odd'], dtype='category')
c = Series(['even', 'odd', 'even', 'odd'])
exp = CategoricalIndex(['odd', 'even', 'odd', np.nan])
tm.assert_index_equal(a.map(b), exp)
exp = Index(['odd', 'even', 'odd', np.nan])
tm.assert_index_equal(a.map(c), exp)
```

## Next Steps


---

*Source: test_map.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*