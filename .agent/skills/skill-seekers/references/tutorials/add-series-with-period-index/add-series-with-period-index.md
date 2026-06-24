# How To: Add Series With Period Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add series with period index

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign rng = pd.period_range(...)

```python
rng = pd.period_range('1/1/2000', '1/1/2010', freq='Y')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 3: Assign result = value

```python
result = ts + ts[::2]
```

### Step 4: Assign expected = value

```python
expected = ts + ts
```

### Step 5: Assign unknown = value

```python
expected.iloc[1::2] = np.nan
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = ts + _permute(ts[::2])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign msg = 'Input has different freq=D from Period\\(freq=Y-DEC\\)'

```python
msg = 'Input has different freq=D from Period\\(freq=Y-DEC\\)'
```

### Step 10: ts + ts.asfreq('D', how='end')

```python
ts + ts.asfreq('D', how='end')
```


## Complete Example

```python
# Workflow
rng = pd.period_range('1/1/2000', '1/1/2010', freq='Y')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
result = ts + ts[::2]
expected = ts + ts
expected.iloc[1::2] = np.nan
tm.assert_series_equal(result, expected)
result = ts + _permute(ts[::2])
tm.assert_series_equal(result, expected)
msg = 'Input has different freq=D from Period\\(freq=Y-DEC\\)'
with pytest.raises(IncompatibleFrequency, match=msg):
    ts + ts.asfreq('D', how='end')
```

## Next Steps


---

*Source: test_arithmetic.py:163 | Complexity: Advanced | Last updated: 2026-06-02*