# How To: Cut Pass Labels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cut pass labels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`

**Setup Required:**
```python
# Fixtures: get_labels, get_expected
```

## Step-by-Step Guide

### Step 1: Assign bins = value

```python
bins = [0, 25, 50, 100]
```

### Step 2: Assign arr = value

```python
arr = [50, 5, 10, 15, 20, 30, 70]
```

### Step 3: Assign labels = value

```python
labels = ['Small', 'Medium', 'Large']
```

### Step 4: Assign result = cut(...)

```python
result = cut(arr, bins, labels=get_labels(labels))
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, get_expected(labels))
```


## Complete Example

```python
# Setup
# Fixtures: get_labels, get_expected

# Workflow
bins = [0, 25, 50, 100]
arr = [50, 5, 10, 15, 20, 30, 70]
labels = ['Small', 'Medium', 'Large']
result = cut(arr, bins, labels=get_labels(labels))
tm.assert_categorical_equal(result, get_expected(labels))
```

## Next Steps


---

*Source: test_cut.py:311 | Complexity: Intermediate | Last updated: 2026-06-02*