# How To: Stack Preserves Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test stack preserves na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`

**Setup Required:**
```python
# Fixtures: dtype, na_value, test_multiindex
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1]}, index=index)
```

### Step 2: Assign result = df.stack(...)

```python
result = df.stack(future_stack=True)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(1, index=expected_index)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(2 * [Index([na_value], dtype=dtype)])
```

### Step 6: Assign index = Index(...)

```python
index = Index([na_value], dtype=dtype)
```

### Step 7: Assign expected_index = MultiIndex.from_arrays(...)

```python
expected_index = MultiIndex.from_arrays([Index([na_value], dtype=dtype), Index([na_value], dtype=dtype), Index(['a'])])
```

### Step 8: Assign expected_index = MultiIndex.from_arrays(...)

```python
expected_index = MultiIndex.from_arrays([Index([na_value], dtype=dtype), Index(['a'])])
```


## Complete Example

```python
# Setup
# Fixtures: dtype, na_value, test_multiindex

# Workflow
if test_multiindex:
    index = MultiIndex.from_arrays(2 * [Index([na_value], dtype=dtype)])
else:
    index = Index([na_value], dtype=dtype)
df = DataFrame({'a': [1]}, index=index)
result = df.stack(future_stack=True)
if test_multiindex:
    expected_index = MultiIndex.from_arrays([Index([na_value], dtype=dtype), Index([na_value], dtype=dtype), Index(['a'])])
else:
    expected_index = MultiIndex.from_arrays([Index([na_value], dtype=dtype), Index(['a'])])
expected = Series(1, index=expected_index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:2659 | Complexity: Advanced | Last updated: 2026-06-02*