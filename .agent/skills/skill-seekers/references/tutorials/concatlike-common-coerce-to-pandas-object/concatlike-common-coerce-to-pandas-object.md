# How To: Concatlike Common Coerce To Pandas Object

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concatlike common coerce to pandas object

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = pd.DatetimeIndex(...)

```python
dti = pd.DatetimeIndex(['2011-01-01', '2011-01-02'])
```

**Verification:**
```python
assert isinstance(res[0], pd.Timestamp)
```

### Step 2: Assign tdi = pd.TimedeltaIndex(...)

```python
tdi = pd.TimedeltaIndex(['1 days', '2 days'])
```

**Verification:**
```python
assert isinstance(res[-1], pd.Timedelta)
```

### Step 3: Assign exp = Index(...)

```python
exp = Index([pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timedelta('1 days'), pd.Timedelta('2 days')])
```

**Verification:**
```python
assert isinstance(res.iloc[0], pd.Timestamp)
```

### Step 4: Assign res = dti.append(...)

```python
res = dti.append(tdi)
```

**Verification:**
```python
assert isinstance(res.iloc[-1], pd.Timedelta)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

**Verification:**
```python
assert isinstance(res.iloc[0], pd.Timestamp)
```

### Step 6: Assign dts = Series(...)

```python
dts = Series(dti)
```

**Verification:**
```python
assert isinstance(res.iloc[-1], pd.Timedelta)
```

### Step 7: Assign tds = Series(...)

```python
tds = Series(tdi)
```

### Step 8: Assign res = dts._append(...)

```python
res = dts._append(tds)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

**Verification:**
```python
assert isinstance(res.iloc[0], pd.Timestamp)
```

### Step 10: Assign res = pd.concat(...)

```python
res = pd.concat([dts, tds])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

**Verification:**
```python
assert isinstance(res.iloc[0], pd.Timestamp)
```


## Complete Example

```python
# Workflow
dti = pd.DatetimeIndex(['2011-01-01', '2011-01-02'])
tdi = pd.TimedeltaIndex(['1 days', '2 days'])
exp = Index([pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02'), pd.Timedelta('1 days'), pd.Timedelta('2 days')])
res = dti.append(tdi)
tm.assert_index_equal(res, exp)
assert isinstance(res[0], pd.Timestamp)
assert isinstance(res[-1], pd.Timedelta)
dts = Series(dti)
tds = Series(tdi)
res = dts._append(tds)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
assert isinstance(res.iloc[0], pd.Timestamp)
assert isinstance(res.iloc[-1], pd.Timedelta)
res = pd.concat([dts, tds])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
assert isinstance(res.iloc[0], pd.Timestamp)
assert isinstance(res.iloc[-1], pd.Timedelta)
```

## Next Steps


---

*Source: test_append_common.py:256 | Complexity: Advanced | Last updated: 2026-06-02*