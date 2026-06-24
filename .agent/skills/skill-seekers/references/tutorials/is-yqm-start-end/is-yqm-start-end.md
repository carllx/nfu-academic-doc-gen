# How To: Is Yqm Start End

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is yqm start end

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign freq_m = to_offset(...)

```python
freq_m = to_offset('ME')
```

**Verification:**
```python
assert ts == value
```

### Step 2: Assign bm = to_offset(...)

```python
bm = to_offset('BME')
```

### Step 3: Assign qfeb = to_offset(...)

```python
qfeb = to_offset('QE-FEB')
```

### Step 4: Assign qsfeb = to_offset(...)

```python
qsfeb = to_offset('QS-FEB')
```

### Step 5: Assign bq = to_offset(...)

```python
bq = to_offset('BQE')
```

### Step 6: Assign bqs_apr = to_offset(...)

```python
bqs_apr = to_offset('BQS-APR')
```

### Step 7: Assign as_nov = to_offset(...)

```python
as_nov = to_offset('YS-NOV')
```

### Step 8: Assign tests = value

```python
tests = [(freq_m.is_month_start(Timestamp('2013-06-01')), 1), (bm.is_month_start(Timestamp('2013-06-01')), 0), (freq_m.is_month_start(Timestamp('2013-06-03')), 0), (bm.is_month_start(Timestamp('2013-06-03')), 1), (qfeb.is_month_end(Timestamp('2013-02-28')), 1), (qfeb.is_quarter_end(Timestamp('2013-02-28')), 1), (qfeb.is_year_end(Timestamp('2013-02-28')), 1), (qfeb.is_month_start(Timestamp('2013-03-01')), 1), (qfeb.is_quarter_start(Timestamp('2013-03-01')), 1), (qfeb.is_year_start(Timestamp('2013-03-01')), 1), (qsfeb.is_month_end(Timestamp('2013-03-31')), 1), (qsfeb.is_quarter_end(Timestamp('2013-03-31')), 0), (qsfeb.is_year_end(Timestamp('2013-03-31')), 0), (qsfeb.is_month_start(Timestamp('2013-02-01')), 1), (qsfeb.is_quarter_start(Timestamp('2013-02-01')), 1), (qsfeb.is_year_start(Timestamp('2013-02-01')), 1), (bq.is_month_end(Timestamp('2013-06-30')), 0), (bq.is_quarter_end(Timestamp('2013-06-30')), 0), (bq.is_year_end(Timestamp('2013-06-30')), 0), (bq.is_month_end(Timestamp('2013-06-28')), 1), (bq.is_quarter_end(Timestamp('2013-06-28')), 1), (bq.is_year_end(Timestamp('2013-06-28')), 0), (bqs_apr.is_month_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_quarter_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_year_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_month_end(Timestamp('2013-06-28')), 1), (bqs_apr.is_quarter_end(Timestamp('2013-06-28')), 1), (bqs_apr.is_year_end(Timestamp('2013-03-29')), 1), (as_nov.is_year_start(Timestamp('2013-11-01')), 1), (as_nov.is_year_end(Timestamp('2013-10-31')), 1), (Timestamp('2012-02-01').days_in_month, 29), (Timestamp('2013-02-01').days_in_month, 28)]
```

**Verification:**
```python
assert ts == value
```


## Complete Example

```python
# Workflow
freq_m = to_offset('ME')
bm = to_offset('BME')
qfeb = to_offset('QE-FEB')
qsfeb = to_offset('QS-FEB')
bq = to_offset('BQE')
bqs_apr = to_offset('BQS-APR')
as_nov = to_offset('YS-NOV')
tests = [(freq_m.is_month_start(Timestamp('2013-06-01')), 1), (bm.is_month_start(Timestamp('2013-06-01')), 0), (freq_m.is_month_start(Timestamp('2013-06-03')), 0), (bm.is_month_start(Timestamp('2013-06-03')), 1), (qfeb.is_month_end(Timestamp('2013-02-28')), 1), (qfeb.is_quarter_end(Timestamp('2013-02-28')), 1), (qfeb.is_year_end(Timestamp('2013-02-28')), 1), (qfeb.is_month_start(Timestamp('2013-03-01')), 1), (qfeb.is_quarter_start(Timestamp('2013-03-01')), 1), (qfeb.is_year_start(Timestamp('2013-03-01')), 1), (qsfeb.is_month_end(Timestamp('2013-03-31')), 1), (qsfeb.is_quarter_end(Timestamp('2013-03-31')), 0), (qsfeb.is_year_end(Timestamp('2013-03-31')), 0), (qsfeb.is_month_start(Timestamp('2013-02-01')), 1), (qsfeb.is_quarter_start(Timestamp('2013-02-01')), 1), (qsfeb.is_year_start(Timestamp('2013-02-01')), 1), (bq.is_month_end(Timestamp('2013-06-30')), 0), (bq.is_quarter_end(Timestamp('2013-06-30')), 0), (bq.is_year_end(Timestamp('2013-06-30')), 0), (bq.is_month_end(Timestamp('2013-06-28')), 1), (bq.is_quarter_end(Timestamp('2013-06-28')), 1), (bq.is_year_end(Timestamp('2013-06-28')), 0), (bqs_apr.is_month_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_quarter_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_year_end(Timestamp('2013-06-30')), 0), (bqs_apr.is_month_end(Timestamp('2013-06-28')), 1), (bqs_apr.is_quarter_end(Timestamp('2013-06-28')), 1), (bqs_apr.is_year_end(Timestamp('2013-03-29')), 1), (as_nov.is_year_start(Timestamp('2013-11-01')), 1), (as_nov.is_year_end(Timestamp('2013-10-31')), 1), (Timestamp('2012-02-01').days_in_month, 29), (Timestamp('2013-02-01').days_in_month, 28)]
for ts, value in tests:
    assert ts == value
```

## Next Steps


---

*Source: test_offsets.py:1140 | Complexity: Advanced | Last updated: 2026-06-02*