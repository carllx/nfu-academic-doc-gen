# How To: Sem

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sem

## Prerequisites

**Required Modules:**
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign string_series = Series(...)

```python
string_series = Series(range(20), dtype=np.float64, name='series')
```

**Verification:**
```python
assert pd.isna(result)
```

### Step 2: Assign datetime_series = Series(...)

```python
datetime_series = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
```

### Step 3: Assign alt = value

```python
alt = lambda x: np.std(x, ddof=1) / np.sqrt(len(x))
```

### Step 4: Call self._check_stat_op()

```python
self._check_stat_op('sem', alt, string_series)
```

### Step 5: Assign result = datetime_series.sem(...)

```python
result = datetime_series.sem(ddof=4)
```

### Step 6: Assign expected = value

```python
expected = np.std(datetime_series.values, ddof=4) / np.sqrt(len(datetime_series.values))
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 8: Assign s = value

```python
s = datetime_series.iloc[[0]]
```

### Step 9: Assign result = s.sem(...)

```python
result = s.sem(ddof=1)
```

**Verification:**
```python
assert pd.isna(result)
```


## Complete Example

```python
# Workflow
string_series = Series(range(20), dtype=np.float64, name='series')
datetime_series = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
alt = lambda x: np.std(x, ddof=1) / np.sqrt(len(x))
self._check_stat_op('sem', alt, string_series)
result = datetime_series.sem(ddof=4)
expected = np.std(datetime_series.values, ddof=4) / np.sqrt(len(datetime_series.values))
tm.assert_almost_equal(result, expected)
s = datetime_series.iloc[[0]]
result = s.sem(ddof=1)
assert pd.isna(result)
```

## Next Steps


---

*Source: test_stat_reductions.py:211 | Complexity: Advanced | Last updated: 2026-06-02*