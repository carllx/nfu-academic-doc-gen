# How To: Codes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test codes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`

**Setup Required:**
```python
# Fixtures: verify, codes, exp_codes
```

## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([3, 1, 2, 0, 4])
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 2, 3, 4])
```

### Step 3: Assign unknown = safe_sort(...)

```python
result, result_codes = safe_sort(values, codes, use_na_sentinel=True, verify=verify)
```

### Step 4: Assign expected_codes = np.array(...)

```python
expected_codes = np.array(exp_codes, dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_codes, expected_codes)
```


## Complete Example

```python
# Setup
# Fixtures: verify, codes, exp_codes

# Workflow
values = np.array([3, 1, 2, 0, 4])
expected = np.array([0, 1, 2, 3, 4])
result, result_codes = safe_sort(values, codes, use_na_sentinel=True, verify=verify)
expected_codes = np.array(exp_codes, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
tm.assert_numpy_array_equal(result_codes, expected_codes)
```

## Next Steps


---

*Source: test_sorting.py:396 | Complexity: Intermediate | Last updated: 2026-06-02*