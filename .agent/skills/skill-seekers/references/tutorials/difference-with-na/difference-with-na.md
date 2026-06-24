# How To: Difference With Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test difference with na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: na_value
```

## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(['a', 'b', 'c', None])
```

### Step 2: Assign other = Index(...)

```python
other = Index(['c', na_value])
```

### Step 3: Assign result = ci.difference(...)

```python
result = ci.difference(other)
```

### Step 4: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(['a', 'b'], categories=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: na_value

# Workflow
ci = CategoricalIndex(['a', 'b', 'c', None])
other = Index(['c', na_value])
result = ci.difference(other)
expected = CategoricalIndex(['a', 'b'], categories=['a', 'b', 'c'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*