# How To: Corr Scipy Method

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test corr scipy method

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame, method
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign unknown = value

```python
float_frame.loc[float_frame.index[:5], 'A'] = np.nan
```

### Step 3: Assign unknown = value

```python
float_frame.loc[float_frame.index[5:10], 'B'] = np.nan
```

### Step 4: Assign unknown = unknown.copy(...)

```python
float_frame.loc[float_frame.index[:10], 'A'] = float_frame['A'][10:20].copy()
```

### Step 5: Assign correls = float_frame.corr(...)

```python
correls = float_frame.corr(method=method)
```

### Step 6: Assign expected = unknown.corr(...)

```python
expected = float_frame['A'].corr(float_frame['C'], method=method)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(correls['A']['C'], expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, method

# Workflow
pytest.importorskip('scipy')
float_frame.loc[float_frame.index[:5], 'A'] = np.nan
float_frame.loc[float_frame.index[5:10], 'B'] = np.nan
float_frame.loc[float_frame.index[:10], 'A'] = float_frame['A'][10:20].copy()
correls = float_frame.corr(method=method)
expected = float_frame['A'].corr(float_frame['C'], method=method)
tm.assert_almost_equal(correls['A']['C'], expected)
```

## Next Steps


---

*Source: test_cov_corr.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*