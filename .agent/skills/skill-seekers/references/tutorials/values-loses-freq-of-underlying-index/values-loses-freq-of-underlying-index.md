# How To: Values Loses Freq Of Underlying Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values loses freq of underlying index

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign idx = pd.DatetimeIndex(...)

```python
idx = pd.DatetimeIndex(date_range('20200101', periods=3, freq='BME'))
```

**Verification:**
```python
assert idx.freq is not None
```

### Step 2: Assign expected = idx.copy(...)

```python
expected = idx.copy(deep=True)
```

### Step 3: Assign idx2 = Index(...)

```python
idx2 = Index([1, 2, 3])
```

### Step 4: Assign midx = MultiIndex(...)

```python
midx = MultiIndex(levels=[idx, idx2], codes=[[0, 1, 2], [0, 1, 2]])
```

### Step 5: midx.values

```python
midx.values
```

**Verification:**
```python
assert idx.freq is not None
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```


## Complete Example

```python
# Workflow
idx = pd.DatetimeIndex(date_range('20200101', periods=3, freq='BME'))
expected = idx.copy(deep=True)
idx2 = Index([1, 2, 3])
midx = MultiIndex(levels=[idx, idx2], codes=[[0, 1, 2], [0, 1, 2]])
midx.values
assert idx.freq is not None
tm.assert_index_equal(idx, expected)
```

## Next Steps


---

*Source: test_get_level_values.py:116 | Complexity: Intermediate | Last updated: 2026-06-02*