# How To: Union Sorted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union sorted

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
# Fixtures: idx1, idx2, expected_sorted, expected_notsorted
```

## Step-by-Step Guide

### Step 1: Assign res1 = idx1.union(...)

```python
res1 = idx1.union(idx2, sort=None)
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res1, expected_sorted, exact=True)
```

### Step 3: Assign res1 = idx1.union(...)

```python
res1 = idx1.union(idx2, sort=False)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res1, expected_notsorted, exact=True)
```

### Step 5: Assign res2 = idx2.union(...)

```python
res2 = idx2.union(idx1, sort=None)
```

### Step 6: Assign res3 = Index.union(...)

```python
res3 = Index(idx1._values, name=idx1.name).union(idx2, sort=None)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res2, expected_sorted, exact=True)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res3, expected_sorted, exact='equiv')
```


## Complete Example

```python
# Setup
# Fixtures: idx1, idx2, expected_sorted, expected_notsorted

# Workflow
res1 = idx1.union(idx2, sort=None)
tm.assert_index_equal(res1, expected_sorted, exact=True)
res1 = idx1.union(idx2, sort=False)
tm.assert_index_equal(res1, expected_notsorted, exact=True)
res2 = idx2.union(idx1, sort=None)
res3 = Index(idx1._values, name=idx1.name).union(idx2, sort=None)
tm.assert_index_equal(res2, expected_sorted, exact=True)
tm.assert_index_equal(res3, expected_sorted, exact='equiv')
```

## Next Steps


---

*Source: test_setops.py:286 | Complexity: Advanced | Last updated: 2026-06-02*