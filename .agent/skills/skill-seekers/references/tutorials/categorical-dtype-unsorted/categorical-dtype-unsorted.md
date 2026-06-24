# How To: Categorical Dtype Unsorted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical dtype unsorted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
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

### Step 2: Assign data = 'a,b,c\n1,b,3.4\n1,b,3.4\n2,a,4.5'

```python
data = 'a,b,c\n1,b,3.4\n1,b,3.4\n2,a,4.5'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': Categorical(['1', '1', '2']), 'b': Categorical(['b', 'b', 'a']), 'c': Categorical(['3.4', '3.4', '4.5'])})
```

### Step 4: Assign actual = parser.read_csv(...)

```python
actual = parser.read_csv(StringIO(data), dtype='category')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b,c\n1,b,3.4\n1,b,3.4\n2,a,4.5'
expected = DataFrame({'a': Categorical(['1', '1', '2']), 'b': Categorical(['b', 'b', 'a']), 'c': Categorical(['3.4', '3.4', '4.5'])})
actual = parser.read_csv(StringIO(data), dtype='category')
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*