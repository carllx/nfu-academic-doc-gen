# How To: Constructor From Series Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from series freq

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `functools`
- `math`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`
- `pyarrow`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign dts = value

```python
dts = ['1-1-1990', '2-1-1990', '3-1-1990', '4-1-1990', '5-1-1990']
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(dts, freq='MS')
```

### Step 3: Assign s = Series(...)

```python
s = Series(pd.to_datetime(dts))
```

### Step 4: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(s, freq='MS')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dts = ['1-1-1990', '2-1-1990', '3-1-1990', '4-1-1990', '5-1-1990']
expected = DatetimeIndex(dts, freq='MS')
s = Series(pd.to_datetime(dts))
result = DatetimeIndex(s, freq='MS')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*