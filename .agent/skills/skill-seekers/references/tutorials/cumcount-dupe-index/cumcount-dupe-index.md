# How To: Cumcount Dupe Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cumcount dupe index

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['a'], ['a'], ['a'], ['b'], ['a']], columns=['A'], index=[0] * 5)
```

### Step 2: Assign g = df.groupby(...)

```python
g = df.groupby('A')
```

### Step 3: Assign sg = value

```python
sg = g.A
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0, 1, 2, 0, 3], index=[0] * 5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, g.cumcount())
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, sg.cumcount())
```


## Complete Example

```python
# Workflow
df = DataFrame([['a'], ['a'], ['a'], ['b'], ['a']], columns=['A'], index=[0] * 5)
g = df.groupby('A')
sg = g.A
expected = Series([0, 1, 2, 0, 3], index=[0] * 5)
tm.assert_series_equal(expected, g.cumcount())
tm.assert_series_equal(expected, sg.cumcount())
```

## Next Steps


---

*Source: test_counting.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*