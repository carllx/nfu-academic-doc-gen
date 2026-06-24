# How To: Map Na Action Ignore

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map na action ignore

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`
- `pandas.core.arrays.floating`
- `pandas.core.arrays.integer`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data_missing_for_sorting
```

## Step-by-Step Guide

### Step 1: Assign zero = value

```python
zero = data_missing_for_sorting[2]
```

### Step 2: Assign result = data_missing_for_sorting.map(...)

```python
result = data_missing_for_sorting.map(lambda x: zero, na_action='ignore')
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([False, pd.NA, False], dtype=object)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([zero, np.nan, zero])
```


## Complete Example

```python
# Setup
# Fixtures: data_missing_for_sorting

# Workflow
zero = data_missing_for_sorting[2]
result = data_missing_for_sorting.map(lambda x: zero, na_action='ignore')
if data_missing_for_sorting.dtype.kind == 'b':
    expected = np.array([False, pd.NA, False], dtype=object)
else:
    expected = np.array([zero, np.nan, zero])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_masked.py:182 | Complexity: Intermediate | Last updated: 2026-06-02*