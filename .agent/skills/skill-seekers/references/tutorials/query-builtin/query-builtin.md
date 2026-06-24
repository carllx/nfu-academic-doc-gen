# How To: Query Builtin

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test query builtin

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign n, m = 10

```python
n = m = 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(m, size=(n, 3)), columns=list('abc'))
```

### Step 3: Assign df.index.name = 'sin'

```python
df.index.name = 'sin'
```

### Step 4: Assign expected = value

```python
expected = df[df.index > 5]
```

### Step 5: Assign result = df.query(...)

```python
result = df.query('sin > 5', engine=engine, parser=parser)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Workflow
n = m = 10
df = DataFrame(np.random.default_rng(2).integers(m, size=(n, 3)), columns=list('abc'))
df.index.name = 'sin'
expected = df[df.index > 5]
result = df.query('sin > 5', engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_query_eval.py:942 | Complexity: Intermediate | Last updated: 2026-06-02*