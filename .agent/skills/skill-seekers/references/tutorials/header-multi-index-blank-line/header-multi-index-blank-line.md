# How To: Header Multi Index Blank Line

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test header multi index blank line

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

### Step 2: Assign data = value

```python
data = [[None, None], [1, 2], [3, 4]]
```

### Step 3: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('a', 'A'), ('b', 'B')])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, columns=columns)
```

### Step 5: Assign data = 'a,b\nA,B\n,\n1,2\n3,4'

```python
data = 'a,b\nA,B\n,\n1,2\n3,4'
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=[0, 1])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = [[None, None], [1, 2], [3, 4]]
columns = MultiIndex.from_tuples([('a', 'A'), ('b', 'B')])
expected = DataFrame(data, columns=columns)
data = 'a,b\nA,B\n,\n1,2\n3,4'
result = parser.read_csv(StringIO(data), header=[0, 1])
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_header.py:411 | Complexity: Intermediate | Last updated: 2026-06-02*