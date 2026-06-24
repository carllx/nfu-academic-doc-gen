# How To: Constructor With Existing Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor with existing categories

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

### Step 1: Assign c0 = Categorical(...)

```python
c0 = Categorical(['a', 'b', 'c', 'a'])
```

### Step 2: Assign c1 = Categorical(...)

```python
c1 = Categorical(['a', 'b', 'c', 'a'], categories=['b', 'c'])
```

### Step 3: Assign c2 = Categorical(...)

```python
c2 = Categorical(c0, categories=c1.categories)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c2)
```

### Step 5: Assign c3 = Categorical(...)

```python
c3 = Categorical(Series(c0), categories=c1.categories)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c3)
```


## Complete Example

```python
# Workflow
c0 = Categorical(['a', 'b', 'c', 'a'])
c1 = Categorical(['a', 'b', 'c', 'a'], categories=['b', 'c'])
c2 = Categorical(c0, categories=c1.categories)
tm.assert_categorical_equal(c1, c2)
c3 = Categorical(Series(c0), categories=c1.categories)
tm.assert_categorical_equal(c1, c3)
```

## Next Steps


---

*Source: test_constructors.py:256 | Complexity: Intermediate | Last updated: 2026-06-02*