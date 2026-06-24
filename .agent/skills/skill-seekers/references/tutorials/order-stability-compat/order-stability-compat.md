# How To: Order Stability Compat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test order stability compat

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pidx = PeriodIndex(...)

```python
pidx = PeriodIndex(['2011', '2013', '2015', '2012', '2011'], name='pidx', freq='Y')
```

### Step 2: Assign iidx = Index(...)

```python
iidx = Index([2011, 2013, 2015, 2012, 2011], name='idx')
```

### Step 3: Assign unknown = pidx.sort_values(...)

```python
ordered1, indexer1 = pidx.sort_values(return_indexer=True, ascending=False)
```

### Step 4: Assign unknown = iidx.sort_values(...)

```python
ordered2, indexer2 = iidx.sort_values(return_indexer=True, ascending=False)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer1, indexer2)
```


## Complete Example

```python
# Workflow
pidx = PeriodIndex(['2011', '2013', '2015', '2012', '2011'], name='pidx', freq='Y')
iidx = Index([2011, 2013, 2015, 2012, 2011], name='idx')
ordered1, indexer1 = pidx.sort_values(return_indexer=True, ascending=False)
ordered2, indexer2 = iidx.sort_values(return_indexer=True, ascending=False)
tm.assert_numpy_array_equal(indexer1, indexer2)
```

## Next Steps


---

*Source: test_sort_values.py:309 | Complexity: Intermediate | Last updated: 2026-06-02*