# How To: Join Multiindex Not Alphabetical Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join multiindex not alphabetical categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: categories, values
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame.set_index(...)

```python
left = DataFrame({'first': ['A', 'A'], 'second': Categorical(categories, categories=categories), 'value': [1, 2]}).set_index(['first', 'second'])
```

### Step 2: Assign right = DataFrame.set_index(...)

```python
right = DataFrame({'first': ['A', 'A', 'B'], 'second': Categorical(values, categories=categories), 'value': [3, 4, 5]}).set_index(['first', 'second'])
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, lsuffix='_left', rsuffix='_right')
```

### Step 4: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'first': ['A', 'A'], 'second': Categorical(categories, categories=categories), 'value_left': [1, 2], 'value_right': [3, 4]}).set_index(['first', 'second'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: categories, values

# Workflow
left = DataFrame({'first': ['A', 'A'], 'second': Categorical(categories, categories=categories), 'value': [1, 2]}).set_index(['first', 'second'])
right = DataFrame({'first': ['A', 'A', 'B'], 'second': Categorical(values, categories=categories), 'value': [3, 4, 5]}).set_index(['first', 'second'])
result = left.join(right, lsuffix='_left', rsuffix='_right')
expected = DataFrame({'first': ['A', 'A'], 'second': Categorical(categories, categories=categories), 'value_left': [1, 2], 'value_right': [3, 4]}).set_index(['first', 'second'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:980 | Complexity: Intermediate | Last updated: 2026-06-02*