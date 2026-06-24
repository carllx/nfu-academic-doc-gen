# How To: Set Change Dtype Slice

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set change dtype slice

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign cols = MultiIndex.from_tuples(...)

```python
cols = MultiIndex.from_tuples([('1st', 'a'), ('2nd', 'b'), ('3rd', 'c')])
```

**Verification:**
```python
assert sorted(blocks.keys()) == ['float64', 'int64']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1.0, 2, 3], [4.0, 5, 6]], columns=cols)
```

### Step 3: Assign unknown = value

```python
df['2nd'] = df['2nd'] * 2.0
```

### Step 4: Assign blocks = df._to_dict_of_blocks(...)

```python
blocks = df._to_dict_of_blocks()
```

**Verification:**
```python
assert sorted(blocks.keys()) == ['float64', 'int64']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(blocks['float64'], DataFrame([[1.0, 4.0], [4.0, 10.0]], columns=cols[:2]))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(blocks['int64'], DataFrame([[3], [6]], columns=cols[2:]))
```


## Complete Example

```python
# Workflow
cols = MultiIndex.from_tuples([('1st', 'a'), ('2nd', 'b'), ('3rd', 'c')])
df = DataFrame([[1.0, 2, 3], [4.0, 5, 6]], columns=cols)
df['2nd'] = df['2nd'] * 2.0
blocks = df._to_dict_of_blocks()
assert sorted(blocks.keys()) == ['float64', 'int64']
tm.assert_frame_equal(blocks['float64'], DataFrame([[1.0, 4.0], [4.0, 10.0]], columns=cols[:2]))
tm.assert_frame_equal(blocks['int64'], DataFrame([[3], [6]], columns=cols[2:]))
```

## Next Steps


---

*Source: test_to_dict_of_blocks.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*