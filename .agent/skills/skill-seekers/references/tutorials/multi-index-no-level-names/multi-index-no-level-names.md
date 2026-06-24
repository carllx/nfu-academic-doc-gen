# How To: Multi Index No Level Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multi index no level names

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
# Fixtures: request, all_parsers, index_col, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign data = 'index1,index2,A,B,C,D\nfoo,one,2,3,4,5\nfoo,two,7,8,9,10\nfoo,three,12,13,14,15\nbar,one,12,13,14,15\nbar,two,12,13,14,15\n'

```python
data = 'index1,index2,A,B,C,D\nfoo,one,2,3,4,5\nfoo,two,7,8,9,10\nfoo,three,12,13,14,15\nbar,one,12,13,14,15\nbar,two,12,13,14,15\n'
```

### Step 2: Assign headless_data = unknown.join(...)

```python
headless_data = '\n'.join(data.split('\n')[1:])
```

### Step 3: Assign names = value

```python
names = ['A', 'B', 'C', 'D']
```

### Step 4: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(headless_data), index_col=index_col, header=None, names=names)
```

### Step 6: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data), index_col=index_col)
```

### Step 7: Assign expected.index.names = value

```python
expected.index.names = [None] * 2
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: request, all_parsers, index_col, using_infer_string

# Workflow
data = 'index1,index2,A,B,C,D\nfoo,one,2,3,4,5\nfoo,two,7,8,9,10\nfoo,three,12,13,14,15\nbar,one,12,13,14,15\nbar,two,12,13,14,15\n'
headless_data = '\n'.join(data.split('\n')[1:])
names = ['A', 'B', 'C', 'D']
parser = all_parsers
result = parser.read_csv(StringIO(headless_data), index_col=index_col, header=None, names=names)
expected = parser.read_csv(StringIO(data), index_col=index_col)
expected.index.names = [None] * 2
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:89 | Complexity: Advanced | Last updated: 2026-06-02*