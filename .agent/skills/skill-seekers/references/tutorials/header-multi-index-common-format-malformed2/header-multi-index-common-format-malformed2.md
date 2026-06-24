# How To: Header Multi Index Common Format Malformed2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test header multi index common format malformed2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
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

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.array([[2, 3, 4, 5, 6], [8, 9, 10, 11, 12]], dtype='int64'), index=Index([1, 7]), columns=MultiIndex(levels=[['a', 'b', 'c'], ['r', 's', 't', 'u', 'v']], codes=[[0, 0, 1, 2, 2], [0, 1, 2, 3, 4]], names=[None, 'q']))
```

### Step 3: Assign data = ',a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'

```python
data = ',a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=[0, 1], index_col=0)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
expected = DataFrame(np.array([[2, 3, 4, 5, 6], [8, 9, 10, 11, 12]], dtype='int64'), index=Index([1, 7]), columns=MultiIndex(levels=[['a', 'b', 'c'], ['r', 's', 't', 'u', 'v']], codes=[[0, 0, 1, 2, 2], [0, 1, 2, 3, 4]], names=[None, 'q']))
data = ',a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'
result = parser.read_csv(StringIO(data), header=[0, 1], index_col=0)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_header.py:368 | Complexity: Intermediate | Last updated: 2026-06-02*