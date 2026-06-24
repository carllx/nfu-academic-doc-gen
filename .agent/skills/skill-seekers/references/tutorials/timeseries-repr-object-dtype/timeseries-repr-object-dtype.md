# How To: Timeseries Repr Object Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timeseries repr object dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([datetime(2000, 1, 1) + timedelta(i) for i in range(1000)], dtype=object)
```

**Verification:**
```python
assert repr(ts).splitlines()[-1].startswith('Freq:')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(index)), index)
```

### Step 3: Call repr()

```python
repr(ts)
```

### Step 4: Assign ts = Series(...)

```python
ts = Series(np.arange(20, dtype=np.float64), index=date_range('2020-01-01', periods=20))
```

**Verification:**
```python
assert repr(ts).splitlines()[-1].startswith('Freq:')
```

### Step 5: Assign ts2 = value

```python
ts2 = ts.iloc[np.random.default_rng(2).integers(0, len(ts) - 1, 400)]
```

### Step 6: repr(ts2).splitlines()[-1]

```python
repr(ts2).splitlines()[-1]
```


## Complete Example

```python
# Workflow
index = Index([datetime(2000, 1, 1) + timedelta(i) for i in range(1000)], dtype=object)
ts = Series(np.random.default_rng(2).standard_normal(len(index)), index)
repr(ts)
ts = Series(np.arange(20, dtype=np.float64), index=date_range('2020-01-01', periods=20))
assert repr(ts).splitlines()[-1].startswith('Freq:')
ts2 = ts.iloc[np.random.default_rng(2).integers(0, len(ts) - 1, 400)]
repr(ts2).splitlines()[-1]
```

## Next Steps


---

*Source: test_formats.py:214 | Complexity: Intermediate | Last updated: 2026-06-02*