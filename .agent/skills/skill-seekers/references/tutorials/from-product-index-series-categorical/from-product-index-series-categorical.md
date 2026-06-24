# How To: From Product Index Series Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from product index series categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ordered, f
```

## Step-by-Step Guide

### Step 1: Assign first = value

```python
first = ['foo', 'bar']
```

### Step 2: Assign idx = pd.CategoricalIndex(...)

```python
idx = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=ordered)
```

### Step 3: Assign expected = pd.CategoricalIndex(...)

```python
expected = pd.CategoricalIndex(list('abcaab') + list('abcaab'), categories=list('bac'), ordered=ordered)
```

### Step 4: Assign result = MultiIndex.from_product(...)

```python
result = MultiIndex.from_product([first, f(idx)])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.get_level_values(1), expected)
```


## Complete Example

```python
# Setup
# Fixtures: ordered, f

# Workflow
first = ['foo', 'bar']
idx = pd.CategoricalIndex(list('abcaab'), categories=list('bac'), ordered=ordered)
expected = pd.CategoricalIndex(list('abcaab') + list('abcaab'), categories=list('bac'), ordered=ordered)
result = MultiIndex.from_product([first, f(idx)])
tm.assert_index_equal(result.get_level_values(1), expected)
```

## Next Steps


---

*Source: test_constructors.py:484 | Complexity: Intermediate | Last updated: 2026-06-02*