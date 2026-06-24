# How To: Object Dtype Series Set Series Element

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test object dtype series set series element

## Prerequisites

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series(dtype='O', index=['a', 'b'])
```

### Step 2: Assign unknown = Series(...)

```python
s1['a'] = Series()
```

### Step 3: Assign unknown = Series(...)

```python
s1.loc['b'] = Series()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1.loc['a'], Series())
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1.loc['b'], Series())
```

### Step 6: Assign s2 = Series(...)

```python
s2 = Series(dtype='O', index=['a', 'b'])
```

### Step 7: Assign unknown = Series(...)

```python
s2.iloc[1] = Series()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s2.iloc[1], Series())
```


## Complete Example

```python
# Workflow
s1 = Series(dtype='O', index=['a', 'b'])
s1['a'] = Series()
s1.loc['b'] = Series()
tm.assert_series_equal(s1.loc['a'], Series())
tm.assert_series_equal(s1.loc['b'], Series())
s2 = Series(dtype='O', index=['a', 'b'])
s2.iloc[1] = Series()
tm.assert_series_equal(s2.iloc[1], Series())
```

## Next Steps


---

*Source: test_indexing.py:1144 | Complexity: Advanced | Last updated: 2026-06-02*