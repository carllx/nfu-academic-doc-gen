# How To: Insert2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert2

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = value

```python
idx = [('test1', i) for i in range(5)] + [('test2', i) for i in range(6)] + [('test', 17), ('test', 18)]
```

### Step 2: Assign left = pd.Series(...)

```python
left = pd.Series(np.linspace(0, 10, 11), MultiIndex.from_tuples(idx[:-2]))
```

### Step 3: Assign unknown = 11

```python
left.loc['test', 17] = 11
```

### Step 4: Assign unknown = 12

```python
left.loc['test', 18] = 12
```

### Step 5: Assign right = pd.Series(...)

```python
right = pd.Series(np.linspace(0, 12, 13), MultiIndex.from_tuples(idx))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(left, right)
```


## Complete Example

```python
# Workflow
idx = [('test1', i) for i in range(5)] + [('test2', i) for i in range(6)] + [('test', 17), ('test', 18)]
left = pd.Series(np.linspace(0, 10, 11), MultiIndex.from_tuples(idx[:-2]))
left.loc['test', 17] = 11
left.loc['test', 18] = 12
right = pd.Series(np.linspace(0, 12, 13), MultiIndex.from_tuples(idx))
tm.assert_series_equal(left, right)
```

## Next Steps


---

*Source: test_reshape.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*