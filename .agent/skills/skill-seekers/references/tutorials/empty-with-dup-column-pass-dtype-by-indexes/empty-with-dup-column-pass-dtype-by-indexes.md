# How To: Empty With Dup Column Pass Dtype By Indexes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with dup column pass dtype by indexes

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

### Step 2: Assign expected = concat(...)

```python
expected = concat([Series([], name='one', dtype='u1'), Series([], name='one.1', dtype='f')], axis=1)
```

### Step 3: Assign data = 'one,one'

```python
data = 'one,one'
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype={0: 'u1', 1: 'f'})
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
expected = concat([Series([], name='one', dtype='u1'), Series([], name='one.1', dtype='f')], axis=1)
data = 'one,one'
result = parser.read_csv(StringIO(data), dtype={0: 'u1', 1: 'f'})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*