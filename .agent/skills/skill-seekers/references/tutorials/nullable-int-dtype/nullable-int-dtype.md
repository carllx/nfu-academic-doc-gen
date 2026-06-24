# How To: Nullable Int Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nullable int dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers, any_int_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign dtype = any_int_ea_dtype

```python
dtype = any_int_ea_dtype
```

### Step 3: Assign data = 'a,b,c\n,3,5\n1,,6\n2,4,'

```python
data = 'a,b,c\n,3,5\n1,,6\n2,4,'
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': pd.array([pd.NA, 1, 2], dtype=dtype), 'b': pd.array([3, pd.NA, 4], dtype=dtype), 'c': pd.array([5, 6, pd.NA], dtype=dtype)})
```

### Step 5: Assign actual = parser.read_csv(...)

```python
actual = parser.read_csv(StringIO(data), dtype=dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, any_int_ea_dtype

# Workflow
parser = all_parsers
dtype = any_int_ea_dtype
data = 'a,b,c\n,3,5\n1,,6\n2,4,'
expected = DataFrame({'a': pd.array([pd.NA, 1, 2], dtype=dtype), 'b': pd.array([3, pd.NA, 4], dtype=dtype), 'c': pd.array([5, 6, pd.NA], dtype=dtype)})
actual = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:355 | Complexity: Intermediate | Last updated: 2026-06-02*