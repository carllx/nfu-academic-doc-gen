# How To: Fillna Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna datetime

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
# Fixtures: datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign tf = datetime_frame

```python
tf = datetime_frame
```

**Verification:**
```python
assert (zero_filled.loc[zero_filled.index[:5], 'A'] == 0).all()
```

### Step 2: Assign unknown = value

```python
tf.loc[tf.index[:5], 'A'] = np.nan
```

**Verification:**
```python
assert np.isnan(padded.loc[padded.index[:5], 'A']).all()
```

### Step 3: Assign unknown = value

```python
tf.loc[tf.index[-5:], 'A'] = np.nan
```

**Verification:**
```python
assert (padded.loc[padded.index[-5:], 'A'] == padded.loc[padded.index[-5], 'A']).all()
```

### Step 4: Assign zero_filled = datetime_frame.fillna(...)

```python
zero_filled = datetime_frame.fillna(0)
```

**Verification:**
```python
assert (zero_filled.loc[zero_filled.index[:5], 'A'] == 0).all()
```

### Step 5: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

**Verification:**
```python
assert np.isnan(padded.loc[padded.index[:5], 'A']).all()
```

### Step 6: Assign msg = "Must specify a fill 'value' or 'method'"

```python
msg = "Must specify a fill 'value' or 'method'"
```

### Step 7: Assign msg = "Cannot specify both 'value' and 'method'"

```python
msg = "Cannot specify both 'value' and 'method'"
```

### Step 8: Assign padded = datetime_frame.fillna(...)

```python
padded = datetime_frame.fillna(method='pad')
```

### Step 9: Call datetime_frame.fillna()

```python
datetime_frame.fillna()
```

### Step 10: Call datetime_frame.fillna()

```python
datetime_frame.fillna(5, method='ffill')
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame

# Workflow
tf = datetime_frame
tf.loc[tf.index[:5], 'A'] = np.nan
tf.loc[tf.index[-5:], 'A'] = np.nan
zero_filled = datetime_frame.fillna(0)
assert (zero_filled.loc[zero_filled.index[:5], 'A'] == 0).all()
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    padded = datetime_frame.fillna(method='pad')
assert np.isnan(padded.loc[padded.index[:5], 'A']).all()
assert (padded.loc[padded.index[-5:], 'A'] == padded.loc[padded.index[-5], 'A']).all()
msg = "Must specify a fill 'value' or 'method'"
with pytest.raises(ValueError, match=msg):
    datetime_frame.fillna()
msg = "Cannot specify both 'value' and 'method'"
with pytest.raises(ValueError, match=msg):
    datetime_frame.fillna(5, method='ffill')
```

## Next Steps


---

*Source: test_fillna.py:73 | Complexity: Advanced | Last updated: 2026-06-02*