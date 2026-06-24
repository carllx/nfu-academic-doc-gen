# How To: Groupby Raises Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby raises datetime

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
# Fixtures: how, by, groupby_series, groupby_func, df_with_datetime_col
```

## Step-by-Step Guide

### Step 1: Assign df = df_with_datetime_col

```python
df = df_with_datetime_col
```

**Verification:**
```python
assert not hasattr(gb, 'corrwith')
```

### Step 2: Assign args = get_groupby_method_args(...)

```python
args = get_groupby_method_args(groupby_func, df)
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby(by=by)
```

### Step 4: Assign unknown = value

```python
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, 'cannot perform __mul__ with this index type'), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': (None, ''), 'cummin': (None, ''), 'cumprod': (TypeError, 'datetime64 type does not support cumprod operations'), 'cumsum': (TypeError, 'datetime64 type does not support cumsum operations'), 'diff': (None, ''), 'ffill': (None, ''), 'fillna': (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (None, ''), 'median': (None, ''), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, 'cannot perform __truediv__ with this index type'), 'prod': (TypeError, 'datetime64 type does not support prod'), 'quantile': (None, ''), 'rank': (None, ''), 'sem': (None, ''), 'shift': (None, ''), 'size': (None, ''), 'skew': (TypeError, '|'.join(['dtype datetime64\\[ns\\] does not support reduction', 'datetime64 type does not support skew operations'])), 'std': (None, ''), 'sum': (TypeError, 'datetime64 type does not support sum operations'), 'var': (TypeError, 'datetime64 type does not support var operations')}[groupby_func]
```

### Step 5: Call _call_and_check()

```python
_call_and_check(klass, msg, how, gb, groupby_func, args, warn_msg=warn_msg)
```

### Step 6: Assign gb = value

```python
gb = gb['d']
```

### Step 7: Assign warn_msg = value

```python
warn_msg = f"'{groupby_func}' with datetime64 dtypes is deprecated"
```

**Verification:**
```python
assert not hasattr(gb, 'corrwith')
```

### Step 8: Assign kind = value

```python
kind = 'Series' if groupby_series else 'DataFrame'
```

### Step 9: Assign warn_msg = value

```python
warn_msg = f'{kind}GroupBy.fillna is deprecated'
```

### Step 10: Assign warn_msg = ''

```python
warn_msg = ''
```


## Complete Example

```python
# Setup
# Fixtures: how, by, groupby_series, groupby_func, df_with_datetime_col

# Workflow
df = df_with_datetime_col
args = get_groupby_method_args(groupby_func, df)
gb = df.groupby(by=by)
if groupby_series:
    gb = gb['d']
    if groupby_func == 'corrwith':
        assert not hasattr(gb, 'corrwith')
        return
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, 'cannot perform __mul__ with this index type'), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': (None, ''), 'cummin': (None, ''), 'cumprod': (TypeError, 'datetime64 type does not support cumprod operations'), 'cumsum': (TypeError, 'datetime64 type does not support cumsum operations'), 'diff': (None, ''), 'ffill': (None, ''), 'fillna': (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (None, ''), 'median': (None, ''), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, 'cannot perform __truediv__ with this index type'), 'prod': (TypeError, 'datetime64 type does not support prod'), 'quantile': (None, ''), 'rank': (None, ''), 'sem': (None, ''), 'shift': (None, ''), 'size': (None, ''), 'skew': (TypeError, '|'.join(['dtype datetime64\\[ns\\] does not support reduction', 'datetime64 type does not support skew operations'])), 'std': (None, ''), 'sum': (TypeError, 'datetime64 type does not support sum operations'), 'var': (TypeError, 'datetime64 type does not support var operations')}[groupby_func]
if groupby_func in ['any', 'all']:
    warn_msg = f"'{groupby_func}' with datetime64 dtypes is deprecated"
elif groupby_func == 'fillna':
    kind = 'Series' if groupby_series else 'DataFrame'
    warn_msg = f'{kind}GroupBy.fillna is deprecated'
else:
    warn_msg = ''
_call_and_check(klass, msg, how, gb, groupby_func, args, warn_msg=warn_msg)
```

## Next Steps


---

*Source: test_raises.py:288 | Complexity: Advanced | Last updated: 2026-06-02*