# How To: Convert Dtypes Pyarrow Null

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert dtypes pyarrow null

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series([None, None])
```

### Step 3: Assign result = ser.convert_dtypes(...)

```python
result = ser.convert_dtypes(dtype_backend='pyarrow')
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([None, None], dtype=pd.ArrowDtype(pa.null()))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
ser = pd.Series([None, None])
result = ser.convert_dtypes(dtype_backend='pyarrow')
expected = pd.Series([None, None], dtype=pd.ArrowDtype(pa.null()))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_convert_dtypes.py:303 | Complexity: Intermediate | Last updated: 2026-06-02*