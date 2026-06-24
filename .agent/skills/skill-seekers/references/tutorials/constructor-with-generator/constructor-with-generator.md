# How To: Constructor With Generator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor with generator

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign exp = Categorical(...)

```python
exp = Categorical([0, 1, 2])
```

### Step 2: Assign cat = Categorical(...)

```python
cat = Categorical((x for x in [0, 1, 2]))
```

### Step 3: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, exp)
```

### Step 4: Assign cat = Categorical(...)

```python
cat = Categorical(range(3))
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, exp)
```

### Step 6: Call MultiIndex.from_product()

```python
MultiIndex.from_product([range(5), ['a', 'b', 'c']])
```

### Step 7: Assign cat = Categorical(...)

```python
cat = Categorical([0, 1, 2], categories=(x for x in [0, 1, 2]))
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, exp)
```

### Step 9: Assign cat = Categorical(...)

```python
cat = Categorical([0, 1, 2], categories=range(3))
```

### Step 10: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, exp)
```


## Complete Example

```python
# Workflow
exp = Categorical([0, 1, 2])
cat = Categorical((x for x in [0, 1, 2]))
tm.assert_categorical_equal(cat, exp)
cat = Categorical(range(3))
tm.assert_categorical_equal(cat, exp)
MultiIndex.from_product([range(5), ['a', 'b', 'c']])
cat = Categorical([0, 1, 2], categories=(x for x in [0, 1, 2]))
tm.assert_categorical_equal(cat, exp)
cat = Categorical([0, 1, 2], categories=range(3))
tm.assert_categorical_equal(cat, exp)
```

## Next Steps


---

*Source: test_constructors.py:298 | Complexity: Advanced | Last updated: 2026-06-02*