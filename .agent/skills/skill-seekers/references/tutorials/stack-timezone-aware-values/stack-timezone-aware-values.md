# How To: Stack Timezone Aware Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test stack timezone aware values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`

**Setup Required:**
```python
# Fixtures: future_stack
```

## Step-by-Step Guide

### Step 1: Assign ts = date_range(...)

```python
ts = date_range(freq='D', start='20180101', end='20180103', tz='America/New_York')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ts}, index=['a', 'b', 'c'])
```

### Step 3: Assign result = df.stack(...)

```python
result = df.stack(future_stack=future_stack)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(ts, index=MultiIndex(levels=[['a', 'b', 'c'], ['A']], codes=[[0, 1, 2], [0, 0, 0]]))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: future_stack

# Workflow
ts = date_range(freq='D', start='20180101', end='20180103', tz='America/New_York')
df = DataFrame({'A': ts}, index=['a', 'b', 'c'])
result = df.stack(future_stack=future_stack)
expected = Series(ts, index=MultiIndex(levels=[['a', 'b', 'c'], ['A']], codes=[[0, 1, 2], [0, 0, 0]]))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1405 | Complexity: Intermediate | Last updated: 2026-06-02*