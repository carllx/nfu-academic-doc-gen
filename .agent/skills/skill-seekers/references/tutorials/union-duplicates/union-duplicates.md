# How To: Union Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union duplicates

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01', periods=2)
```

### Step 2: Assign idx_dup = idx.append(...)

```python
idx_dup = idx.append(idx)
```

### Step 3: Assign idx2 = period_range(...)

```python
idx2 = period_range('2011-01-02', periods=2)
```

### Step 4: Assign idx2_dup = idx2.append(...)

```python
idx2_dup = idx2.append(idx2)
```

### Step 5: Assign result = idx_dup.union(...)

```python
result = idx_dup.union(idx2_dup)
```

### Step 6: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-02', '2011-01-03', '2011-01-03'], freq='D')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = period_range('2011-01-01', periods=2)
idx_dup = idx.append(idx)
idx2 = period_range('2011-01-02', periods=2)
idx2_dup = idx2.append(idx2)
result = idx_dup.union(idx2_dup)
expected = PeriodIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-02', '2011-01-03', '2011-01-03'], freq='D')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:343 | Complexity: Intermediate | Last updated: 2026-06-02*