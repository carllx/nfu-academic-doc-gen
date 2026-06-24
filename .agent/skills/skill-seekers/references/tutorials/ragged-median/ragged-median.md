# How To: Ragged Median

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ragged median

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
# Fixtures: ragged
```

## Step-by-Step Guide

### Step 1: Assign df = ragged

```python
df = ragged
```

### Step 2: Assign result = df.rolling.median(...)

```python
result = df.rolling(window='1s', min_periods=1).median()
```

### Step 3: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 4: Assign unknown = value

```python
expected['B'] = [0.0, 1, 2, 3, 4]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = df.rolling.median(...)

```python
result = df.rolling(window='2s', min_periods=1).median()
```

### Step 7: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 8: Assign unknown = value

```python
expected['B'] = [0.0, 1, 1.5, 3.0, 3.5]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ragged

# Workflow
df = ragged
result = df.rolling(window='1s', min_periods=1).median()
expected = df.copy()
expected['B'] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)
result = df.rolling(window='2s', min_periods=1).median()
expected = df.copy()
expected['B'] = [0.0, 1, 1.5, 3.0, 3.5]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timeseries_window.py:356 | Complexity: Advanced | Last updated: 2026-06-02*