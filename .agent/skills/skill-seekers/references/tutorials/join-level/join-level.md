# How To: Join Level

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx, other, join_type
```

## Step-by-Step Guide

### Step 1: Assign unknown = other.join(...)

```python
join_index, lidx, ridx = other.join(idx, how=join_type, level='second', return_indexers=True)
```

**Verification:**
```python
assert join_index.levels[0].equals(idx.levels[0])
```

### Step 2: Assign exp_level = other.join(...)

```python
exp_level = other.join(idx.levels[1], how=join_type)
```

**Verification:**
```python
assert join_index.levels[1].equals(exp_level)
```

### Step 3: Assign mask = np.array(...)

```python
mask = np.array([x[1] in exp_level for x in idx], dtype=bool)
```

**Verification:**
```python
assert join_index.equals(join_index2)
```

### Step 4: Assign exp_values = value

```python
exp_values = idx.values[mask]
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(join_index.values, exp_values)
```

### Step 6: Assign unknown = idx.join(...)

```python
join_index2, ridx2, lidx2 = idx.join(other, how=join_type, level='second', return_indexers=True)
```

**Verification:**
```python
assert join_index.equals(join_index2)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lidx, lidx2)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ridx, ridx2)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(join_index2.values, exp_values)
```


## Complete Example

```python
# Setup
# Fixtures: idx, other, join_type

# Workflow
join_index, lidx, ridx = other.join(idx, how=join_type, level='second', return_indexers=True)
exp_level = other.join(idx.levels[1], how=join_type)
assert join_index.levels[0].equals(idx.levels[0])
assert join_index.levels[1].equals(exp_level)
mask = np.array([x[1] in exp_level for x in idx], dtype=bool)
exp_values = idx.values[mask]
tm.assert_numpy_array_equal(join_index.values, exp_values)
if join_type in ('outer', 'inner'):
    join_index2, ridx2, lidx2 = idx.join(other, how=join_type, level='second', return_indexers=True)
    assert join_index.equals(join_index2)
    tm.assert_numpy_array_equal(lidx, lidx2)
    tm.assert_numpy_array_equal(ridx, ridx2)
    tm.assert_numpy_array_equal(join_index2.values, exp_values)
```

## Next Steps


---

*Source: test_join.py:18 | Complexity: Advanced | Last updated: 2026-06-02*