# How To: Categorical To Numpy Dlpack

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical to numpy dlpack

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core.interchange.column`
- `pandas.core.interchange.dataframe_protocol`
- `pandas.core.interchange.from_dataframe`
- `pandas.core.interchange.utils`
- `pyarrow.interchange`
- `pyarrow.compute`
- `pyarrow.interchange`
- `pyarrow.interchange`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': pd.Categorical(['a', 'b', 'a'])})
```

### Step 2: Assign col = df.__dataframe__.get_column_by_name(...)

```python
col = df.__dataframe__().get_column_by_name('A')
```

### Step 3: Assign result = np.from_dlpack(...)

```python
result = np.from_dlpack(col.get_buffers()['data'][0])
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 0], dtype='int8')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': pd.Categorical(['a', 'b', 'a'])})
col = df.__dataframe__().get_column_by_name('A')
result = np.from_dlpack(col.get_buffers()['data'][0])
expected = np.array([0, 1, 0], dtype='int8')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_impl.py:273 | Complexity: Intermediate | Last updated: 2026-06-02*