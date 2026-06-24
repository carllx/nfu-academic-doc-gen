# How To: Append Multiple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append multiple

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(['a', 'b', 'c', 'd', 'e', 'f'])
```

### Step 2: Assign foos = value

```python
foos = [index[:2], index[2:4], index[4:]]
```

### Step 3: Assign result = unknown.append(...)

```python
result = foos[0].append(foos[1:])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```

### Step 5: Assign result = index.append(...)

```python
result = index.append([])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```


## Complete Example

```python
# Workflow
index = Index(['a', 'b', 'c', 'd', 'e', 'f'])
foos = [index[:2], index[2:4], index[4:]]
result = foos[0].append(foos[1:])
tm.assert_index_equal(result, index)
result = index.append([])
tm.assert_index_equal(result, index)
```

## Next Steps


---

*Source: test_reshape.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*