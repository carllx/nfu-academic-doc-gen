# How To: Get Loc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cidx1 = CategoricalIndex(...)

```python
cidx1 = CategoricalIndex(list('abcde'), categories=list('edabc'))
```

**Verification:**
```python
assert cidx1.get_loc('a') == idx1.get_loc('a')
```

### Step 2: Assign idx1 = Index(...)

```python
idx1 = Index(list('abcde'))
```

**Verification:**
```python
assert cidx1.get_loc('e') == idx1.get_loc('e')
```

### Step 3: Assign cidx2 = CategoricalIndex(...)

```python
cidx2 = CategoricalIndex(list('aacded'), categories=list('edabc'))
```

**Verification:**
```python
assert res == idx2.get_loc('e')
```

### Step 4: Assign idx2 = Index(...)

```python
idx2 = Index(list('aacded'))
```

**Verification:**
```python
assert res == 4
```

### Step 5: Assign res = cidx2.get_loc(...)

```python
res = cidx2.get_loc('d')
```

**Verification:**
```python
assert res == idx3.get_loc('a')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, idx2.get_loc('d'))
```

**Verification:**
```python
assert res == slice(0, 2, None)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, np.array([False, False, False, True, False, True]))
```

**Verification:**
```python
assert res == idx3.get_loc('b')
```

### Step 8: Assign res = cidx2.get_loc(...)

```python
res = cidx2.get_loc('e')
```

**Verification:**
```python
assert res == slice(2, 5, None)
```

### Step 9: Assign cidx3 = CategoricalIndex(...)

```python
cidx3 = CategoricalIndex(list('aabbb'), categories=list('abc'))
```

### Step 10: Assign idx3 = Index(...)

```python
idx3 = Index(list('aabbb'))
```

### Step 11: Assign res = cidx3.get_loc(...)

```python
res = cidx3.get_loc('a')
```

**Verification:**
```python
assert res == idx3.get_loc('a')
```

### Step 12: Assign res = cidx3.get_loc(...)

```python
res = cidx3.get_loc('b')
```

**Verification:**
```python
assert res == idx3.get_loc('b')
```

### Step 13: Call i.get_loc()

```python
i.get_loc('NOT-EXIST')
```

### Step 14: Call i.get_loc()

```python
i.get_loc('NOT-EXIST')
```

### Step 15: Call i.get_loc()

```python
i.get_loc('c')
```


## Complete Example

```python
# Workflow
cidx1 = CategoricalIndex(list('abcde'), categories=list('edabc'))
idx1 = Index(list('abcde'))
assert cidx1.get_loc('a') == idx1.get_loc('a')
assert cidx1.get_loc('e') == idx1.get_loc('e')
for i in [cidx1, idx1]:
    with pytest.raises(KeyError, match="'NOT-EXIST'"):
        i.get_loc('NOT-EXIST')
cidx2 = CategoricalIndex(list('aacded'), categories=list('edabc'))
idx2 = Index(list('aacded'))
res = cidx2.get_loc('d')
tm.assert_numpy_array_equal(res, idx2.get_loc('d'))
tm.assert_numpy_array_equal(res, np.array([False, False, False, True, False, True]))
res = cidx2.get_loc('e')
assert res == idx2.get_loc('e')
assert res == 4
for i in [cidx2, idx2]:
    with pytest.raises(KeyError, match="'NOT-EXIST'"):
        i.get_loc('NOT-EXIST')
cidx3 = CategoricalIndex(list('aabbb'), categories=list('abc'))
idx3 = Index(list('aabbb'))
res = cidx3.get_loc('a')
assert res == idx3.get_loc('a')
assert res == slice(0, 2, None)
res = cidx3.get_loc('b')
assert res == idx3.get_loc('b')
assert res == slice(2, 5, None)
for i in [cidx3, idx3]:
    with pytest.raises(KeyError, match="'c'"):
        i.get_loc('c')
```

## Next Steps


---

*Source: test_indexing.py:136 | Complexity: Advanced | Last updated: 2026-06-02*