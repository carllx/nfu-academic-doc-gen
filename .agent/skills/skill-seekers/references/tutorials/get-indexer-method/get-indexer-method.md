# How To: Get Indexer Method

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer method

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = CategoricalIndex(...)

```python
idx1 = CategoricalIndex(list('aabcde'), categories=list('edabc'))
```

### Step 2: Assign idx2 = CategoricalIndex(...)

```python
idx2 = CategoricalIndex(list('abf'))
```

### Step 3: Assign msg = 'method pad not yet implemented for CategoricalIndex'

```python
msg = 'method pad not yet implemented for CategoricalIndex'
```

### Step 4: Assign msg = 'method backfill not yet implemented for CategoricalIndex'

```python
msg = 'method backfill not yet implemented for CategoricalIndex'
```

### Step 5: Assign msg = 'method nearest not yet implemented for CategoricalIndex'

```python
msg = 'method nearest not yet implemented for CategoricalIndex'
```

### Step 6: Call idx2.get_indexer()

```python
idx2.get_indexer(idx1, method='pad')
```

### Step 7: Call idx2.get_indexer()

```python
idx2.get_indexer(idx1, method='backfill')
```

### Step 8: Call idx2.get_indexer()

```python
idx2.get_indexer(idx1, method='nearest')
```


## Complete Example

```python
# Workflow
idx1 = CategoricalIndex(list('aabcde'), categories=list('edabc'))
idx2 = CategoricalIndex(list('abf'))
msg = 'method pad not yet implemented for CategoricalIndex'
with pytest.raises(NotImplementedError, match=msg):
    idx2.get_indexer(idx1, method='pad')
msg = 'method backfill not yet implemented for CategoricalIndex'
with pytest.raises(NotImplementedError, match=msg):
    idx2.get_indexer(idx1, method='backfill')
msg = 'method nearest not yet implemented for CategoricalIndex'
with pytest.raises(NotImplementedError, match=msg):
    idx2.get_indexer(idx1, method='nearest')
```

## Next Steps


---

*Source: test_indexing.py:255 | Complexity: Advanced | Last updated: 2026-06-02*