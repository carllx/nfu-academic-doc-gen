# How To: Usecols Index Col Conflict2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols index col conflict2

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

### Step 2: Assign data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'

```python
data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': ['a', 'b'], 'c': [1, 2], 'd': ('one', 'two')})
```

### Step 4: Assign expected = expected.set_index(...)

```python
expected = expected.set_index(['b', 'c'])
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=['b', 'c', 'd'], index_col=['b', 'c'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'
expected = DataFrame({'b': ['a', 'b'], 'c': [1, 2], 'd': ('one', 'two')})
expected = expected.set_index(['b', 'c'])
result = parser.read_csv(StringIO(data), usecols=['b', 'c', 'd'], index_col=['b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:192 | Complexity: Intermediate | Last updated: 2026-06-02*