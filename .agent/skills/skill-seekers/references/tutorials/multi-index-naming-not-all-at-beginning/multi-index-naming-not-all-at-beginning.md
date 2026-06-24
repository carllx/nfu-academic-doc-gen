# How To: Multi Index Naming Not All At Beginning

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi index naming not all at beginning

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = ',Unnamed: 2,\na,c,1\na,d,2\nb,c,3\nb,d,4'

```python
data = ',Unnamed: 2,\na,c,1\na,d,2\nb,c,3\nb,d,4'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=[0, 2])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Unnamed: 2': ['c', 'd', 'c', 'd']}, index=MultiIndex(levels=[['a', 'b'], [1, 2, 3, 4]], codes=[[0, 0, 1, 1], [0, 1, 2, 3]]))
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
data = ',Unnamed: 2,\na,c,1\na,d,2\nb,c,3\nb,d,4'
result = parser.read_csv(StringIO(data), index_col=[0, 2])
expected = DataFrame({'Unnamed: 2': ['c', 'd', 'c', 'd']}, index=MultiIndex(levels=[['a', 'b'], [1, 2, 3, 4]], codes=[[0, 0, 1, 1], [0, 1, 2, 3]]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index_col.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*