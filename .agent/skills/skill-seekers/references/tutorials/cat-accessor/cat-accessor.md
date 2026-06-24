# How To: Cat Accessor

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cat accessor

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`
- `pandas.core.indexes.accessors`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(Categorical(['a', 'b', np.nan, 'a']))
```

**Verification:**
```python
assert not ser.cat.ordered, False
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ser.cat.categories, Index(['a', 'b']))
```

**Verification:**
```python
assert not ser.cat.ordered, False
```

### Step 3: Assign exp = Categorical(...)

```python
exp = Categorical(['a', 'b', np.nan, 'a'], categories=['b', 'a'])
```

### Step 4: Assign res = ser.cat.set_categories(...)

```python
res = ser.cat.set_categories(['b', 'a'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res.values, exp)
```

### Step 6: Assign unknown = 'a'

```python
ser[:] = 'a'
```

### Step 7: Assign ser = ser.cat.remove_unused_categories(...)

```python
ser = ser.cat.remove_unused_categories()
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ser.cat.categories, Index(['a']))
```


## Complete Example

```python
# Workflow
ser = Series(Categorical(['a', 'b', np.nan, 'a']))
tm.assert_index_equal(ser.cat.categories, Index(['a', 'b']))
assert not ser.cat.ordered, False
exp = Categorical(['a', 'b', np.nan, 'a'], categories=['b', 'a'])
res = ser.cat.set_categories(['b', 'a'])
tm.assert_categorical_equal(res.values, exp)
ser[:] = 'a'
ser = ser.cat.remove_unused_categories()
tm.assert_index_equal(ser.cat.categories, Index(['a']))
```

## Next Steps


---

*Source: test_cat_accessor.py:40 | Complexity: Advanced | Last updated: 2026-06-02*