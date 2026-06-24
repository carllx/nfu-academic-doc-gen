# How To: Constructor Positional Keyword Mixed With Tzinfo

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor positional keyword mixed with tzinfo

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `zoneinfo`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat`
- `pandas.errors`
- `pandas`

**Setup Required:**
```python
# Fixtures: kwd, request
```

## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {kwd: 4}
```

**Verification:**
```python
assert ts == expected
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(2020, 12, 31, tzinfo=timezone.utc, **kwargs)
```

### Step 3: Assign td_kwargs = value

```python
td_kwargs = {kwd + 's': 4}
```

### Step 4: Assign td = Timedelta(...)

```python
td = Timedelta(**td_kwargs)
```

### Step 5: Assign expected = value

```python
expected = Timestamp('2020-12-31', tz=timezone.utc) + td
```

**Verification:**
```python
assert ts == expected
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='GH#45307')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: kwd, request

# Workflow
if kwd != 'nanosecond':
    mark = pytest.mark.xfail(reason='GH#45307')
    request.applymarker(mark)
kwargs = {kwd: 4}
ts = Timestamp(2020, 12, 31, tzinfo=timezone.utc, **kwargs)
td_kwargs = {kwd + 's': 4}
td = Timedelta(**td_kwargs)
expected = Timestamp('2020-12-31', tz=timezone.utc) + td
assert ts == expected
```

## Next Steps


---

*Source: test_constructors.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*