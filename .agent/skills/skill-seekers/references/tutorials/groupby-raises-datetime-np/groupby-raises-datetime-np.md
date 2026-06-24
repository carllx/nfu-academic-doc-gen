# How To: Groupby Raises Datetime Np

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby raises datetime np

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: how, by, groupby_series, groupby_func_np, df_with_datetime_col
```

## Step-by-Step Guide

### Step 1: Assign df = df_with_datetime_col

```python
df = df_with_datetime_col
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby(by=by)
```

### Step 3: Assign unknown = value

```python
klass, msg = {np.sum: (TypeError, 'datetime64 type does not support sum operations'), np.mean: (None, '')}[groupby_func_np]
```

### Step 4: Call _call_and_check()

```python
_call_and_check(klass, msg, how, gb, groupby_func_np, (), warn_msg=warn_msg)
```

### Step 5: Assign gb = value

```python
gb = gb['d']
```

### Step 6: Assign warn_msg = 'using SeriesGroupBy.[sum|mean]'

```python
warn_msg = 'using SeriesGroupBy.[sum|mean]'
```

### Step 7: Assign warn_msg = 'using DataFrameGroupBy.[sum|mean]'

```python
warn_msg = 'using DataFrameGroupBy.[sum|mean]'
```


## Complete Example

```python
# Setup
# Fixtures: how, by, groupby_series, groupby_func_np, df_with_datetime_col

# Workflow
df = df_with_datetime_col
gb = df.groupby(by=by)
if groupby_series:
    gb = gb['d']
klass, msg = {np.sum: (TypeError, 'datetime64 type does not support sum operations'), np.mean: (None, '')}[groupby_func_np]
if groupby_series:
    warn_msg = 'using SeriesGroupBy.[sum|mean]'
else:
    warn_msg = 'using DataFrameGroupBy.[sum|mean]'
_call_and_check(klass, msg, how, gb, groupby_func_np, (), warn_msg=warn_msg)
```

## Next Steps


---

*Source: test_raises.py:374 | Complexity: Intermediate | Last updated: 2026-06-02*