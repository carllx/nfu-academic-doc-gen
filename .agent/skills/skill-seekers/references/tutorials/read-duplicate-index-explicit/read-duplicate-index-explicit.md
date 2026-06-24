# How To: Read Duplicate Index Explicit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read duplicate index explicit

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

### Step 1: Assign data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo,12,13,14,15\nbar,12,13,14,15\n'

```python
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo,12,13,14,15\nbar,12,13,14,15\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=0)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, 3, 4, 5], [7, 8, 9, 10], [12, 13, 14, 15], [12, 13, 14, 15], [12, 13, 14, 15], [12, 13, 14, 15]], columns=['A', 'B', 'C', 'D'], index=Index(['foo', 'bar', 'baz', 'qux', 'foo', 'bar'], name='index'))
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
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo,12,13,14,15\nbar,12,13,14,15\n'
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=0)
expected = DataFrame([[2, 3, 4, 5], [7, 8, 9, 10], [12, 13, 14, 15], [12, 13, 14, 15], [12, 13, 14, 15], [12, 13, 14, 15]], columns=['A', 'B', 'C', 'D'], index=Index(['foo', 'bar', 'baz', 'qux', 'foo', 'bar'], name='index'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:186 | Complexity: Intermediate | Last updated: 2026-06-02*