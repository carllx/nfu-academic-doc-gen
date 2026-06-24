# How To: Numba Vs Python String Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numba vs python string index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(1, index=Index(['a', 'b'], dtype=pd.StringDtype(na_value=np.nan)), columns=Index(['x', 'y'], dtype=pd.StringDtype(na_value=np.nan)))
```

### Step 2: Assign func = value

```python
func = lambda x: x
```

### Step 3: Assign result = df.apply(...)

```python
result = df.apply(func, engine='numba', axis=0)
```

### Step 4: Assign expected = df.apply(...)

```python
expected = df.apply(func, engine='python', axis=0)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_column_type=False, check_index_type=False)
```


## Complete Example

```python
# Workflow
df = DataFrame(1, index=Index(['a', 'b'], dtype=pd.StringDtype(na_value=np.nan)), columns=Index(['x', 'y'], dtype=pd.StringDtype(na_value=np.nan)))
func = lambda x: x
result = df.apply(func, engine='numba', axis=0)
expected = df.apply(func, engine='python', axis=0)
tm.assert_frame_equal(result, expected, check_column_type=False, check_index_type=False)
```

## Next Steps


---

*Source: test_numba.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*