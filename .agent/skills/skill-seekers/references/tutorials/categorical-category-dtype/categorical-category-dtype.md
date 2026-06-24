# How To: Categorical Category Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical category dtype

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
# Fixtures: all_parsers, categories, ordered
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b\n1,a\n1,b\n1,b\n2,c'

```python
data = 'a,b\n1,a\n1,b\n1,b\n2,c'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 1, 1, 2], 'b': Categorical(['a', 'b', 'b', 'c'], categories=categories, ordered=ordered)})
```

### Step 4: Assign dtype = value

```python
dtype = {'b': CategoricalDtype(categories=categories, ordered=ordered)}
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype=dtype)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, categories, ordered

# Workflow
parser = all_parsers
data = 'a,b\n1,a\n1,b\n1,b\n2,c'
expected = DataFrame({'a': [1, 1, 1, 2], 'b': Categorical(['a', 'b', 'b', 'c'], categories=categories, ordered=ordered)})
dtype = {'b': CategoricalDtype(categories=categories, ordered=ordered)}
result = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*