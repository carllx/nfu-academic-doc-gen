# How To: Parsing Tzlocal Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parsing tzlocal deprecated

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.parser`
- `dateutil.tz`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.parsing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas._testing`
- `pandas._testing._hypothesis`


## Step-by-Step Guide

### Step 1: Assign msg = "Parsing 'EST' as tzlocal.*Pass the 'tz' keyword or call tz_localize after construction instead"

```python
msg = "Parsing 'EST' as tzlocal.*Pass the 'tz' keyword or call tz_localize after construction instead"
```

**Verification:**
```python
assert isinstance(res.tzinfo, tzlocal)
```

### Step 2: Assign dtstr = 'Jan 15 2004 03:00 EST'

```python
dtstr = 'Jan 15 2004 03:00 EST'
```

**Verification:**
```python
assert isinstance(res.tzinfo, tzlocal)
```

### Step 3: Assign unknown = parse_datetime_string_with_reso(...)

```python
res, _ = parse_datetime_string_with_reso(dtstr)
```

### Step 4: Assign res = parsing.py_parse_datetime_string(...)

```python
res = parsing.py_parse_datetime_string(dtstr)
```


## Complete Example

```python
# Workflow
msg = "Parsing 'EST' as tzlocal.*Pass the 'tz' keyword or call tz_localize after construction instead"
dtstr = 'Jan 15 2004 03:00 EST'
with tm.set_timezone('US/Eastern'):
    with tm.assert_produces_warning(FutureWarning, match=msg):
        res, _ = parse_datetime_string_with_reso(dtstr)
    assert isinstance(res.tzinfo, tzlocal)
    with tm.assert_produces_warning(FutureWarning, match=msg):
        res = parsing.py_parse_datetime_string(dtstr)
    assert isinstance(res.tzinfo, tzlocal)
```

## Next Steps


---

*Source: test_parsing.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*