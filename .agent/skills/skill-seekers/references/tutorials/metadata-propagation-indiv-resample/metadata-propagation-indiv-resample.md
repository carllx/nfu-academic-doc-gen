# How To: Metadata Propagation Indiv Resample

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test metadata propagation indiv resample

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).random(1000), index=date_range('20130101', periods=1000, freq='s'), name='foo')
```

### Step 2: Assign result = ts.resample.mean(...)

```python
result = ts.resample('1min').mean()
```

### Step 3: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(ts, result)
```

### Step 4: Assign result = ts.resample.min(...)

```python
result = ts.resample('1min').min()
```

### Step 5: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(ts, result)
```

### Step 6: Assign result = ts.resample.apply(...)

```python
result = ts.resample('1min').apply(lambda x: x.sum())
```

### Step 7: Call tm.assert_metadata_equivalent()

```python
tm.assert_metadata_equivalent(ts, result)
```


## Complete Example

```python
# Workflow
ts = Series(np.random.default_rng(2).random(1000), index=date_range('20130101', periods=1000, freq='s'), name='foo')
result = ts.resample('1min').mean()
tm.assert_metadata_equivalent(ts, result)
result = ts.resample('1min').min()
tm.assert_metadata_equivalent(ts, result)
result = ts.resample('1min').apply(lambda x: x.sum())
tm.assert_metadata_equivalent(ts, result)
```

## Next Steps


---

*Source: test_series.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*