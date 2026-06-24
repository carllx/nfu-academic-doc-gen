# How To: Concat Empty Df Object Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty df object dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_1 = DataFrame(...)

```python
df_1 = DataFrame({'Row': [0, 1, 1], 'EmptyCol': np.nan, 'NumberCol': [1, 2, 3]})
```

### Step 2: Assign df_2 = DataFrame(...)

```python
df_2 = DataFrame(columns=df_1.columns)
```

### Step 3: Assign result = concat(...)

```python
result = concat([df_1, df_2], axis=0)
```

### Step 4: Assign expected = df_1.astype(...)

```python
expected = df_1.astype(object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df_1 = DataFrame({'Row': [0, 1, 1], 'EmptyCol': np.nan, 'NumberCol': [1, 2, 3]})
df_2 = DataFrame(columns=df_1.columns)
result = concat([df_1, df_2], axis=0)
expected = df_1.astype(object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*