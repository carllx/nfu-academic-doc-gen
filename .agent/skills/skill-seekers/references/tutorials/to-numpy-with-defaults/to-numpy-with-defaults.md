# How To: To Numpy With Defaults

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numpy with defaults

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign result = data.to_numpy(...)

```python
result = data.to_numpy()
```

### Step 2: Assign pa_type = value

```python
pa_type = data._pa_array.type
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Call pytest.skip()

```python
pytest.skip('Tested in test_to_numpy_temporal')
```

### Step 5: Assign expected = expected.astype(...)

```python
expected = expected.astype(object)
```

### Step 6: Assign unknown = value

```python
expected[pd.isna(data)] = pd.NA
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array(list(data))
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array(data._pa_array)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
result = data.to_numpy()
pa_type = data._pa_array.type
if pa.types.is_duration(pa_type) or pa.types.is_timestamp(pa_type):
    pytest.skip('Tested in test_to_numpy_temporal')
elif pa.types.is_date(pa_type):
    expected = np.array(list(data))
else:
    expected = np.array(data._pa_array)
if data._hasna and (not is_numeric_dtype(data.dtype)):
    expected = expected.astype(object)
    expected[pd.isna(data)] = pd.NA
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow.py:1545 | Complexity: Advanced | Last updated: 2026-06-02*