# How To: Int Conversion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A,B\n1.0,1\n2.0,2\n3.0,3\n'

```python
data = 'A,B\n1.0,1\n2.0,2\n3.0,3\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 1], [2.0, 2], [3.0, 3]], columns=['A', 'B'])
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
data = 'A,B\n1.0,1\n2.0,2\n3.0,3\n'
parser = all_parsers
result = parser.read_csv(StringIO(data))
expected = DataFrame([[1.0, 1], [2.0, 2], [3.0, 3]], columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ints.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*