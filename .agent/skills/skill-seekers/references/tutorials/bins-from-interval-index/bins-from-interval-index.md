# How To: Bins From Interval Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bins from interval index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign c = cut(...)

```python
c = cut(range(5), 3)
```

### Step 2: Assign expected = c

```python
expected = c
```

### Step 3: Assign result = cut(...)

```python
result = cut(range(5), bins=expected.categories)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 5: Assign expected = Categorical.from_codes(...)

```python
expected = Categorical.from_codes(np.append(c.codes, -1), categories=c.categories, ordered=True)
```

### Step 6: Assign result = cut(...)

```python
result = cut(range(6), bins=expected.categories)
```

### Step 7: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
c = cut(range(5), 3)
expected = c
result = cut(range(5), bins=expected.categories)
tm.assert_categorical_equal(result, expected)
expected = Categorical.from_codes(np.append(c.codes, -1), categories=c.categories, ordered=True)
result = cut(range(6), bins=expected.categories)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_cut.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*