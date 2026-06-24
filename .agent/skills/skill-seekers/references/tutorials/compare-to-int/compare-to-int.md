# How To: Compare To Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare to int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.arrays.masked_shared`

**Setup Required:**
```python
# Fixtures: dtype, comparison_op
```

## Step-by-Step Guide

### Step 1: Assign op_name = value

```python
op_name = f'__{comparison_op.__name__}__'
```

### Step 2: Assign s1 = pd.Series(...)

```python
s1 = pd.Series([1, None, 3], dtype=dtype)
```

### Step 3: Assign s2 = pd.Series(...)

```python
s2 = pd.Series([1, None, 3], dtype='float')
```

### Step 4: Assign method = getattr(...)

```python
method = getattr(s1, op_name)
```

### Step 5: Assign result = method(...)

```python
result = method(2)
```

### Step 6: Assign method = getattr(...)

```python
method = getattr(s2, op_name)
```

### Step 7: Assign expected = method.astype(...)

```python
expected = method(2).astype('boolean')
```

### Step 8: Assign unknown = value

```python
expected[s2.isna()] = pd.NA
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, comparison_op

# Workflow
op_name = f'__{comparison_op.__name__}__'
s1 = pd.Series([1, None, 3], dtype=dtype)
s2 = pd.Series([1, None, 3], dtype='float')
method = getattr(s1, op_name)
result = method(2)
method = getattr(s2, op_name)
expected = method(2).astype('boolean')
expected[s2.isna()] = pd.NA
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_comparison.py:16 | Complexity: Advanced | Last updated: 2026-06-02*