# How To: Concat Periodarray 2D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat periodarray 2d

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = pd.period_range(...)

```python
pi = pd.period_range('2016-01-01', periods=36, freq='D')
```

### Step 2: Assign arr = pi._data.reshape(...)

```python
arr = pi._data.reshape(6, 6)
```

### Step 3: Assign result = _concat.concat_compat(...)

```python
result = _concat.concat_compat([arr[:2], arr[2:]], axis=0)
```

### Step 4: Call tm.assert_period_array_equal()

```python
tm.assert_period_array_equal(result, arr)
```

### Step 5: Assign result = _concat.concat_compat(...)

```python
result = _concat.concat_compat([arr[:, :2], arr[:, 2:]], axis=1)
```

### Step 6: Call tm.assert_period_array_equal()

```python
tm.assert_period_array_equal(result, arr)
```

### Step 7: Assign msg = 'all the input array dimensions.* for the concatenation axis must match exactly'

```python
msg = 'all the input array dimensions.* for the concatenation axis must match exactly'
```

### Step 8: Call _concat.concat_compat()

```python
_concat.concat_compat([arr[:, :2], arr[:, 2:]], axis=0)
```

### Step 9: Call _concat.concat_compat()

```python
_concat.concat_compat([arr[:2], arr[2:]], axis=1)
```


## Complete Example

```python
# Workflow
pi = pd.period_range('2016-01-01', periods=36, freq='D')
arr = pi._data.reshape(6, 6)
result = _concat.concat_compat([arr[:2], arr[2:]], axis=0)
tm.assert_period_array_equal(result, arr)
result = _concat.concat_compat([arr[:, :2], arr[:, 2:]], axis=1)
tm.assert_period_array_equal(result, arr)
msg = 'all the input array dimensions.* for the concatenation axis must match exactly'
with pytest.raises(ValueError, match=msg):
    _concat.concat_compat([arr[:, :2], arr[:, 2:]], axis=0)
with pytest.raises(ValueError, match=msg):
    _concat.concat_compat([arr[:2], arr[2:]], axis=1)
```

## Next Steps


---

*Source: test_concat.py:34 | Complexity: Advanced | Last updated: 2026-06-02*