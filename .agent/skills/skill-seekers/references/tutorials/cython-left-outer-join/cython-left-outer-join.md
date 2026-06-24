# How To: Cython Left Outer Join

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython left outer join

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.join`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = np.array(...)

```python
left = np.array([0, 1, 2, 1, 2, 0, 0, 1, 2, 3, 3], dtype=np.intp)
```

### Step 2: Assign right = np.array(...)

```python
right = np.array([1, 1, 0, 4, 2, 2, 1], dtype=np.intp)
```

### Step 3: Assign max_group = 5

```python
max_group = 5
```

### Step 4: Assign unknown = left_outer_join(...)

```python
ls, rs = left_outer_join(left, right, max_group)
```

### Step 5: Assign exp_ls = left.argsort(...)

```python
exp_ls = left.argsort(kind='mergesort')
```

### Step 6: Assign exp_rs = right.argsort(...)

```python
exp_rs = right.argsort(kind='mergesort')
```

### Step 7: Assign exp_li = np.array(...)

```python
exp_li = np.array([0, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10])
```

### Step 8: Assign exp_ri = np.array(...)

```python
exp_ri = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5, -1, -1])
```

### Step 9: Assign exp_ls = exp_ls.take(...)

```python
exp_ls = exp_ls.take(exp_li)
```

### Step 10: Assign unknown = value

```python
exp_ls[exp_li == -1] = -1
```

### Step 11: Assign exp_rs = exp_rs.take(...)

```python
exp_rs = exp_rs.take(exp_ri)
```

### Step 12: Assign unknown = value

```python
exp_rs[exp_ri == -1] = -1
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ls, exp_ls, check_dtype=False)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(rs, exp_rs, check_dtype=False)
```


## Complete Example

```python
# Workflow
left = np.array([0, 1, 2, 1, 2, 0, 0, 1, 2, 3, 3], dtype=np.intp)
right = np.array([1, 1, 0, 4, 2, 2, 1], dtype=np.intp)
max_group = 5
ls, rs = left_outer_join(left, right, max_group)
exp_ls = left.argsort(kind='mergesort')
exp_rs = right.argsort(kind='mergesort')
exp_li = np.array([0, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10])
exp_ri = np.array([0, 0, 0, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5, -1, -1])
exp_ls = exp_ls.take(exp_li)
exp_ls[exp_li == -1] = -1
exp_rs = exp_rs.take(exp_ri)
exp_rs[exp_ri == -1] = -1
tm.assert_numpy_array_equal(ls, exp_ls, check_dtype=False)
tm.assert_numpy_array_equal(rs, exp_rs, check_dtype=False)
```

## Next Steps


---

*Source: test_join.py:48 | Complexity: Advanced | Last updated: 2026-06-02*