# How To: Drop Not Lexsorted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop not lexsorted

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tuples = value

```python
tuples = [('a', ''), ('b1', 'c1'), ('b2', 'c2')]
```

**Verification:**
```python
assert lexsorted_mi._is_lexsorted()
```

### Step 2: Assign lexsorted_mi = MultiIndex.from_tuples(...)

```python
lexsorted_mi = MultiIndex.from_tuples(tuples, names=['b', 'c'])
```

**Verification:**
```python
assert not not_lexsorted_mi._is_lexsorted()
```

### Step 3: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(columns=['a', 'b', 'c', 'd'], data=[[1, 'b1', 'c1', 3], [1, 'b2', 'c2', 4]])
```

### Step 4: Assign df = df.pivot_table(...)

```python
df = df.pivot_table(index='a', columns=['b', 'c'], values='d')
```

### Step 5: Assign df = df.reset_index(...)

```python
df = df.reset_index()
```

### Step 6: Assign not_lexsorted_mi = value

```python
not_lexsorted_mi = df.columns
```

**Verification:**
```python
assert not not_lexsorted_mi._is_lexsorted()
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(lexsorted_mi, not_lexsorted_mi)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(lexsorted_mi.drop('a'), not_lexsorted_mi.drop('a'))
```


## Complete Example

```python
# Workflow
tuples = [('a', ''), ('b1', 'c1'), ('b2', 'c2')]
lexsorted_mi = MultiIndex.from_tuples(tuples, names=['b', 'c'])
assert lexsorted_mi._is_lexsorted()
df = pd.DataFrame(columns=['a', 'b', 'c', 'd'], data=[[1, 'b1', 'c1', 3], [1, 'b2', 'c2', 4]])
df = df.pivot_table(index='a', columns=['b', 'c'], values='d')
df = df.reset_index()
not_lexsorted_mi = df.columns
assert not not_lexsorted_mi._is_lexsorted()
tm.assert_index_equal(lexsorted_mi, not_lexsorted_mi)
with tm.assert_produces_warning(PerformanceWarning):
    tm.assert_index_equal(lexsorted_mi.drop('a'), not_lexsorted_mi.drop('a'))
```

## Next Steps


---

*Source: test_drop.py:124 | Complexity: Advanced | Last updated: 2026-06-02*