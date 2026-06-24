# How To: Categorical Pyarrow

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical pyarrow

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
arr = ['Mon', 'Tue', 'Mon', 'Wed', 'Mon', 'Thu', 'Fri', 'Sat', 'Sun']
```

### Step 3: Assign table = pa.table(...)

```python
table = pa.table({'weekday': pa.array(arr).dictionary_encode()})
```

### Step 4: Assign exchange_df = table.__dataframe__(...)

```python
exchange_df = table.__dataframe__()
```

### Step 5: Assign result = from_dataframe(...)

```python
result = from_dataframe(exchange_df)
```

### Step 6: Assign weekday = pd.Categorical(...)

```python
weekday = pd.Categorical(arr, categories=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'weekday': weekday})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow', '11.0.0')
arr = ['Mon', 'Tue', 'Mon', 'Wed', 'Mon', 'Thu', 'Fri', 'Sat', 'Sun']
table = pa.table({'weekday': pa.array(arr).dictionary_encode()})
exchange_df = table.__dataframe__()
result = from_dataframe(exchange_df)
weekday = pd.Categorical(arr, categories=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
expected = pd.DataFrame({'weekday': weekday})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_impl.py:68 | Complexity: Advanced | Last updated: 2026-06-02*