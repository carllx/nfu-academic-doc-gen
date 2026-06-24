# How To: To Numpy Int With Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numpy int with na

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `decimal`
- `io`
- `operator`
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.api.types`
- `pandas.tests.extension`
- `pandas.core.arrays.arrow.array`
- `pandas.core.arrays.arrow.extension_types`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1, None]
```

**Verification:**
```python
assert isinstance(result[0], float)
```

### Step 2: Assign arr = pd.array(...)

```python
arr = pd.array(data, dtype='int64[pyarrow]')
```

### Step 3: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy()
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([1, np.nan])
```

**Verification:**
```python
assert isinstance(result[0], float)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [1, None]
arr = pd.array(data, dtype='int64[pyarrow]')
result = arr.to_numpy()
expected = np.array([1, np.nan])
assert isinstance(result[0], float)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow.py:1564 | Complexity: Intermediate | Last updated: 2026-06-02*