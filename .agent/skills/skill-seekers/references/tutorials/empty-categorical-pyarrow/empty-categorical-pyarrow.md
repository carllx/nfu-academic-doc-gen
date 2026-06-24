# How To: Empty Categorical Pyarrow

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty categorical pyarrow

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

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow', '11.0.0')
```

### Step 2: Assign arr = value

```python
arr = [None]
```

### Step 3: Assign table = pa.table(...)

```python
table = pa.table({'arr': pa.array(arr, 'float64').dictionary_encode()})
```

### Step 4: Assign exchange_df = table.__dataframe__(...)

```python
exchange_df = table.__dataframe__()
```

### Step 5: Assign result = pd.api.interchange.from_dataframe(...)

```python
result = pd.api.interchange.from_dataframe(exchange_df)
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'arr': pd.Categorical([np.nan])})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow', '11.0.0')
arr = [None]
table = pa.table({'arr': pa.array(arr, 'float64').dictionary_encode()})
exchange_df = table.__dataframe__()
result = pd.api.interchange.from_dataframe(exchange_df)
expected = pd.DataFrame({'arr': pd.Categorical([np.nan])})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_impl.py:83 | Complexity: Intermediate | Last updated: 2026-06-02*