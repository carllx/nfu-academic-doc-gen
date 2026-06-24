# How To: Asfreq 2Me

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test asfreq 2ME

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
# Fixtures: freq, freq_half
```

## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('1/1/2000', periods=6, freq=freq_half)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'s': Series([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], index=index)})
```

### Step 3: Assign expected = df.asfreq(...)

```python
expected = df.asfreq(freq=freq)
```

### Step 4: Assign index = date_range(...)

```python
index = date_range('1/1/2000', periods=3, freq=freq)
```

### Step 5: Assign result = DataFrame(...)

```python
result = DataFrame({'s': Series([0.0, 2.0, 4.0], index=index)})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: freq, freq_half

# Workflow
index = date_range('1/1/2000', periods=6, freq=freq_half)
df = DataFrame({'s': Series([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], index=index)})
expected = df.asfreq(freq=freq)
index = date_range('1/1/2000', periods=3, freq=freq)
result = DataFrame({'s': Series([0.0, 2.0, 4.0], index=index)})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_asfreq.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*