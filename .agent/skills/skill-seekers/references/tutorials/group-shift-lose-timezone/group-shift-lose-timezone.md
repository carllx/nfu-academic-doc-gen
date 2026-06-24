# How To: Group Shift Lose Timezone

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group shift lose timezone

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign now_dt = Timestamp.utcnow.as_unit(...)

```python
now_dt = Timestamp.utcnow().as_unit('ns')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1], 'date': now_dt})
```

### Step 3: Assign result = value

```python
result = df.groupby('a').shift(0).iloc[0]
```

### Step 4: Assign expected = Series(...)

```python
expected = Series({'date': now_dt}, name=result.name)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
now_dt = Timestamp.utcnow().as_unit('ns')
df = DataFrame({'a': [1, 1], 'date': now_dt})
result = df.groupby('a').shift(0).iloc[0]
expected = Series({'date': now_dt}, name=result.name)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_shift_diff.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*