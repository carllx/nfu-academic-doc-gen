# How To: Roundtrip With Prefixes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roundtrip with prefixes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign categories = DataFrame(...)

```python
categories = DataFrame({'col1': ['a', 'b', 'a'], 'col2': ['b', 'a', 'c']})
```

### Step 2: Assign dummies = get_dummies(...)

```python
dummies = get_dummies(categories)
```

### Step 3: Assign result = from_dummies(...)

```python
result = from_dummies(dummies, sep='_')
```

### Step 4: Assign expected = categories

```python
expected = categories
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
categories = DataFrame({'col1': ['a', 'b', 'a'], 'col2': ['b', 'a', 'c']})
dummies = get_dummies(categories)
result = from_dummies(dummies, sep='_')
expected = categories
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_from_dummies.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*