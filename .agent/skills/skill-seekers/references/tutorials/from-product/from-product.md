# How To: From Product

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from product

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign first = value

```python
first = ['foo', 'bar', 'buz']
```

### Step 2: Assign second = value

```python
second = ['a', 'b', 'c']
```

### Step 3: Assign names = value

```python
names = ['first', 'second']
```

### Step 4: Assign result = MultiIndex.from_product(...)

```python
result = MultiIndex.from_product([first, second], names=names)
```

### Step 5: Assign tuples = value

```python
tuples = [('foo', 'a'), ('foo', 'b'), ('foo', 'c'), ('bar', 'a'), ('bar', 'b'), ('bar', 'c'), ('buz', 'a'), ('buz', 'b'), ('buz', 'c')]
```

### Step 6: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples(tuples, names=names)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
first = ['foo', 'bar', 'buz']
second = ['a', 'b', 'c']
names = ['first', 'second']
result = MultiIndex.from_product([first, second], names=names)
tuples = [('foo', 'a'), ('foo', 'b'), ('foo', 'c'), ('bar', 'a'), ('bar', 'b'), ('bar', 'c'), ('buz', 'a'), ('buz', 'b'), ('buz', 'c')]
expected = MultiIndex.from_tuples(tuples, names=names)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:497 | Complexity: Intermediate | Last updated: 2026-06-02*