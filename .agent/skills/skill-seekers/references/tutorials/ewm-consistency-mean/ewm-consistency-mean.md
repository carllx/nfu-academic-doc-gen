# How To: Ewm Consistency Mean

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test ewm consistency mean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_data, adjust, ignore_na, min_periods
```

## Step-by-Step Guide

### Step 1: Assign com = 3.0

```python
com = 3.0
```

### Step 2: Assign result = all_data.ewm.mean(...)

```python
result = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 3: Assign weights = create_mock_weights(...)

```python
weights = create_mock_weights(all_data, com=com, adjust=adjust, ignore_na=ignore_na)
```

### Step 4: Assign expected = all_data.multiply.cumsum.divide.ffill(...)

```python
expected = all_data.multiply(weights).cumsum().divide(weights.cumsum()).ffill()
```

### Step 5: Assign unknown = value

```python
expected[all_data.expanding().count() < (max(min_periods, 1) if min_periods else 1)] = np.nan
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected.astype('float64'))
```


## Complete Example

```python
# Setup
# Fixtures: all_data, adjust, ignore_na, min_periods

# Workflow
com = 3.0
result = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
weights = create_mock_weights(all_data, com=com, adjust=adjust, ignore_na=ignore_na)
expected = all_data.multiply(weights).cumsum().divide(weights.cumsum()).ffill()
expected[all_data.expanding().count() < (max(min_periods, 1) if min_periods else 1)] = np.nan
tm.assert_equal(result, expected.astype('float64'))
```

## Next Steps


---

*Source: test_moments_consistency_ewm.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*