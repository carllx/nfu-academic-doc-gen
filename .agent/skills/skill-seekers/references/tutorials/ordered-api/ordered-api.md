# How To: Ordered Api

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ordered api

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign cat1 = Categorical(...)

```python
cat1 = Categorical(list('acb'), ordered=False)
```

**Verification:**
```python
assert not cat1.ordered
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(cat1.categories, Index(['a', 'b', 'c']))
```

**Verification:**
```python
assert not cat2.ordered
```

### Step 3: Assign cat2 = Categorical(...)

```python
cat2 = Categorical(list('acb'), categories=list('bca'), ordered=False)
```

**Verification:**
```python
assert cat3.ordered
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(cat2.categories, Index(['b', 'c', 'a']))
```

**Verification:**
```python
assert cat4.ordered
```

### Step 5: Assign cat3 = Categorical(...)

```python
cat3 = Categorical(list('acb'), ordered=True)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(cat3.categories, Index(['a', 'b', 'c']))
```

**Verification:**
```python
assert cat3.ordered
```

### Step 7: Assign cat4 = Categorical(...)

```python
cat4 = Categorical(list('acb'), categories=list('bca'), ordered=True)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(cat4.categories, Index(['b', 'c', 'a']))
```

**Verification:**
```python
assert cat4.ordered
```


## Complete Example

```python
# Workflow
cat1 = Categorical(list('acb'), ordered=False)
tm.assert_index_equal(cat1.categories, Index(['a', 'b', 'c']))
assert not cat1.ordered
cat2 = Categorical(list('acb'), categories=list('bca'), ordered=False)
tm.assert_index_equal(cat2.categories, Index(['b', 'c', 'a']))
assert not cat2.ordered
cat3 = Categorical(list('acb'), ordered=True)
tm.assert_index_equal(cat3.categories, Index(['a', 'b', 'c']))
assert cat3.ordered
cat4 = Categorical(list('acb'), categories=list('bca'), ordered=True)
tm.assert_index_equal(cat4.categories, Index(['b', 'c', 'a']))
assert cat4.ordered
```

## Next Steps


---

*Source: test_api.py:28 | Complexity: Advanced | Last updated: 2026-06-02*