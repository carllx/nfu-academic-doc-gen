# How To: Concatlike Common Period Mixed Dt To Object

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concatlike common period mixed dt to object

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi1 = pd.PeriodIndex(...)

```python
pi1 = pd.PeriodIndex(['2011-01', '2011-02'], freq='M')
```

### Step 2: Assign tdi = pd.TimedeltaIndex(...)

```python
tdi = pd.TimedeltaIndex(['1 days', '2 days'])
```

### Step 3: Assign exp = Index(...)

```python
exp = Index([pd.Period('2011-01', freq='M'), pd.Period('2011-02', freq='M'), pd.Timedelta('1 days'), pd.Timedelta('2 days')], dtype=object)
```

### Step 4: Assign res = pi1.append(...)

```python
res = pi1.append(tdi)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 6: Assign ps1 = Series(...)

```python
ps1 = Series(pi1)
```

### Step 7: Assign tds = Series(...)

```python
tds = Series(tdi)
```

### Step 8: Assign res = ps1._append(...)

```python
res = ps1._append(tds)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 10: Assign res = pd.concat(...)

```python
res = pd.concat([ps1, tds])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 12: Assign exp = Index(...)

```python
exp = Index([pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Period('2011-01', freq='M'), pd.Period('2011-02', freq='M')], dtype=object)
```

### Step 13: Assign res = tdi.append(...)

```python
res = tdi.append(pi1)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 15: Assign ps1 = Series(...)

```python
ps1 = Series(pi1)
```

### Step 16: Assign tds = Series(...)

```python
tds = Series(tdi)
```

### Step 17: Assign res = tds._append(...)

```python
res = tds._append(ps1)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

### Step 19: Assign res = pd.concat(...)

```python
res = pd.concat([tds, ps1])
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```


## Complete Example

```python
# Workflow
pi1 = pd.PeriodIndex(['2011-01', '2011-02'], freq='M')
tdi = pd.TimedeltaIndex(['1 days', '2 days'])
exp = Index([pd.Period('2011-01', freq='M'), pd.Period('2011-02', freq='M'), pd.Timedelta('1 days'), pd.Timedelta('2 days')], dtype=object)
res = pi1.append(tdi)
tm.assert_index_equal(res, exp)
ps1 = Series(pi1)
tds = Series(tdi)
res = ps1._append(tds)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([ps1, tds])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
exp = Index([pd.Timedelta('1 days'), pd.Timedelta('2 days'), pd.Period('2011-01', freq='M'), pd.Period('2011-02', freq='M')], dtype=object)
res = tdi.append(pi1)
tm.assert_index_equal(res, exp)
ps1 = Series(pi1)
tds = Series(tdi)
res = tds._append(ps1)
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
res = pd.concat([tds, ps1])
tm.assert_series_equal(res, Series(exp, index=[0, 1, 0, 1]))
```

## Next Steps


---

*Source: test_append_common.py:423 | Complexity: Advanced | Last updated: 2026-06-02*