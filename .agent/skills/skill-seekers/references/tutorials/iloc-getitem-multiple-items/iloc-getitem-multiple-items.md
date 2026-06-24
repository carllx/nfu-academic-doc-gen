# How To: Iloc Getitem Multiple Items

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem multiple items

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tup = zip(...)

```python
tup = zip(*[['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])
```

### Step 2: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tup)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index)
```

### Step 4: Assign result = value

```python
result = df.iloc[[2, 3]]
```

### Step 5: Assign expected = df.xs(...)

```python
expected = df.xs('b', drop_level=False)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
tup = zip(*[['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])
index = MultiIndex.from_tuples(tup)
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=index)
result = df.iloc[[2, 3]]
expected = df.xs('b', drop_level=False)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*