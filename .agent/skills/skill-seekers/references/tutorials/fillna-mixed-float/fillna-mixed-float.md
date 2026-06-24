# How To: Fillna Mixed Float

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna mixed float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`

**Setup Required:**
```python
# Fixtures: mixed_float_frame
```

## Step-by-Step Guide

### Step 1: Assign mf = mixed_float_frame.reindex(...)

```python
mf = mixed_float_frame.reindex(columns=['A', 'B', 'D'])
```

### Step 2: Assign unknown = value

```python
mf.loc[mf.index[-10:], 'A'] = np.nan
```

### Step 3: Assign result = mf.fillna(...)

```python
result = mf.fillna(value=0)
```

### Step 4: Call _check_mixed_float()

```python
_check_mixed_float(result, dtype={'C': None})
```

### Step 5: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 6: Call _check_mixed_float()

```python
_check_mixed_float(result, dtype={'C': None})
```

### Step 7: Assign result = mf.fillna(...)

```python
result = mf.fillna(method='pad')
```


## Complete Example

```python
# Setup
# Fixtures: mixed_float_frame

# Workflow
mf = mixed_float_frame.reindex(columns=['A', 'B', 'D'])
mf.loc[mf.index[-10:], 'A'] = np.nan
result = mf.fillna(value=0)
_check_mixed_float(result, dtype={'C': None})
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = mf.fillna(method='pad')
_check_mixed_float(result, dtype={'C': None})
```

## Next Steps


---

*Source: test_fillna.py:106 | Complexity: Intermediate | Last updated: 2026-06-02*