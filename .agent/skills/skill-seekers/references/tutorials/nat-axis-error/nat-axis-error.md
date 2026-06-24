# How To: Nat Axis Error

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat axis error

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: msg, axis
```

## Step-by-Step Guide

### Step 1: Assign idx = value

```python
idx = [Timestamp('2020'), NaT]
```

### Step 2: Assign kwargs = value

```python
kwargs = {'columns' if axis == 1 else 'index': idx}
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.eye(2), **kwargs)
```

### Step 4: Assign warn_msg = "The 'axis' keyword in DataFrame.rolling is deprecated"

```python
warn_msg = "The 'axis' keyword in DataFrame.rolling is deprecated"
```

### Step 5: Assign warn_msg = 'Support for axis=1 in DataFrame.rolling is deprecated'

```python
warn_msg = 'Support for axis=1 in DataFrame.rolling is deprecated'
```

### Step 6: Call df.rolling.mean()

```python
df.rolling('D', axis=axis).mean()
```


## Complete Example

```python
# Setup
# Fixtures: msg, axis

# Workflow
idx = [Timestamp('2020'), NaT]
kwargs = {'columns' if axis == 1 else 'index': idx}
df = DataFrame(np.eye(2), **kwargs)
warn_msg = "The 'axis' keyword in DataFrame.rolling is deprecated"
if axis == 1:
    warn_msg = 'Support for axis=1 in DataFrame.rolling is deprecated'
with pytest.raises(ValueError, match=f'{msg} values must not have NaT'):
    with tm.assert_produces_warning(FutureWarning, match=warn_msg):
        df.rolling('D', axis=axis).mean()
```

## Next Steps


---

*Source: test_timeseries_window.py:693 | Complexity: Intermediate | Last updated: 2026-06-02*