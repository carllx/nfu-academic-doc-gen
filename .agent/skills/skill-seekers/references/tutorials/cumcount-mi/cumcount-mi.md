# How To: Cumcount Mi

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cumcount mi

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([[0, 1], [1, 2], [2, 2], [2, 2], [1, 0]])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([['a'], ['a'], ['a'], ['b'], ['a']], columns=['A'], index=mi)
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby('A')
```

### Step 4: Assign sg = value

```python
sg = g.A
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0, 1, 2, 0, 3], index=mi)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, g.cumcount())
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, sg.cumcount())
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([[0, 1], [1, 2], [2, 2], [2, 2], [1, 0]])
df = DataFrame([['a'], ['a'], ['a'], ['b'], ['a']], columns=['A'], index=mi)
g = df.groupby('A')
sg = g.A
expected = Series([0, 1, 2, 0, 3], index=mi)
tm.assert_series_equal(expected, g.cumcount())
tm.assert_series_equal(expected, sg.cumcount())
```

## Next Steps


---

*Source: test_counting.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*