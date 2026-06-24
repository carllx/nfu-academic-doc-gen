# How To: Unique Index Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique index series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: ordered
```

## Step-by-Step Guide

### Step 1: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype([3, 2, 1], ordered=ordered)
```

### Step 2: Assign c = Categorical(...)

```python
c = Categorical([3, 1, 2, 2, 1], dtype=dtype)
```

### Step 3: Assign exp = Categorical(...)

```python
exp = Categorical([3, 1, 2], dtype=dtype)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c.unique(), exp)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(Index(c).unique(), Index(exp))
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(Series(c).unique(), exp)
```

### Step 7: Assign c = Categorical(...)

```python
c = Categorical([1, 1, 2, 2], dtype=dtype)
```

### Step 8: Assign exp = Categorical(...)

```python
exp = Categorical([1, 2], dtype=dtype)
```

### Step 9: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c.unique(), exp)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(Index(c).unique(), Index(exp))
```

### Step 11: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(Series(c).unique(), exp)
```


## Complete Example

```python
# Setup
# Fixtures: ordered

# Workflow
dtype = CategoricalDtype([3, 2, 1], ordered=ordered)
c = Categorical([3, 1, 2, 2, 1], dtype=dtype)
exp = Categorical([3, 1, 2], dtype=dtype)
tm.assert_categorical_equal(c.unique(), exp)
tm.assert_index_equal(Index(c).unique(), Index(exp))
tm.assert_categorical_equal(Series(c).unique(), exp)
c = Categorical([1, 1, 2, 2], dtype=dtype)
exp = Categorical([1, 2], dtype=dtype)
tm.assert_categorical_equal(c.unique(), exp)
tm.assert_index_equal(Index(c).unique(), Index(exp))
tm.assert_categorical_equal(Series(c).unique(), exp)
```

## Next Steps


---

*Source: test_analytics.py:254 | Complexity: Advanced | Last updated: 2026-06-02*