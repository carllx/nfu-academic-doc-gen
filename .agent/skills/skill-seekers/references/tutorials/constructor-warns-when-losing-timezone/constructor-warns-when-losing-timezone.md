# How To: Constructor Warns When Losing Timezone

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor warns when losing timezone

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
```

### Step 2: Assign expected = SparseArray(...)

```python
expected = SparseArray(np.asarray(dti, dtype='datetime64[ns]'))
```

### Step 3: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 5: Assign result = SparseArray(...)

```python
result = SparseArray(dti)
```

### Step 6: Assign result = SparseArray(...)

```python
result = SparseArray(pd.Series(dti))
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3, tz='US/Pacific')
expected = SparseArray(np.asarray(dti, dtype='datetime64[ns]'))
with tm.assert_produces_warning(UserWarning):
    result = SparseArray(dti)
tm.assert_sp_array_equal(result, expected)
with tm.assert_produces_warning(UserWarning):
    result = SparseArray(pd.Series(dti))
tm.assert_sp_array_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*