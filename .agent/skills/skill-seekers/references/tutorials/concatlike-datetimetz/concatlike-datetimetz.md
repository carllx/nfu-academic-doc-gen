# How To: Concatlike Datetimetz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concatlike datetimetz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign dti1 = pd.DatetimeIndex(...)

```python
dti1 = pd.DatetimeIndex(['2011-01-01', '2011-01-02'], tz=tz)
```

### Step 3: Assign dti2 = pd.DatetimeIndex(...)

```python
dti2 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'], tz=tz)
```

### Step 4: Assign exp = pd.DatetimeIndex(...)

```python
exp = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2012-01-01', '2012-01-02'], tz=tz)
```

### Step 5: Assign res = dti1.append(...)

```python
res = dti1.append(dti2)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 7: Assign dts1 = Series(...)

```python
dts1 = Series(dti1)
```

### Step 8: Assign dts2 = Series(...)

```python
dts2 = Series(dti2)
```

### Step 9: Assign res = dts1._append(...)

```python
res = dts1._append(dts2)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 11: Assign res = pd.concat(...)

```python
res = pd.concat([dts1, dts2])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
dti1 = pd.DatetimeIndex(['2011-01-01', '2011-01-02'], tz=tz)
dti2 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'], tz=tz)
exp = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2012-01-01', '2012-01-02'], tz=tz)
res = dti1.append(dti2)
tm.assert_index_equal(res, exp)
dts1 = Series(dti1)
dts2 = Series(dti2)
res = dts1._append(dts2)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([dts1, dts2])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

## Next Steps


---

*Source: test_append_common.py:288 | Complexity: Advanced | Last updated: 2026-06-02*