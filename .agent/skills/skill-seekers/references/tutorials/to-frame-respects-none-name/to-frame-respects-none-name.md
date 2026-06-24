# How To: To Frame Respects None Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to frame respects none name

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='2019-01-01', end='2019-01-30', freq='D', tz='UTC')
```

### Step 2: Assign result = idx.to_frame(...)

```python
result = idx.to_frame(name=None)
```

### Step 3: Assign exp_idx = Index(...)

```python
exp_idx = Index([None], dtype=object)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(exp_idx, result.columns)
```

### Step 5: Assign result = idx.rename.to_frame(...)

```python
result = idx.rename('foo').to_frame(name=None)
```

### Step 6: Assign exp_idx = Index(...)

```python
exp_idx = Index([None], dtype=object)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(exp_idx, result.columns)
```


## Complete Example

```python
# Workflow
idx = date_range(start='2019-01-01', end='2019-01-30', freq='D', tz='UTC')
result = idx.to_frame(name=None)
exp_idx = Index([None], dtype=object)
tm.assert_index_equal(exp_idx, result.columns)
result = idx.rename('foo').to_frame(name=None)
exp_idx = Index([None], dtype=object)
tm.assert_index_equal(exp_idx, result.columns)
```

## Next Steps


---

*Source: test_to_frame.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*