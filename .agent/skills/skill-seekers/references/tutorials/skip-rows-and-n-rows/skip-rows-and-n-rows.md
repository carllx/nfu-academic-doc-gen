# How To: Skip Rows And N Rows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test skip rows and n rows

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

### Step 1: Assign data = 'a,b\n1,a\n2,b\n3,c\n4,d\n5,e\n6,f\n7,g\n8,h\n'

```python
data = 'a,b\n1,a\n2,b\n3,c\n4,d\n5,e\n6,f\n7,g\n8,h\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), nrows=5, skiprows=[2, 4, 6])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 3, 5, 7, 8], 'b': ['a', 'c', 'e', 'g', 'h']})
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
data = 'a,b\n1,a\n2,b\n3,c\n4,d\n5,e\n6,f\n7,g\n8,h\n'
parser = all_parsers
result = parser.read_csv(StringIO(data), nrows=5, skiprows=[2, 4, 6])
expected = DataFrame({'a': [1, 3, 5, 7, 8], 'b': ['a', 'c', 'e', 'g', 'h']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skiprows.py:293 | Complexity: Intermediate | Last updated: 2026-06-02*