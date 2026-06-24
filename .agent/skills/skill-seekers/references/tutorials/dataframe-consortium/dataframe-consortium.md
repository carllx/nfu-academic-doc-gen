# How To: Dataframe Consortium

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test some basic methods of the dataframe consortium standard.

Full testing is done at https://github.com/data-apis/dataframe-api-compat,
this is just to check that the entry point works as expected.

## Prerequisites

**Required Modules:**
- `array`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.util.version`
- `sklearn`
- `dask.array`
- `xarray`


## Step-by-Step Guide

### Step 1: '\n    Test some basic methods of the dataframe consortium standard.\n\n    Full testing is done at https://github.com/data-apis/dataframe-api-compat,\n    this is just to check that the entry point works as expected.\n    '

```python
'\n    Test some basic methods of the dataframe consortium standard.\n\n    Full testing is done at https://github.com/data-apis/dataframe-api-compat,\n    this is just to check that the entry point works as expected.\n    '
```

**Verification:**
```python
assert result_1 == expected_1
```

### Step 2: Call pytest.importorskip()

```python
pytest.importorskip('dataframe_api_compat')
```

**Verification:**
```python
assert col.name == 'a'
```

### Step 3: Assign df_pd = DataFrame(...)

```python
df_pd = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 4: Assign df = df_pd.__dataframe_consortium_standard__(...)

```python
df = df_pd.__dataframe_consortium_standard__()
```

### Step 5: Assign result_1 = df.get_column_names(...)

```python
result_1 = df.get_column_names()
```

### Step 6: Assign expected_1 = value

```python
expected_1 = ['a', 'b']
```

**Verification:**
```python
assert result_1 == expected_1
```

### Step 7: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='a')
```

### Step 8: Assign col = ser.__column_consortium_standard__(...)

```python
col = ser.__column_consortium_standard__()
```

**Verification:**
```python
assert col.name == 'a'
```


## Complete Example

```python
# Workflow
'\n    Test some basic methods of the dataframe consortium standard.\n\n    Full testing is done at https://github.com/data-apis/dataframe-api-compat,\n    this is just to check that the entry point works as expected.\n    '
pytest.importorskip('dataframe_api_compat')
df_pd = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df = df_pd.__dataframe_consortium_standard__()
result_1 = df.get_column_names()
expected_1 = ['a', 'b']
assert result_1 == expected_1
ser = Series([1, 2, 3], name='a')
col = ser.__column_consortium_standard__()
assert col.name == 'a'
```

## Next Steps


---

*Source: test_downstream.py:336 | Complexity: Advanced | Last updated: 2026-06-02*