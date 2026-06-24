# How To: Select Dtypes Exclude Include Using List Like

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes exclude include using list like

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6, dtype='u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
```

### Step 2: Assign exclude = value

```python
exclude = (np.datetime64,)
```

### Step 3: Assign include = value

```python
include = (np.bool_, 'integer')
```

### Step 4: Assign r = df.select_dtypes(...)

```python
r = df.select_dtypes(include=include, exclude=exclude)
```

### Step 5: Assign e = value

```python
e = df[['b', 'c', 'e']]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(r, e)
```

### Step 7: Assign exclude = value

```python
exclude = ('datetime',)
```

### Step 8: Assign include = value

```python
include = ('bool', 'int64', 'int32')
```

### Step 9: Assign r = df.select_dtypes(...)

```python
r = df.select_dtypes(include=include, exclude=exclude)
```

### Step 10: Assign e = value

```python
e = df[['b', 'e']]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(r, e)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6, dtype='u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
exclude = (np.datetime64,)
include = (np.bool_, 'integer')
r = df.select_dtypes(include=include, exclude=exclude)
e = df[['b', 'c', 'e']]
tm.assert_frame_equal(r, e)
exclude = ('datetime',)
include = ('bool', 'int64', 'int32')
r = df.select_dtypes(include=include, exclude=exclude)
e = df[['b', 'e']]
tm.assert_frame_equal(r, e)
```

## Next Steps


---

*Source: test_select_dtypes.py:123 | Complexity: Advanced | Last updated: 2026-06-02*