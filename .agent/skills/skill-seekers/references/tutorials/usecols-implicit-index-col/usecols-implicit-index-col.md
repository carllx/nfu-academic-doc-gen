# How To: Usecols Implicit Index Col

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols implicit index col

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

### Step 2: Assign data = 'a,b,c\n4,apple,bat,5.7\n8,orange,cow,10'

```python
data = 'a,b,c\n4,apple,bat,5.7\n8,orange,cow,10'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=['a', 'b'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['apple', 'orange'], 'b': ['bat', 'cow']}, index=[4, 8])
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
data = 'a,b,c\n4,apple,bat,5.7\n8,orange,cow,10'
result = parser.read_csv(StringIO(data), usecols=['a', 'b'])
expected = DataFrame({'a': ['apple', 'orange'], 'b': ['bat', 'cow']}, index=[4, 8])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*