# How To: Append Mixed Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append mixed dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2011-01-01', freq='ME', periods=3)
```

**Verification:**
```python
assert mi.nlevels == 6
```

### Step 2: Assign dti_tz = date_range(...)

```python
dti_tz = date_range('2011-01-01', freq='ME', periods=3, tz='US/Eastern')
```

### Step 3: Assign pi = period_range(...)

```python
pi = period_range('2011-01', freq='M', periods=3)
```

### Step 4: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[1, 2, 3], [1.1, np.nan, 3.3], ['a', 'b', 'c'], dti, dti_tz, pi])
```

**Verification:**
```python
assert mi.nlevels == 6
```

### Step 5: Assign res = mi.append(...)

```python
res = mi.append(mi)
```

### Step 6: Assign exp = MultiIndex.from_arrays(...)

```python
exp = MultiIndex.from_arrays([[1, 2, 3, 1, 2, 3], [1.1, np.nan, 3.3, 1.1, np.nan, 3.3], ['a', 'b', 'c', 'a', 'b', 'c'], dti.append(dti), dti_tz.append(dti_tz), pi.append(pi)])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 8: Assign other = MultiIndex.from_arrays(...)

```python
other = MultiIndex.from_arrays([['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z']])
```

### Step 9: Assign res = mi.append(...)

```python
res = mi.append(other)
```

### Step 10: Assign exp = MultiIndex.from_arrays(...)

```python
exp = MultiIndex.from_arrays([[1, 2, 3, 'x', 'y', 'z'], [1.1, np.nan, 3.3, 'x', 'y', 'z'], ['a', 'b', 'c', 'x', 'y', 'z'], dti.append(Index(['x', 'y', 'z'])), dti_tz.append(Index(['x', 'y', 'z'])), pi.append(Index(['x', 'y', 'z']))])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```


## Complete Example

```python
# Workflow
dti = date_range('2011-01-01', freq='ME', periods=3)
dti_tz = date_range('2011-01-01', freq='ME', periods=3, tz='US/Eastern')
pi = period_range('2011-01', freq='M', periods=3)
mi = MultiIndex.from_arrays([[1, 2, 3], [1.1, np.nan, 3.3], ['a', 'b', 'c'], dti, dti_tz, pi])
assert mi.nlevels == 6
res = mi.append(mi)
exp = MultiIndex.from_arrays([[1, 2, 3, 1, 2, 3], [1.1, np.nan, 3.3, 1.1, np.nan, 3.3], ['a', 'b', 'c', 'a', 'b', 'c'], dti.append(dti), dti_tz.append(dti_tz), pi.append(pi)])
tm.assert_index_equal(res, exp)
other = MultiIndex.from_arrays([['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z'], ['x', 'y', 'z']])
res = mi.append(other)
exp = MultiIndex.from_arrays([[1, 2, 3, 'x', 'y', 'z'], [1.1, np.nan, 3.3, 'x', 'y', 'z'], ['a', 'b', 'c', 'x', 'y', 'z'], dti.append(Index(['x', 'y', 'z'])), dti_tz.append(Index(['x', 'y', 'z'])), pi.append(Index(['x', 'y', 'z']))])
tm.assert_index_equal(res, exp)
```

## Next Steps


---

*Source: test_analytics.py:99 | Complexity: Advanced | Last updated: 2026-06-02*