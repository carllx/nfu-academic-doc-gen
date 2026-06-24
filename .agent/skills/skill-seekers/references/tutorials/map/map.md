# How To: Map

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign c = Categorical(...)

```python
c = Categorical(list('ABABC'), categories=list('CBA'), ordered=True)
```

### Step 2: Assign result = c.map(...)

```python
result = c.map(lambda x: x.lower(), na_action=None)
```

### Step 3: Assign exp = Categorical(...)

```python
exp = Categorical(list('ababc'), categories=list('cba'), ordered=True)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, exp)
```

### Step 5: Assign c = Categorical(...)

```python
c = Categorical(list('ABABC'), categories=list('ABC'), ordered=False)
```

### Step 6: Assign result = c.map(...)

```python
result = c.map(lambda x: x.lower(), na_action=None)
```

### Step 7: Assign exp = Categorical(...)

```python
exp = Categorical(list('ababc'), categories=list('abc'), ordered=False)
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, exp)
```

### Step 9: Assign result = c.map(...)

```python
result = c.map(lambda x: 1, na_action=None)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, Index(np.array([1] * 5, dtype=np.int64)))
```


## Complete Example

```python
# Workflow
c = Categorical(list('ABABC'), categories=list('CBA'), ordered=True)
result = c.map(lambda x: x.lower(), na_action=None)
exp = Categorical(list('ababc'), categories=list('cba'), ordered=True)
tm.assert_categorical_equal(result, exp)
c = Categorical(list('ABABC'), categories=list('ABC'), ordered=False)
result = c.map(lambda x: x.lower(), na_action=None)
exp = Categorical(list('ababc'), categories=list('abc'), ordered=False)
tm.assert_categorical_equal(result, exp)
result = c.map(lambda x: 1, na_action=None)
tm.assert_index_equal(result, Index(np.array([1] * 5, dtype=np.int64)))
```

## Next Steps


---

*Source: test_analytics.py:321 | Complexity: Advanced | Last updated: 2026-06-02*