# How To: Multilevel Consolidate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multilevel consolidate

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'two')])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index, columns=index)
```

### Step 3: Assign unknown = df.sum(...)

```python
df['Totals', ''] = df.sum(1)
```

### Step 4: Assign df = df._consolidate(...)

```python
df = df._consolidate()
```


## Complete Example

```python
# Workflow
index = MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('bar', 'one'), ('bar', 'two')])
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index, columns=index)
df['Totals', ''] = df.sum(1)
df = df._consolidate()
```

## Next Steps


---

*Source: test_multilevel.py:168 | Complexity: Intermediate | Last updated: 2026-06-02*