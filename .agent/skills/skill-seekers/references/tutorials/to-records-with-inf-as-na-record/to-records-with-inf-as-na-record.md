# How To: To Records With Inf As Na Record

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records with inf as na record

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = '   NaN  inf         record\n0  inf    b    [0, inf, b]\n1  NaN  NaN  [1, nan, nan]\n2    e    f      [2, e, f]'

```python
expected = '   NaN  inf         record\n0  inf    b    [0, inf, b]\n1  NaN  NaN  [1, nan, nan]\n2    e    f      [2, e, f]'
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([[np.inf, 'b'], [np.nan, np.nan], ['e', 'f']], columns=[np.nan, np.inf])
```

### Step 4: Assign unknown = unknown.to_records(...)

```python
df['record'] = df[[np.nan, np.inf]].to_records()
```

### Step 5: Assign result = repr(...)

```python
result = repr(df)
```


## Complete Example

```python
# Workflow
expected = '   NaN  inf         record\n0  inf    b    [0, inf, b]\n1  NaN  NaN  [1, nan, nan]\n2    e    f      [2, e, f]'
msg = 'use_inf_as_na option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with option_context('use_inf_as_na', True):
        df = DataFrame([[np.inf, 'b'], [np.nan, np.nan], ['e', 'f']], columns=[np.nan, np.inf])
        df['record'] = df[[np.nan, np.inf]].to_records()
        result = repr(df)
assert result == expected
```

## Next Steps


---

*Source: test_repr.py:425 | Complexity: Intermediate | Last updated: 2026-06-02*