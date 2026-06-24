# How To: Skip Rows Callable Not In

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip rows callable not in

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '0,a\n1,b\n2,c\n3,d\n4,e'

```python
data = '0,a\n1,b\n2,c\n3,d\n4,e'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 'b'], [3, 'd']])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, skiprows=lambda x: x not in [1, 3])
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
data = '0,a\n1,b\n2,c\n3,d\n4,e'
expected = DataFrame([[1, 'b'], [3, 'd']])
result = parser.read_csv(StringIO(data), header=None, skiprows=lambda x: x not in [1, 3])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skiprows.py:261 | Complexity: Intermediate | Last updated: 2026-06-02*