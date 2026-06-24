# How To: Typical Usecase

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test typical usecase

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([{'var1': 'a,b,c', 'var2': 1}, {'var1': 'd,e,f', 'var2': 2}], columns=['var1', 'var2'])
```

### Step 2: Assign exploded = df.var1.str.split.explode(...)

```python
exploded = df.var1.str.split(',').explode()
```

### Step 3: Assign result = unknown.join(...)

```python
result = df[['var2']].join(exploded)
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'var2': [1, 1, 1, 2, 2, 2], 'var1': list('abcdef')}, columns=['var2', 'var1'], index=[0, 0, 0, 1, 1, 1])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame([{'var1': 'a,b,c', 'var2': 1}, {'var1': 'd,e,f', 'var2': 2}], columns=['var1', 'var2'])
exploded = df.var1.str.split(',').explode()
result = df[['var2']].join(exploded)
expected = pd.DataFrame({'var2': [1, 1, 1, 2, 2, 2], 'var1': list('abcdef')}, columns=['var2', 'var1'], index=[0, 0, 0, 1, 1, 1])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_explode.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*