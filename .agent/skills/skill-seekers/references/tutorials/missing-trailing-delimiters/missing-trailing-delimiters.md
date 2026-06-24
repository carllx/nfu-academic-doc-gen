# How To: Missing Trailing Delimiters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test missing trailing delimiters

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C,D\n1,2,3,4\n1,3,3,\n1,4,5'

```python
data = 'A,B,C,D\n1,2,3,4\n1,3,3,\n1,4,5'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3, 4], [1, 3, 3, np.nan], [1, 4, 5, np.nan]], columns=['A', 'B', 'C', 'D'])
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
data = 'A,B,C,D\n1,2,3,4\n1,3,3,\n1,4,5'
result = parser.read_csv(StringIO(data))
expected = DataFrame([[1, 2, 3, 4], [1, 3, 3, np.nan], [1, 4, 5, np.nan]], columns=['A', 'B', 'C', 'D'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*