# How To: Split With Name Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test split with name index

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas.tests.strings`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(['a,b', 'c,d'], name='xxx')
```

**Verification:**
```python
assert res.nlevels == 1
```

### Step 2: Assign res = idx.str.split(...)

```python
res = idx.str.split(',')
```

**Verification:**
```python
assert res.nlevels == 2
```

### Step 3: Assign exp = Index(...)

```python
exp = Index([['a', 'b'], ['c', 'd']], name='xxx')
```

**Verification:**
```python
assert res.nlevels == 1
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 5: Assign res = idx.str.split(...)

```python
res = idx.str.split(',', expand=True)
```

### Step 6: Assign exp = MultiIndex.from_tuples(...)

```python
exp = MultiIndex.from_tuples([('a', 'b'), ('c', 'd')])
```

**Verification:**
```python
assert res.nlevels == 2
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```


## Complete Example

```python
# Workflow
idx = Index(['a,b', 'c,d'], name='xxx')
res = idx.str.split(',')
exp = Index([['a', 'b'], ['c', 'd']], name='xxx')
assert res.nlevels == 1
tm.assert_index_equal(res, exp)
res = idx.str.split(',', expand=True)
exp = MultiIndex.from_tuples([('a', 'b'), ('c', 'd')])
assert res.nlevels == 2
tm.assert_index_equal(res, exp)
```

## Next Steps


---

*Source: test_split_partition.py:407 | Complexity: Intermediate | Last updated: 2026-06-02*