# How To: Frame Equal Index Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame equal index mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_like, obj_fixture, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign msg = value

```python
msg = f"{obj_fixture}\\.index are different\n\n{obj_fixture}\\.index values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\['a', 'b', 'c'\\], dtype='{dtype}'\\)\n\\[right\\]: Index\\(\\['a', 'b', 'd'\\], dtype='{dtype}'\\)\nAt positional index 2, first diff: c != d"
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'd'])
```

### Step 4: Assign dtype = 'str'

```python
dtype = 'str'
```

### Step 5: Assign dtype = 'object'

```python
dtype = 'object'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2, check_like=check_like, obj=obj_fixture)
```


## Complete Example

```python
# Setup
# Fixtures: check_like, obj_fixture, using_infer_string

# Workflow
if using_infer_string:
    dtype = 'str'
else:
    dtype = 'object'
msg = f"{obj_fixture}\\.index are different\n\n{obj_fixture}\\.index values are different \\(33\\.33333 %\\)\n\\[left\\]:  Index\\(\\['a', 'b', 'c'\\], dtype='{dtype}'\\)\n\\[right\\]: Index\\(\\['a', 'b', 'd'\\], dtype='{dtype}'\\)\nAt positional index 2, first diff: c != d"
df1 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df2 = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'd'])
with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2, check_like=check_like, obj=obj_fixture)
```

## Next Steps


---

*Source: test_assert_frame_equal.py:112 | Complexity: Intermediate | Last updated: 2026-06-02*