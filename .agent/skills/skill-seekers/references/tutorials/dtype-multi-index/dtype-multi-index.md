# How To: Dtype Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dtype multi index

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,B\nX,Y,Z\n1,2,3'

```python
data = 'A,B,B\nX,Y,Z\n1,2,3'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=list(range(2)), dtype={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({('A', 'X'): np.int32([1]), ('B', 'Y'): np.int32([2]), ('B', 'Z'): np.float32([3])})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'A,B,B\nX,Y,Z\n1,2,3'
result = parser.read_csv(StringIO(data), header=list(range(2)), dtype={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
expected = DataFrame({('A', 'X'): np.int32([1]), ('B', 'Y'): np.int32([2]), ('B', 'Z'): np.float32([3])})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:329 | Complexity: Intermediate | Last updated: 2026-06-02*