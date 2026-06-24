# How To: Groupby Raises Category

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby raises category

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
# Fixtures: how, by, groupby_series, groupby_func, using_copy_on_write, df_with_cat_col
```

## Step-by-Step Guide

### Step 1: Assign df = df_with_cat_col

```python
df = df_with_cat_col
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
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, "unsupported operand type\\(s\\) for \\*: 'Categorical' and 'int'"), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': ((NotImplementedError, TypeError), '(category type does not support cummax operations|category dtype not supported|cummax is not supported for category dtype)'), 'cummin': ((NotImplementedError, TypeError), '(category type does not support cummin operations|category dtype not supported|cummin is not supported for category dtype)'), 'cumprod': ((NotImplementedError, TypeError), '(category type does not support cumprod operations|category dtype not supported|cumprod is not supported for category dtype)'), 'cumsum': ((NotImplementedError, TypeError), '(category type does not support cumsum operations|category dtype not supported|cumsum is not supported for category dtype)'), 'diff': (TypeError, "unsupported operand type\\(s\\) for -: 'Categorical' and 'Categorical'"), 'ffill': (None, ''), 'fillna': (TypeError, 'Cannot setitem on a Categorical with a new category \\(0\\), set the categories first') if not using_copy_on_write else (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'mean'", "category dtype does not support aggregation 'mean'"])), 'median': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'median'", "category dtype does not support aggregation 'median'"])), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, "unsupported operand type\\(s\\) for /: 'Categorical' and 'Categorical'"), 'prod': (TypeError, 'category type does not support prod operations'), 'quantile': (TypeError, 'No matching signature found'), 'rank': (None, ''), 'sem': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'sem'", "category dtype does not support aggregation 'sem'"])), 'shift': (None, ''), 'size': (None, ''), 'skew': (TypeError, '|'.join(["dtype category does not support reduction 'skew'", 'category type does not support skew operations'])), 'std': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'std'", "category dtype does not support aggregation 'std'"])), 'sum': (TypeError, 'category type does not support sum operations'), 'var': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'var'", "category dtype does not support aggregation 'var'"]))}[groupby_func]
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


## Complete Example

```python
# Setup
# Fixtures: how, by, groupby_series, groupby_func, using_copy_on_write, df_with_cat_col

# Workflow
df = df_with_cat_col
args = get_groupby_method_args(groupby_func, df)
gb = df.groupby(by=by)
if groupby_series:
    gb = gb['d']
    if groupby_func == 'corrwith':
        assert not hasattr(gb, 'corrwith')
        return
klass, msg = {'all': (None, ''), 'any': (None, ''), 'bfill': (None, ''), 'corrwith': (TypeError, "unsupported operand type\\(s\\) for \\*: 'Categorical' and 'int'"), 'count': (None, ''), 'cumcount': (None, ''), 'cummax': ((NotImplementedError, TypeError), '(category type does not support cummax operations|category dtype not supported|cummax is not supported for category dtype)'), 'cummin': ((NotImplementedError, TypeError), '(category type does not support cummin operations|category dtype not supported|cummin is not supported for category dtype)'), 'cumprod': ((NotImplementedError, TypeError), '(category type does not support cumprod operations|category dtype not supported|cumprod is not supported for category dtype)'), 'cumsum': ((NotImplementedError, TypeError), '(category type does not support cumsum operations|category dtype not supported|cumsum is not supported for category dtype)'), 'diff': (TypeError, "unsupported operand type\\(s\\) for -: 'Categorical' and 'Categorical'"), 'ffill': (None, ''), 'fillna': (TypeError, 'Cannot setitem on a Categorical with a new category \\(0\\), set the categories first') if not using_copy_on_write else (None, ''), 'first': (None, ''), 'idxmax': (None, ''), 'idxmin': (None, ''), 'last': (None, ''), 'max': (None, ''), 'mean': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'mean'", "category dtype does not support aggregation 'mean'"])), 'median': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'median'", "category dtype does not support aggregation 'median'"])), 'min': (None, ''), 'ngroup': (None, ''), 'nunique': (None, ''), 'pct_change': (TypeError, "unsupported operand type\\(s\\) for /: 'Categorical' and 'Categorical'"), 'prod': (TypeError, 'category type does not support prod operations'), 'quantile': (TypeError, 'No matching signature found'), 'rank': (None, ''), 'sem': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'sem'", "category dtype does not support aggregation 'sem'"])), 'shift': (None, ''), 'size': (None, ''), 'skew': (TypeError, '|'.join(["dtype category does not support reduction 'skew'", 'category type does not support skew operations'])), 'std': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'std'", "category dtype does not support aggregation 'std'"])), 'sum': (TypeError, 'category type does not support sum operations'), 'var': (TypeError, '|'.join(["'Categorical' .* does not support reduction 'var'", "category dtype does not support aggregation 'var'"]))}[groupby_func]
if groupby_func == 'fillna':
    kind = 'Series' if groupby_series else 'DataFrame'
    warn_msg = f'{kind}GroupBy.fillna is deprecated'
else:
    warn_msg = ''
_call_and_check(klass, msg, how, gb, groupby_func, args, warn_msg)
```

## Next Steps


---

*Source: test_raises.py:412 | Complexity: Advanced | Last updated: 2026-06-02*