# How To: Csv Mixed Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test csv mixed type

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

### Step 1: Assign data = 'A,B,C\na,1,2\nb,3,4\nc,4,5\n'

```python
data = 'A,B,C\na,1,2\nb,3,4\nc,4,5\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 3, 4], 'C': [2, 4, 5]})
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
data = 'A,B,C\na,1,2\nb,3,4\nc,4,5\n'
parser = all_parsers
expected = DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 3, 4], 'C': [2, 4, 5]})
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*