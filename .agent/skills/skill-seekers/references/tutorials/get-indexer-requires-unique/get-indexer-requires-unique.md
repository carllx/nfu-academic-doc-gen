# How To: Get Indexer Requires Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer requires unique

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
```

### Step 2: Assign oidx = Index(...)

```python
oidx = Index(np.array(ci))
```

### Step 3: Assign msg = 'Reindexing only valid with uniquely valued Index objects'

```python
msg = 'Reindexing only valid with uniquely valued Index objects'
```

### Step 4: Assign finder = value

```python
finder = oidx[np.random.default_rng(2).integers(0, len(ci), size=n)]
```

### Step 5: Call ci.get_indexer()

```python
ci.get_indexer(finder)
```

### Step 6: Call ci.get_indexer()

```python
ci.get_indexer(finder)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
oidx = Index(np.array(ci))
msg = 'Reindexing only valid with uniquely valued Index objects'
for n in [1, 2, 5, len(ci)]:
    finder = oidx[np.random.default_rng(2).integers(0, len(ci), size=n)]
    with pytest.raises(InvalidIndexError, match=msg):
        ci.get_indexer(finder)
for finder in [list('aabbca'), list('aababca')]:
    with pytest.raises(InvalidIndexError, match=msg):
        ci.get_indexer(finder)
```

## Next Steps


---

*Source: test_indexing.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*