# How To: Xs Integer Key

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs integer key

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

### Step 1: Assign dates = range(...)

```python
dates = range(20111201, 20111205)
```

### Step 2: Assign ids = list(...)

```python
ids = list('abcde')
```

### Step 3: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([dates, ids], names=['date', 'secid'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 3)), index, ['X', 'Y', 'Z'])
```

### Step 5: Assign result = df.xs(...)

```python
result = df.xs(20111201, level='date')
```

### Step 6: Assign expected = value

```python
expected = df.loc[20111201, :]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dates = range(20111201, 20111205)
ids = list('abcde')
index = MultiIndex.from_product([dates, ids], names=['date', 'secid'])
df = DataFrame(np.random.default_rng(2).standard_normal((len(index), 3)), index, ['X', 'Y', 'Z'])
result = df.xs(20111201, level='date')
expected = df.loc[20111201, :]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*