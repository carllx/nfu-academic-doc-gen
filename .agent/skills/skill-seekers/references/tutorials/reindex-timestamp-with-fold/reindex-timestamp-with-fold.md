# How To: Reindex Timestamp With Fold

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reindex timestamp with fold

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: timezone, year, month, day, hour
```

## Step-by-Step Guide

### Step 1: Assign test_timezone = gettz(...)

```python
test_timezone = gettz(timezone)
```

### Step 2: Assign transition_1 = pd.Timestamp(...)

```python
transition_1 = pd.Timestamp(year=year, month=month, day=day, hour=hour, minute=0, fold=0, tzinfo=test_timezone)
```

### Step 3: Assign transition_2 = pd.Timestamp(...)

```python
transition_2 = pd.Timestamp(year=year, month=month, day=day, hour=hour, minute=0, fold=1, tzinfo=test_timezone)
```

### Step 4: Assign df = DataFrame.set_index.reindex(...)

```python
df = DataFrame({'index': [transition_1, transition_2], 'vals': ['a', 'b']}).set_index('index').reindex(['1', '2'])
```

### Step 5: Assign exp = DataFrame.set_index(...)

```python
exp = DataFrame({'index': ['1', '2'], 'vals': [np.nan, np.nan]}).set_index('index')
```

### Step 6: Assign exp = exp.astype(...)

```python
exp = exp.astype(df.vals.dtype)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```


## Complete Example

```python
# Setup
# Fixtures: timezone, year, month, day, hour

# Workflow
test_timezone = gettz(timezone)
transition_1 = pd.Timestamp(year=year, month=month, day=day, hour=hour, minute=0, fold=0, tzinfo=test_timezone)
transition_2 = pd.Timestamp(year=year, month=month, day=day, hour=hour, minute=0, fold=1, tzinfo=test_timezone)
df = DataFrame({'index': [transition_1, transition_2], 'vals': ['a', 'b']}).set_index('index').reindex(['1', '2'])
exp = DataFrame({'index': ['1', '2'], 'vals': [np.nan, np.nan]}).set_index('index')
exp = exp.astype(df.vals.dtype)
tm.assert_frame_equal(df, exp)
```

## Next Steps


---

*Source: test_reindex.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*