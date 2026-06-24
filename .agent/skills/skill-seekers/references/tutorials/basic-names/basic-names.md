# How To: Basic Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
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

### Step 2: Assign data = 'a,b,a\n0,1,2\n3,4,5'

```python
data = 'a,b,a\n0,1,2\n3,4,5'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0, 1, 2], [3, 4, 5]], columns=['a', 'b', 'a.1'])
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
parser = all_parsers
data = 'a,b,a\n0,1,2\n3,4,5'
expected = DataFrame([[0, 1, 2], [3, 4, 5]], columns=['a', 'b', 'a.1'])
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_mangle_dupes.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*