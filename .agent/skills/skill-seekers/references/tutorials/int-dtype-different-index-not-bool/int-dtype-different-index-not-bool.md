# How To: Int Dtype Different Index Not Bool

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int dtype different index not bool

## Prerequisites

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([1, 2, 3], index=[10, 11, 23], columns=['a'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([10, 20, 30], index=[11, 10, 23], columns=['a'])
```

### Step 3: Assign result = np.bitwise_xor(...)

```python
result = np.bitwise_xor(df1, df2)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([21, 8, 29], index=[10, 11, 23], columns=['a'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = df1 ^ df2
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame([1, 2, 3], index=[10, 11, 23], columns=['a'])
df2 = DataFrame([10, 20, 30], index=[11, 10, 23], columns=['a'])
result = np.bitwise_xor(df1, df2)
expected = DataFrame([21, 8, 29], index=[10, 11, 23], columns=['a'])
tm.assert_frame_equal(result, expected)
result = df1 ^ df2
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:199 | Complexity: Intermediate | Last updated: 2026-06-02*