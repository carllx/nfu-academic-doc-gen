# How To: To Numpy Multiindex Series Na Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy multiindex series na value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: data, multiindex, dtype, na_value, expected
```

## Step-by-Step Guide

### Step 1: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples(multiindex)
```

### Step 2: Assign series = Series(...)

```python
series = Series(data, index=index)
```

### Step 3: Assign result = series.to_numpy(...)

```python
result = series.to_numpy(dtype=dtype, na_value=na_value)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array(expected)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, multiindex, dtype, na_value, expected

# Workflow
index = pd.MultiIndex.from_tuples(multiindex)
series = Series(data, index=index)
result = series.to_numpy(dtype=dtype, na_value=na_value)
expected = np.array(expected)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_conversion.py:495 | Complexity: Intermediate | Last updated: 2026-06-02*