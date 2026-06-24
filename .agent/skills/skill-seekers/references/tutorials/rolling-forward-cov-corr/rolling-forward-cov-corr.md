# How To: Rolling Forward Cov Corr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling forward cov corr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: func, expected
```

## Step-by-Step Guide

### Step 1: Assign values1 = np.arange.reshape(...)

```python
values1 = np.arange(10).reshape(-1, 1)
```

### Step 2: Assign values2 = value

```python
values2 = values1 * 2
```

### Step 3: Assign unknown = 100

```python
values1[5, 0] = 100
```

### Step 4: Assign values = np.concatenate(...)

```python
values = np.concatenate([values1, values2], axis=1)
```

### Step 5: Assign indexer = FixedForwardWindowIndexer(...)

```python
indexer = FixedForwardWindowIndexer(window_size=3)
```

### Step 6: Assign rolling = DataFrame.rolling(...)

```python
rolling = DataFrame(values).rolling(window=indexer, min_periods=3)
```

### Step 7: Assign result = value

```python
result = getattr(rolling, func)().loc[(slice(None), 1), 0]
```

### Step 8: Assign result = result.reset_index(...)

```python
result = result.reset_index(drop=True)
```

### Step 9: Assign expected = Series.reset_index(...)

```python
expected = Series(expected).reset_index(drop=True)
```

### Step 10: Assign expected.name = value

```python
expected.name = result.name
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: func, expected

# Workflow
values1 = np.arange(10).reshape(-1, 1)
values2 = values1 * 2
values1[5, 0] = 100
values = np.concatenate([values1, values2], axis=1)
indexer = FixedForwardWindowIndexer(window_size=3)
rolling = DataFrame(values).rolling(window=indexer, min_periods=3)
result = getattr(rolling, func)().loc[(slice(None), 1), 0]
result = result.reset_index(drop=True)
expected = Series(expected).reset_index(drop=True)
expected.name = result.name
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:238 | Complexity: Advanced | Last updated: 2026-06-02*