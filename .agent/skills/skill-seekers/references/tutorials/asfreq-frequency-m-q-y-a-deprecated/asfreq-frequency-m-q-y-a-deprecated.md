# How To: Asfreq Frequency M Q Y A Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test asfreq frequency M Q Y A deprecated

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: freq, freq_depr
```

## Step-by-Step Guide

### Step 1: Assign depr_msg = value

```python
depr_msg = f"'{freq_depr[1:]}' is deprecated and will be removed "
```

### Step 2: f"in a future version, please use '{freq[1:]}' instead."

```python
f"in a future version, please use '{freq[1:]}' instead."
```

### Step 3: Assign index = date_range(...)

```python
index = date_range('1/1/2000', periods=4, freq=f'{freq[1:]}')
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'s': Series([0.0, 1.0, 2.0, 3.0], index=index)})
```

### Step 5: Assign expected = df.asfreq(...)

```python
expected = df.asfreq(freq=freq)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = df.asfreq(...)

```python
result = df.asfreq(freq=freq_depr)
```


## Complete Example

```python
# Setup
# Fixtures: freq, freq_depr

# Workflow
depr_msg = f"'{freq_depr[1:]}' is deprecated and will be removed "
f"in a future version, please use '{freq[1:]}' instead."
index = date_range('1/1/2000', periods=4, freq=f'{freq[1:]}')
df = DataFrame({'s': Series([0.0, 1.0, 2.0, 3.0], index=index)})
expected = df.asfreq(freq=freq)
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    result = df.asfreq(freq=freq_depr)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_asfreq.py:253 | Complexity: Intermediate | Last updated: 2026-06-02*