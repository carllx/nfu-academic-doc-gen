# How To: Categories Match Up To Permutation

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categories match up to permutation

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign c1 = Categorical(...)

```python
c1 = Categorical(list('aabca'), categories=list('abc'), ordered=False)
```

**Verification:**
```python
assert c1._categories_match_up_to_permutation(c1)
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical(list('aabca'), categories=list('cab'), ordered=False)
```

**Verification:**
```python
assert c2._categories_match_up_to_permutation(c2)
```

### Step 3: Assign c3 = Categorical(...)

```python
c3 = Categorical(list('aabca'), categories=list('cab'), ordered=True)
```

**Verification:**
```python
assert c3._categories_match_up_to_permutation(c3)
```

### Step 4: Assign s1 = Series(...)

```python
s1 = Series(c1)
```

**Verification:**
```python
assert c1._categories_match_up_to_permutation(c2)
```

### Step 5: Assign s2 = Series(...)

```python
s2 = Series(c2)
```

**Verification:**
```python
assert not c1._categories_match_up_to_permutation(c3)
```

### Step 6: Assign s3 = Series(...)

```python
s3 = Series(c3)
```

**Verification:**
```python
assert not c1._categories_match_up_to_permutation(Index(list('aabca')))
```


## Complete Example

```python
# Workflow
c1 = Categorical(list('aabca'), categories=list('abc'), ordered=False)
c2 = Categorical(list('aabca'), categories=list('cab'), ordered=False)
c3 = Categorical(list('aabca'), categories=list('cab'), ordered=True)
assert c1._categories_match_up_to_permutation(c1)
assert c2._categories_match_up_to_permutation(c2)
assert c3._categories_match_up_to_permutation(c3)
assert c1._categories_match_up_to_permutation(c2)
assert not c1._categories_match_up_to_permutation(c3)
assert not c1._categories_match_up_to_permutation(Index(list('aabca')))
assert not c1._categories_match_up_to_permutation(c1.astype(object))
assert c1._categories_match_up_to_permutation(CategoricalIndex(c1))
assert c1._categories_match_up_to_permutation(CategoricalIndex(c1, categories=list('cab')))
assert not c1._categories_match_up_to_permutation(CategoricalIndex(c1, ordered=True))
s1 = Series(c1)
s2 = Series(c2)
s3 = Series(c3)
assert c1._categories_match_up_to_permutation(s1)
assert c2._categories_match_up_to_permutation(s2)
assert c3._categories_match_up_to_permutation(s3)
assert c1._categories_match_up_to_permutation(s2)
assert not c1._categories_match_up_to_permutation(s3)
assert not c1._categories_match_up_to_permutation(s1.astype(object))
```

## Next Steps


---

*Source: test_dtypes.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*