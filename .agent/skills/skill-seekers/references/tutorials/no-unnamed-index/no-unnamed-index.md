# How To: No Unnamed Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no unnamed index

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = ' id c0 c1 c2\n0 1 0 a b\n1 2 0 c d\n2 2 2 e f\n'

```python
data = ' id c0 c1 c2\n0 1 0 a b\n1 2 0 c d\n2 2 2 e f\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep=' ')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0, 1, 0, 'a', 'b'], [1, 2, 0, 'c', 'd'], [2, 2, 2, 'e', 'f']], columns=['Unnamed: 0', 'id', 'c0', 'c1', 'c2'])
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
data = ' id c0 c1 c2\n0 1 0 a b\n1 2 0 c d\n2 2 2 e f\n'
result = parser.read_csv(StringIO(data), sep=' ')
expected = DataFrame([[0, 1, 0, 'a', 'b'], [1, 2, 0, 'c', 'd'], [2, 2, 2, 'e', 'f']], columns=['Unnamed: 0', 'id', 'c0', 'c1', 'c2'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*