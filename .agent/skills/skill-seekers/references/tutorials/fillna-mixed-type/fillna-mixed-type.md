# How To: Fillna Mixed Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna mixed type

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
# Fixtures: float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign mf = float_string_frame

```python
mf = float_string_frame
```

### Step 2: Assign unknown = value

```python
mf.loc[mf.index[5:20], 'foo'] = np.nan
```

### Step 3: Assign unknown = value

```python
mf.loc[mf.index[-10:], 'A'] = np.nan
```

### Step 4: Call mf.fillna()

```python
mf.fillna(value=0)
```

### Step 5: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 6: Call mf.fillna()

```python
mf.fillna(method='pad')
```


## Complete Example

```python
# Setup
# Fixtures: float_string_frame

# Workflow
mf = float_string_frame
mf.loc[mf.index[5:20], 'foo'] = np.nan
mf.loc[mf.index[-10:], 'A'] = np.nan
mf.fillna(value=0)
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    mf.fillna(method='pad')
```

## Next Steps


---

*Source: test_fillna.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*