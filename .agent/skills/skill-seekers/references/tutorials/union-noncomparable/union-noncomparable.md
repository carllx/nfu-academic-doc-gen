# How To: Union Noncomparable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union noncomparable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign index = RangeIndex(...)

```python
index = RangeIndex(start=0, stop=20, step=2)
```

### Step 2: Assign other = Index(...)

```python
other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
```

### Step 3: Assign result = index.union(...)

```python
result = index.union(other, sort=sort)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(np.concatenate((index, other)))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = other.union(...)

```python
result = other.union(index, sort=sort)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index(np.concatenate((other, index)))
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
index = RangeIndex(start=0, stop=20, step=2)
other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
result = index.union(other, sort=sort)
expected = Index(np.concatenate((index, other)))
tm.assert_index_equal(result, expected)
result = other.union(index, sort=sort)
expected = Index(np.concatenate((other, index)))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:134 | Complexity: Advanced | Last updated: 2026-06-02*