# How To: Reconstruct Remove Unused

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reconstruct remove unused

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['deleteMe', 1, 9], ['keepMe', 2, 9], ['keepMeToo', 3, 9]], columns=['first', 'second', 'third'])
```

**Verification:**
```python
assert result2.is_(result)
```

### Step 2: Assign df2 = df.set_index(...)

```python
df2 = df.set_index(['first', 'second'], drop=False)
```

### Step 3: Assign df2 = value

```python
df2 = df2[df2['first'] != 'deleteMe']
```

### Step 4: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[['deleteMe', 'keepMe', 'keepMeToo'], [1, 2, 3]], codes=[[1, 2], [1, 2]], names=['first', 'second'])
```

### Step 5: Assign result = value

```python
result = df2.index
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[['keepMe', 'keepMeToo'], [2, 3]], codes=[[0, 1], [0, 1]], names=['first', 'second'])
```

### Step 8: Assign result = df2.index.remove_unused_levels(...)

```python
result = df2.index.remove_unused_levels()
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign result2 = result.remove_unused_levels(...)

```python
result2 = result.remove_unused_levels()
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2, expected)
```

**Verification:**
```python
assert result2.is_(result)
```


## Complete Example

```python
# Workflow
df = DataFrame([['deleteMe', 1, 9], ['keepMe', 2, 9], ['keepMeToo', 3, 9]], columns=['first', 'second', 'third'])
df2 = df.set_index(['first', 'second'], drop=False)
df2 = df2[df2['first'] != 'deleteMe']
expected = MultiIndex(levels=[['deleteMe', 'keepMe', 'keepMeToo'], [1, 2, 3]], codes=[[1, 2], [1, 2]], names=['first', 'second'])
result = df2.index
tm.assert_index_equal(result, expected)
expected = MultiIndex(levels=[['keepMe', 'keepMeToo'], [2, 3]], codes=[[0, 1], [0, 1]], names=['first', 'second'])
result = df2.index.remove_unused_levels()
tm.assert_index_equal(result, expected)
result2 = result.remove_unused_levels()
tm.assert_index_equal(result2, expected)
assert result2.is_(result)
```

## Next Steps


---

*Source: test_sorting.py:203 | Complexity: Advanced | Last updated: 2026-06-02*