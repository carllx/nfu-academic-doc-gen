# How To: Header Multi Index Common Format3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test header multi index common format3

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
# Fixtures: all_parsers, kwargs
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], index=['one', 'two'], columns=MultiIndex.from_tuples([('a', 'q'), ('a', 'r'), ('a', 's'), ('b', 't'), ('c', 'u'), ('c', 'v')]))
```

### Step 3: Assign expected = expected.reset_index(...)

```python
expected = expected.reset_index(drop=True)
```

### Step 4: Assign data = 'a,a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'

```python
data = 'a,a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=None, **kwargs)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, kwargs

# Workflow
parser = all_parsers
expected = DataFrame([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], index=['one', 'two'], columns=MultiIndex.from_tuples([('a', 'q'), ('a', 'r'), ('a', 's'), ('b', 't'), ('c', 'u'), ('c', 'v')]))
expected = expected.reset_index(drop=True)
data = 'a,a,a,b,c,c\nq,r,s,t,u,v\n1,2,3,4,5,6\n7,8,9,10,11,12'
result = parser.read_csv(StringIO(data), index_col=None, **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_header.py:327 | Complexity: Intermediate | Last updated: 2026-06-02*