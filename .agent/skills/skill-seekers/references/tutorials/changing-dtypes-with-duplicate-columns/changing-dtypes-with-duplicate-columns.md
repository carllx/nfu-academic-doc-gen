# How To: Changing Dtypes With Duplicate Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test changing dtypes with duplicate columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=['that', 'that'])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(1.0, index=range(5), columns=['that', 'that'])
```

### Step 3: Assign unknown = 1.0

```python
df['that'] = 1.0
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((5, 2)), columns=['that', 'that'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(1, index=range(5), columns=['that', 'that'])
```

### Step 7: Assign unknown = 1

```python
df['that'] = 1
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=['that', 'that'])
expected = DataFrame(1.0, index=range(5), columns=['that', 'that'])
df['that'] = 1.0
tm.assert_frame_equal(df, expected)
df = DataFrame(np.random.default_rng(2).random((5, 2)), columns=['that', 'that'])
expected = DataFrame(1, index=range(5), columns=['that', 'that'])
df['that'] = 1
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:173 | Complexity: Advanced | Last updated: 2026-06-02*