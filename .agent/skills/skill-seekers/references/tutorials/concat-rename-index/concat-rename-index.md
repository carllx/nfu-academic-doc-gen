# How To: Concat Rename Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat rename index

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame(np.random.default_rng(2).random((3, 3)), columns=list('ABC'), index=Index(list('abc'), name='index_a'))
```

**Verification:**
```python
assert result.index.names == exp.index.names
```

### Step 2: Assign b = DataFrame(...)

```python
b = DataFrame(np.random.default_rng(2).random((3, 3)), columns=list('ABC'), index=Index(list('abc'), name='index_b'))
```

### Step 3: Assign result = concat(...)

```python
result = concat([a, b], keys=['key0', 'key1'], names=['lvl0', 'lvl1'])
```

### Step 4: Assign exp = concat(...)

```python
exp = concat([a, b], keys=['key0', 'key1'], names=['lvl0'])
```

### Step 5: Assign names = list(...)

```python
names = list(exp.index.names)
```

### Step 6: Assign unknown = 'lvl1'

```python
names[1] = 'lvl1'
```

### Step 7: Call exp.index.set_names()

```python
exp.index.set_names(names, inplace=True)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

**Verification:**
```python
assert result.index.names == exp.index.names
```


## Complete Example

```python
# Workflow
a = DataFrame(np.random.default_rng(2).random((3, 3)), columns=list('ABC'), index=Index(list('abc'), name='index_a'))
b = DataFrame(np.random.default_rng(2).random((3, 3)), columns=list('ABC'), index=Index(list('abc'), name='index_b'))
result = concat([a, b], keys=['key0', 'key1'], names=['lvl0', 'lvl1'])
exp = concat([a, b], keys=['key0', 'key1'], names=['lvl0'])
names = list(exp.index.names)
names[1] = 'lvl1'
exp.index.set_names(names, inplace=True)
tm.assert_frame_equal(result, exp)
assert result.index.names == exp.index.names
```

## Next Steps


---

*Source: test_index.py:81 | Complexity: Advanced | Last updated: 2026-06-02*