# How To: Duplicate Groupby Issues

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicate groupby issues

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx_tp = value

```python
idx_tp = [('600809', '20061231'), ('600809', '20070331'), ('600809', '20070630'), ('600809', '20070331')]
```

**Verification:**
```python
assert len(result) == 3
```

### Step 2: Assign dt = value

```python
dt = ['demo', 'demo', 'demo', 'demo']
```

### Step 3: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples(idx_tp, names=['STK_ID', 'RPT_Date'])
```

### Step 4: Assign s = Series(...)

```python
s = Series(dt, index=idx)
```

### Step 5: Assign result = s.groupby.first(...)

```python
result = s.groupby(s.index).first()
```

**Verification:**
```python
assert len(result) == 3
```


## Complete Example

```python
# Workflow
idx_tp = [('600809', '20061231'), ('600809', '20070331'), ('600809', '20070630'), ('600809', '20070331')]
dt = ['demo', 'demo', 'demo', 'demo']
idx = MultiIndex.from_tuples(idx_tp, names=['STK_ID', 'RPT_Date'])
s = Series(dt, index=idx)
result = s.groupby(s.index).first()
assert len(result) == 3
```

## Next Steps


---

*Source: test_multilevel.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*