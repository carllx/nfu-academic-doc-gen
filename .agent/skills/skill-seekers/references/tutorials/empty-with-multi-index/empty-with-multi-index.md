# How To: Empty With Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with multi index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `os`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'x,y,z'

```python
data = 'x,y,z'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=['x', 'y'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['z'], index=MultiIndex.from_arrays([[]] * 2, names=['x', 'y']))
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
data = 'x,y,z'
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=['x', 'y'])
expected = DataFrame(columns=['z'], index=MultiIndex.from_arrays([[]] * 2, names=['x', 'y']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*