# How To: Concat Tuple Keys

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat tuple keys

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.ones((2, 2)), columns=list('AB'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.ones((3, 2)) * 2, columns=list('AB'))
```

### Step 3: Assign results = concat(...)

```python
results = concat((df1, df2), keys=[('bee', 'bah'), ('bee', 'boo')])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': {('bee', 'bah', 0): 1.0, ('bee', 'bah', 1): 1.0, ('bee', 'boo', 0): 2.0, ('bee', 'boo', 1): 2.0, ('bee', 'boo', 2): 2.0}, 'B': {('bee', 'bah', 0): 1.0, ('bee', 'bah', 1): 1.0, ('bee', 'boo', 0): 2.0, ('bee', 'boo', 1): 2.0, ('bee', 'boo', 2): 2.0}})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(results, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(np.ones((2, 2)), columns=list('AB'))
df2 = DataFrame(np.ones((3, 2)) * 2, columns=list('AB'))
results = concat((df1, df2), keys=[('bee', 'bah'), ('bee', 'boo')])
expected = DataFrame({'A': {('bee', 'bah', 0): 1.0, ('bee', 'bah', 1): 1.0, ('bee', 'boo', 0): 2.0, ('bee', 'boo', 1): 2.0, ('bee', 'boo', 2): 2.0}, 'B': {('bee', 'bah', 0): 1.0, ('bee', 'bah', 1): 1.0, ('bee', 'boo', 0): 2.0, ('bee', 'boo', 1): 2.0, ('bee', 'boo', 2): 2.0}})
tm.assert_frame_equal(results, expected)
```

## Next Steps


---

*Source: test_dataframe.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*