# How To: Delitem Col Still Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delitem col still multiindex

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['a', 'b', 'c', 'top'], ['', '', '', 'OD'], ['', '', '', 'wx']]
```

**Verification:**
```python
assert isinstance(df.columns, MultiIndex)
```

### Step 2: Assign tuples = sorted(...)

```python
tuples = sorted(zip(*arrays))
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), columns=index)
```

**Verification:**
```python
assert isinstance(df.columns, MultiIndex)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'b', 'c', 'top'], ['', '', '', 'OD'], ['', '', '', 'wx']]
tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), columns=index)
del df['a', '', '']
assert isinstance(df.columns, MultiIndex)
```

## Next Steps


---

*Source: test_delitem.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*