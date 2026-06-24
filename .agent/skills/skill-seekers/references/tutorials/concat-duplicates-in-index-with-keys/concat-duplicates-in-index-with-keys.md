# How To: Concat Duplicates In Index With Keys

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat duplicates in index with keys

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = [1, 1, 3]
```

### Step 2: Assign data = value

```python
data = [1, 2, 3]
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data=data, index=index)
```

### Step 4: Assign result = concat(...)

```python
result = concat([df], keys=['A'], names=['ID', 'date'])
```

### Step 5: Assign mi = pd.MultiIndex.from_product(...)

```python
mi = pd.MultiIndex.from_product([['A'], index], names=['ID', 'date'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(data=data, index=mi)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index.levels[1], Index([1, 3], name='date'))
```


## Complete Example

```python
# Workflow
index = [1, 1, 3]
data = [1, 2, 3]
df = DataFrame(data=data, index=index)
result = concat([df], keys=['A'], names=['ID', 'date'])
mi = pd.MultiIndex.from_product([['A'], index], names=['ID', 'date'])
expected = DataFrame(data=data, index=mi)
tm.assert_frame_equal(result, expected)
tm.assert_index_equal(result.index.levels[1], Index([1, 3], name='date'))
```

## Next Steps


---

*Source: test_dataframe.py:183 | Complexity: Advanced | Last updated: 2026-06-02*