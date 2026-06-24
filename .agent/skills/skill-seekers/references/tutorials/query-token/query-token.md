# How To: Query Token

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test query token

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `functools`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._optional`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.core.computation.engines`
- `pandas.core.computation.expr`
- `pandas.core.computation.expressions`
- `pandas.core.computation.ops`
- `pandas.core.computation.scope`
- `pandas.util.version`
- `pandas.core.computation.eval`
- `numexpr`
- `numexpr`

**Setup Required:**
```python
# Fixtures: engine, column
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=[column, 'b'])
```

### Step 2: Assign expected = value

```python
expected = df[df[column] > 5]
```

### Step 3: Assign query_string = value

```python
query_string = f'`{column}` > 5'
```

### Step 4: Assign result = df.query(...)

```python
result = df.query(query_string, engine=engine)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine, column

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=[column, 'b'])
expected = df[df[column] > 5]
query_string = f'`{column}` > 5'
result = df.query(query_string, engine=engine)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_eval.py:1930 | Complexity: Intermediate | Last updated: 2026-06-02*