# How To: Empty With Index Col False

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with index col false

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

### Step 1: Assign data = 'x,y'

```python
data = 'x,y'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['x', 'y'])
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
data = 'x,y'
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=False)
expected = DataFrame(columns=['x', 'y'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index_col.py:148 | Complexity: Intermediate | Last updated: 2026-06-02*