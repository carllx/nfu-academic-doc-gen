# How To: Groupby Raises String

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby raises string

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
# Fixtures: how, by, groupby_series, groupby_func, df_with_string_col, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = df_with_string_col

```python
df = df_with_string_col
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
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, 'Could not convert'), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': ((NotImplementedError, TypeError), '(function|cummax) is not (implemented|supported) for (this|object) dtype'), 'cummin': ((NotImplementedError, TypeError), '(function|cummin) is not (implemented|supported) for (this|object) dtype'), 'cumprod': ((NotImplementedError, TypeError), '(function|cumprod) is not (implemented|supported) for (this|object) dtype'), 'cumsum': ((NotImplementedError, TypeError), '(function|cumsum) is not (implemented|supported) for (this|object) dtype'), 'diff': (TypeError, 'unsupported operand type'), 'ffill': (None, ''), 'fillna': (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (TypeError, re.escape('agg function failed [how->mean,dtype->object]')), 'median': (TypeError, re.escape('agg function failed [how->median,dtype->object]')), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, 'unsupported operand type'), 'prod': (TypeError, re.escape('agg function failed [how->prod,dtype->object]')), 'quantile': (TypeError, "dtype 'object' does not support operation 'quantile'"), 'rank': (None, ''), 'sem': (ValueError, 'could not convert string to float'), 'shift': (None, ''), 'size': (None, ''), 'skew': (ValueError, 'could not convert string to float'), 'std': (ValueError, 'could not convert string to float'), 'sum': (None, ''), 'var': (TypeError, re.escape('agg function failed [how->var,dtype->'))}[groupby_func]
```

### Step 5: Call _call_and_check()

```python
_call_and_check(klass, msg, how, gb, groupby_func, args, warn_msg)
```

### Step 6: Assign gb = value

```python
gb = gb['d']
```

### Step 7: Assign kind = value

```python
kind = 'Series' if groupby_series else 'DataFrame'
```

### Step 8: Assign warn_msg = value

```python
warn_msg = f'{kind}GroupBy.fillna is deprecated'
```

### Step 9: Assign warn_msg = ''

```python
warn_msg = ''
```

**Verification:**
```python
assert not hasattr(gb, 'corrwith')
```

### Step 10: Assign msg = value

```python
msg = f"dtype 'str' does not support operation '{groupby_func}'"
```

### Step 11: Assign klass = TypeError

```python
klass = TypeError
```

### Step 12: Assign msg = "operation 'truediv' not supported for dtype 'str' with dtype 'str'"

```python
msg = "operation 'truediv' not supported for dtype 'str' with dtype 'str'"
```

### Step 13: Assign msg = "operation 'sub' not supported for dtype 'str' with dtype 'str'"

```python
msg = "operation 'sub' not supported for dtype 'str' with dtype 'str'"
```

### Step 14: Assign msg = msg.replace(...)

```python
msg = msg.replace('object', 'str')
```

### Step 15: Assign msg = "Cannot perform reduction 'mean' with string dtype"

```python
msg = "Cannot perform reduction 'mean' with string dtype"
```


## Complete Example

```python
# Setup
# Fixtures: how, by, groupby_series, groupby_func, df_with_string_col, using_infer_string

# Workflow
df = df_with_string_col
args = get_groupby_method_args(groupby_func, df)
gb = df.groupby(by=by)
if groupby_series:
    gb = gb['d']
    if groupby_func == 'corrwith':
        assert not hasattr(gb, 'corrwith')
        return
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, 'Could not convert'), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': ((NotImplementedError, TypeError), '(function|cummax) is not (implemented|supported) for (this|object) dtype'), 'cummin': ((NotImplementedError, TypeError), '(function|cummin) is not (implemented|supported) for (this|object) dtype'), 'cumprod': ((NotImplementedError, TypeError), '(function|cumprod) is not (implemented|supported) for (this|object) dtype'), 'cumsum': ((NotImplementedError, TypeError), '(function|cumsum) is not (implemented|supported) for (this|object) dtype'), 'diff': (TypeError, 'unsupported operand type'), 'ffill': (None, ''), 'fillna': (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (TypeError, re.escape('agg function failed [how->mean,dtype->object]')), 'median': (TypeError, re.escape('agg function failed [how->median,dtype->object]')), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, 'unsupported operand type'), 'prod': (TypeError, re.escape('agg function failed [how->prod,dtype->object]')), 'quantile': (TypeError, "dtype 'object' does not support operation 'quantile'"), 'rank': (None, ''), 'sem': (ValueError, 'could not convert string to float'), 'shift': (None, ''), 'size': (None, ''), 'skew': (ValueError, 'could not convert string to float'), 'std': (ValueError, 'could not convert string to float'), 'sum': (None, ''), 'var': (TypeError, re.escape('agg function failed [how->var,dtype->'))}[groupby_func]
if using_infer_string:
    if groupby_func in ['prod', 'mean', 'median', 'cumsum', 'cumprod', 'std', 'sem', 'var', 'skew', 'quantile']:
        msg = f"dtype 'str' does not support operation '{groupby_func}'"
        if groupby_func in ['sem', 'std', 'skew']:
            klass = TypeError
    elif groupby_func == 'pct_change' and df['d'].dtype.storage == 'pyarrow':
        msg = "operation 'truediv' not supported for dtype 'str' with dtype 'str'"
    elif groupby_func == 'diff' and df['d'].dtype.storage == 'pyarrow':
        msg = "operation 'sub' not supported for dtype 'str' with dtype 'str'"
    elif groupby_func in ['cummin', 'cummax']:
        msg = msg.replace('object', 'str')
    elif groupby_func == 'corrwith':
        msg = "Cannot perform reduction 'mean' with string dtype"
if groupby_func == 'fillna':
    kind = 'Series' if groupby_series else 'DataFrame'
    warn_msg = f'{kind}GroupBy.fillna is deprecated'
else:
    warn_msg = ''
_call_and_check(klass, msg, how, gb, groupby_func, args, warn_msg)
```

## Next Steps


---

*Source: test_raises.py:121 | Complexity: Advanced | Last updated: 2026-06-02*