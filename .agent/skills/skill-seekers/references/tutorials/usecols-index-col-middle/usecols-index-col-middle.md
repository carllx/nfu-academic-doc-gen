# How To: Usecols Index Col Middle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols index col middle

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c,d\n1,2,3,4\n'

```python
data = 'a,b,c,d\n1,2,3,4\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=['b', 'c', 'd'], index_col='c')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [2], 'd': [4]}, index=Index([3], name='c'))
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
data = 'a,b,c,d\n1,2,3,4\n'
result = parser.read_csv(StringIO(data), usecols=['b', 'c', 'd'], index_col='c')
expected = DataFrame({'b': [2], 'd': [4]}, index=Index([3], name='c'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*