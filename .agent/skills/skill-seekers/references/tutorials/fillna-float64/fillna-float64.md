# How To: Fillna Float64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna float64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index_cls = Index

```python
index_cls = Index
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([1.0, np.nan, 3.0], dtype=float, name='x')
```

### Step 3: Assign exp = Index(...)

```python
exp = Index([1.0, 0.1, 3.0], name='x')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(0.1), exp, exact=True)
```

### Step 5: Assign exp = index_cls(...)

```python
exp = index_cls([1.0, 2.0, 3.0], name='x')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(2), exp)
```

### Step 7: Assign exp = Index(...)

```python
exp = Index([1.0, 'obj', 3.0], name='x')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna('obj'), exp, exact=True)
```


## Complete Example

```python
# Workflow
index_cls = Index
idx = Index([1.0, np.nan, 3.0], dtype=float, name='x')
exp = Index([1.0, 0.1, 3.0], name='x')
tm.assert_index_equal(idx.fillna(0.1), exp, exact=True)
exp = index_cls([1.0, 2.0, 3.0], name='x')
tm.assert_index_equal(idx.fillna(2), exp)
exp = Index([1.0, 'obj', 3.0], name='x')
tm.assert_index_equal(idx.fillna('obj'), exp, exact=True)
```

## Next Steps


---

*Source: test_numeric.py:214 | Complexity: Advanced | Last updated: 2026-06-02*