# How To: Xs Keep Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs keep level

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'day': {0: 'sat', 1: 'sun'}, 'flavour': {0: 'strawberry', 1: 'strawberry'}, 'sales': {0: 10, 1: 12}, 'year': {0: 2008, 1: 2008}}).set_index(['year', 'flavour', 'day'])
```

### Step 2: Assign result = df.xs(...)

```python
result = df.xs('sat', level='day', drop_level=False)
```

### Step 3: Assign expected = value

```python
expected = df[:1]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.xs(...)

```python
result = df.xs((2008, 'sat'), level=['year', 'day'], drop_level=False)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'day': {0: 'sat', 1: 'sun'}, 'flavour': {0: 'strawberry', 1: 'strawberry'}, 'sales': {0: 10, 1: 12}, 'year': {0: 2008, 1: 2008}}).set_index(['year', 'flavour', 'day'])
result = df.xs('sat', level='day', drop_level=False)
expected = df[:1]
tm.assert_frame_equal(result, expected)
result = df.xs((2008, 'sat'), level=['year', 'day'], drop_level=False)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*