# How To: Dtype Mangle Dup Cols Single Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dtype mangle dup cols single dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,a\n1,1'

```python
data = 'a,a\n1,1'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype=str)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['1'], 'a.1': ['1']})
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
data = 'a,a\n1,1'
result = parser.read_csv(StringIO(data), dtype=str)
expected = DataFrame({'a': ['1'], 'a.1': ['1']})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:319 | Complexity: Intermediate | Last updated: 2026-06-02*