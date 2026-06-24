# How To: Empty With Mangled Column Pass Dtype By Indexes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty with mangled column pass dtype by indexes

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

### Step 2: Assign data = 'one,one'

```python
data = 'one,one'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype={0: 'u1', 1: 'f'})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'one': np.empty(0, dtype='u1'), 'one.1': np.empty(0, dtype='f')})
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
data = 'one,one'
result = parser.read_csv(StringIO(data), dtype={0: 'u1', 1: 'f'})
expected = DataFrame({'one': np.empty(0, dtype='u1'), 'one.1': np.empty(0, dtype='f')})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*