# How To: Cmov Window

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cmov window

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign vals = np.array(...)

```python
vals = np.array([6.95, 15.21, 4.72, 9.12, 13.81, 13.49, 16.68, 9.48, 10.63, 14.48])
```

### Step 3: Assign result = Series.rolling.mean(...)

```python
result = Series(vals).rolling(5, win_type='boxcar', center=True, step=step).mean()
```

### Step 4: Assign expected_values = value

```python
expected_values = [np.nan, np.nan, 9.962, 11.27, 11.564, 12.516, 12.818, 12.952, np.nan, np.nan]
```

### Step 5: Assign expected = value

```python
expected = Series(expected_values)[::step]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
pytest.importorskip('scipy')
vals = np.array([6.95, 15.21, 4.72, 9.12, 13.81, 13.49, 16.68, 9.48, 10.63, 14.48])
result = Series(vals).rolling(5, win_type='boxcar', center=True, step=step).mean()
expected_values = [np.nan, np.nan, 9.962, 11.27, 11.564, 12.516, 12.818, 12.952, np.nan, np.nan]
expected = Series(expected_values)[::step]
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_win_type.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*