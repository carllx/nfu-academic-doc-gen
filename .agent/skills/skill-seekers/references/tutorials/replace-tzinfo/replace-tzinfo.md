# How To: Replace Tzinfo

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace tzinfo

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.util._test_decorators`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2016, 3, 27, 1)
```

**Verification:**
```python
assert result_dt.timestamp() == result_pd.timestamp()
```

### Step 2: Assign tzinfo = value

```python
tzinfo = pytz.timezone('CET').localize(dt, is_dst=False).tzinfo
```

**Verification:**
```python
assert result_dt == result_pd
```

### Step 3: Assign result_dt = dt.replace(...)

```python
result_dt = dt.replace(tzinfo=tzinfo)
```

**Verification:**
```python
assert result_dt == result_pd.to_pydatetime()
```

### Step 4: Assign result_pd = Timestamp.replace(...)

```python
result_pd = Timestamp(dt).replace(tzinfo=tzinfo)
```

**Verification:**
```python
assert result_dt.timestamp() == result_pd.timestamp()
```

### Step 5: Assign result_dt = dt.replace.replace(...)

```python
result_dt = dt.replace(tzinfo=tzinfo).replace(tzinfo=None)
```

**Verification:**
```python
assert result_dt == result_pd
```

### Step 6: Assign result_pd = Timestamp.replace.replace(...)

```python
result_pd = Timestamp(dt).replace(tzinfo=tzinfo).replace(tzinfo=None)
```

**Verification:**
```python
assert result_dt == result_pd.to_pydatetime()
```


## Complete Example

```python
# Workflow
dt = datetime(2016, 3, 27, 1)
tzinfo = pytz.timezone('CET').localize(dt, is_dst=False).tzinfo
result_dt = dt.replace(tzinfo=tzinfo)
result_pd = Timestamp(dt).replace(tzinfo=tzinfo)
with tm.set_timezone('UTC'):
    assert result_dt.timestamp() == result_pd.timestamp()
assert result_dt == result_pd
assert result_dt == result_pd.to_pydatetime()
result_dt = dt.replace(tzinfo=tzinfo).replace(tzinfo=None)
result_pd = Timestamp(dt).replace(tzinfo=tzinfo).replace(tzinfo=None)
with tm.set_timezone('UTC'):
    assert result_dt.timestamp() == result_pd.timestamp()
assert result_dt == result_pd
assert result_dt == result_pd.to_pydatetime()
```

## Next Steps


---

*Source: test_replace.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*