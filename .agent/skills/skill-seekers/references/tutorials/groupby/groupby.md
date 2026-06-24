# How To: Groupby

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign groups = idx.groupby(...)

```python
groups = idx.groupby(np.array([1, 1, 1, 2, 2, 2]))
```

### Step 2: Assign labels = idx.tolist(...)

```python
labels = idx.tolist()
```

### Step 3: Assign exp = value

```python
exp = {1: labels[:3], 2: labels[3:]}
```

### Step 4: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(groups, exp)
```

### Step 5: Assign groups = idx.groupby(...)

```python
groups = idx.groupby(idx)
```

### Step 6: Assign exp = value

```python
exp = {key: [key] for key in idx}
```

### Step 7: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(groups, exp)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
groups = idx.groupby(np.array([1, 1, 1, 2, 2, 2]))
labels = idx.tolist()
exp = {1: labels[:3], 2: labels[3:]}
tm.assert_dict_equal(groups, exp)
groups = idx.groupby(idx)
exp = {key: [key] for key in idx}
tm.assert_dict_equal(groups, exp)
```

## Next Steps


---

*Source: test_analytics.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*