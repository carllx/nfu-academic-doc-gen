# How To: Dtype Mangle Dup Cols

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dtype mangle dup cols

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
# Fixtures: all_parsers, dtypes, exp_value
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

**Verification:**
```python
assert dtype_dict == dtype_dict_copy, 'dtype dict changed'
```

### Step 2: Assign data = 'a,a\n1,1'

```python
data = 'a,a\n1,1'
```

### Step 3: Assign dtype_dict = value

```python
dtype_dict = {'a': str, **dtypes}
```

### Step 4: Assign dtype_dict_copy = dtype_dict.copy(...)

```python
dtype_dict_copy = dtype_dict.copy()
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype=dtype_dict)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['1'], 'a.1': [exp_value]})
```

**Verification:**
```python
assert dtype_dict == dtype_dict_copy, 'dtype dict changed'
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, dtypes, exp_value

# Workflow
parser = all_parsers
data = 'a,a\n1,1'
dtype_dict = {'a': str, **dtypes}
dtype_dict_copy = dtype_dict.copy()
result = parser.read_csv(StringIO(data), dtype=dtype_dict)
expected = DataFrame({'a': ['1'], 'a.1': [exp_value]})
assert dtype_dict == dtype_dict_copy, 'dtype dict changed'
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:305 | Complexity: Intermediate | Last updated: 2026-06-02*