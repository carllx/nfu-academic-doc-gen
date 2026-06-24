# How To: Reindex Non Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex non unique

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([(0, 0), (1, 1), (1, 1), (2, 2)])
```

### Step 2: Assign a = pd.Series(...)

```python
a = pd.Series(np.arange(4), index=idx)
```

### Step 3: Assign new_idx = MultiIndex.from_tuples(...)

```python
new_idx = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 2)])
```

### Step 4: Assign msg = 'cannot handle a non-unique multi-index!'

```python
msg = 'cannot handle a non-unique multi-index!'
```

### Step 5: Call a.reindex()

```python
a.reindex(new_idx)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_tuples([(0, 0), (1, 1), (1, 1), (2, 2)])
a = pd.Series(np.arange(4), index=idx)
new_idx = MultiIndex.from_tuples([(0, 0), (1, 1), (2, 2)])
msg = 'cannot handle a non-unique multi-index!'
with pytest.raises(ValueError, match=msg):
    a.reindex(new_idx)
```

## Next Steps


---

*Source: test_reindex.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*