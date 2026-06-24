# How To: Concatlike Datetimetz To Object

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concatlike datetimetz to object

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
dti2 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'])
```

### Step 4: Assign exp = Index(...)

```python
exp = Index([pd.Timestamp('2011-01-01', tz=tz), pd.Timestamp('2011-01-02', tz=tz), pd.Timestamp('2012-01-01'), pd.Timestamp('2012-01-02')], dtype=object)
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

### Step 13: Assign dti3 = pd.DatetimeIndex(...)

```python
dti3 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'], tz='US/Pacific')
```

### Step 14: Assign exp = Index(...)

```python
exp = Index([pd.Timestamp('2011-01-01', tz=tz), pd.Timestamp('2011-01-02', tz=tz), pd.Timestamp('2012-01-01', tz='US/Pacific'), pd.Timestamp('2012-01-02', tz='US/Pacific')], dtype=object)
```

### Step 15: Assign res = dti1.append(...)

```python
res = dti1.append(dti3)
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 17: Assign dts1 = Series(...)

```python
dts1 = Series(dti1)
```

### Step 18: Assign dts3 = Series(...)

```python
dts3 = Series(dti3)
```

### Step 19: Assign res = dts1._append(...)

```python
res = dts1._append(dts3)
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 21: Assign res = pd.concat(...)

```python
res = pd.concat([dts1, dts3])
```

### Step 22: Call tm.assert_series_equal()

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
dti2 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'])
exp = Index([pd.Timestamp('2011-01-01', tz=tz), pd.Timestamp('2011-01-02', tz=tz), pd.Timestamp('2012-01-01'), pd.Timestamp('2012-01-02')], dtype=object)
res = dti1.append(dti2)
tm.assert_index_equal(res, exp)
dts1 = Series(dti1)
dts2 = Series(dti2)
res = dts1._append(dts2)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([dts1, dts2])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
dti3 = pd.DatetimeIndex(['2012-01-01', '2012-01-02'], tz='US/Pacific')
exp = Index([pd.Timestamp('2011-01-01', tz=tz), pd.Timestamp('2011-01-02', tz=tz), pd.Timestamp('2012-01-01', tz='US/Pacific'), pd.Timestamp('2012-01-02', tz='US/Pacific')], dtype=object)
res = dti1.append(dti3)
tm.assert_index_equal(res, exp)
dts1 = Series(dti1)
dts3 = Series(dti3)
res = dts1._append(dts3)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([dts1, dts3])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

## Next Steps


---

*Source: test_append_common.py:326 | Complexity: Advanced | Last updated: 2026-06-02*