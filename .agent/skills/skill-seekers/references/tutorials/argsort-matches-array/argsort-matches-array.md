# How To: Argsort Matches Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test argsort matches array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: simple_index
```

## Step-by-Step Guide

### Step 1: Assign idx = simple_index

```python
idx = simple_index
```

### Step 2: Assign idx = idx.insert(...)

```python
idx = idx.insert(1, pd.NaT)
```

### Step 3: Assign result = idx.argsort(...)

```python
result = idx.argsort()
```

### Step 4: Assign expected = idx._data.argsort(...)

```python
expected = idx._data.argsort()
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: simple_index

# Workflow
idx = simple_index
idx = idx.insert(1, pd.NaT)
result = idx.argsort()
expected = idx._data.argsort()
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimelike.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*