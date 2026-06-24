# How To: Unnamed Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unnamed columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A,B,C,,\n1,2,3,4,5\n6,7,8,9,10\n11,12,13,14,15\n'

```python
data = 'A,B,C,,\n1,2,3,4,5\n6,7,8,9,10\n11,12,13,14,15\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], dtype=np.int64, columns=['A', 'B', 'C', 'Unnamed: 3', 'Unnamed: 4'])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
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
data = 'A,B,C,,\n1,2,3,4,5\n6,7,8,9,10\n11,12,13,14,15\n'
parser = all_parsers
expected = DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], dtype=np.int64, columns=['A', 'B', 'C', 'Unnamed: 3', 'Unnamed: 4'])
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*