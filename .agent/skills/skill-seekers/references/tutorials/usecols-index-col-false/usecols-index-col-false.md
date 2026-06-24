# How To: Usecols Index Col False

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols index col false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, data
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign usecols = value

```python
usecols = ['a', 'c', 'd']
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 5], 'c': [3, 7], 'd': [4, 8]})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols, index_col=False)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, data

# Workflow
parser = all_parsers
usecols = ['a', 'c', 'd']
expected = DataFrame({'a': [1, 5], 'c': [3, 7], 'd': [4, 8]})
result = parser.read_csv(StringIO(data), usecols=usecols, index_col=False)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*