# How To: Closed Fixed Binary Col

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test closed fixed binary col

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
# Fixtures: center, step
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [0, 1, 1, 0, 0, 1, 0, 1]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'binary_col': data}, index=date_range(start='2020-01-01', freq='min', periods=len(data)))
```

### Step 3: Assign expected = value

```python
expected = DataFrame(expected_data, columns=['binary_col'], index=date_range(start='2020-01-01', freq='min', periods=len(expected_data)))[::step]
```

### Step 4: Assign rolling = df.rolling(...)

```python
rolling = df.rolling(window=len(df), closed='left', min_periods=1, center=center, step=step)
```

### Step 5: Assign result = rolling.mean(...)

```python
result = rolling.mean()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected_data = value

```python
expected_data = [2 / 3, 0.5, 0.4, 0.5, 0.428571, 0.5, 0.571429, 0.5]
```

### Step 8: Assign expected_data = value

```python
expected_data = [np.nan, 0, 0.5, 2 / 3, 0.5, 0.4, 0.5, 0.428571]
```


## Complete Example

```python
# Setup
# Fixtures: center, step

# Workflow
data = [0, 1, 1, 0, 0, 1, 0, 1]
df = DataFrame({'binary_col': data}, index=date_range(start='2020-01-01', freq='min', periods=len(data)))
if center:
    expected_data = [2 / 3, 0.5, 0.4, 0.5, 0.428571, 0.5, 0.571429, 0.5]
else:
    expected_data = [np.nan, 0, 0.5, 2 / 3, 0.5, 0.4, 0.5, 0.428571]
expected = DataFrame(expected_data, columns=['binary_col'], index=date_range(start='2020-01-01', freq='min', periods=len(expected_data)))[::step]
rolling = df.rolling(window=len(df), closed='left', min_periods=1, center=center, step=step)
result = rolling.mean()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:391 | Complexity: Advanced | Last updated: 2026-06-02*