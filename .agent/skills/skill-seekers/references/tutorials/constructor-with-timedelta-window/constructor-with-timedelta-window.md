# How To: Constructor With Timedelta Window

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor with timedelta window

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: window
```

## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': np.arange(n)}, index=date_range('2015-12-24', periods=n, freq='D'))
```

### Step 3: Assign expected_data = np.append(...)

```python
expected_data = np.append([0.0, 1.0], np.arange(3.0, 27.0, 3))
```

### Step 4: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window=window).sum()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': expected_data}, index=date_range('2015-12-24', periods=n, freq='D'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = df.rolling.sum(...)

```python
expected = df.rolling('3D').sum()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: window

# Workflow
n = 10
df = DataFrame({'value': np.arange(n)}, index=date_range('2015-12-24', periods=n, freq='D'))
expected_data = np.append([0.0, 1.0], np.arange(3.0, 27.0, 3))
result = df.rolling(window=window).sum()
expected = DataFrame({'value': expected_data}, index=date_range('2015-12-24', periods=n, freq='D'))
tm.assert_frame_equal(result, expected)
expected = df.rolling('3D').sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:117 | Complexity: Advanced | Last updated: 2026-06-02*