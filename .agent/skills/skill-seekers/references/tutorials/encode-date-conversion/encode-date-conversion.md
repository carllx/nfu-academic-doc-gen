# How To: Encode Date Conversion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test encode date conversion

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `decimal`
- `json`
- `locale`
- `math`
- `re`
- `time`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.json`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign date_input = datetime.date.fromtimestamp(...)

```python
date_input = datetime.date.fromtimestamp(time.time())
```

**Verification:**
```python
assert int(expected) == json.loads(output)
```

### Step 2: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(date_input, date_unit='s')
```

**Verification:**
```python
assert int(expected) == ujson.ujson_loads(output)
```

### Step 3: Assign tup = value

```python
tup = (date_input.year, date_input.month, date_input.day, 0, 0, 0)
```

### Step 4: Assign expected = calendar.timegm(...)

```python
expected = calendar.timegm(tup)
```

**Verification:**
```python
assert int(expected) == json.loads(output)
```


## Complete Example

```python
# Workflow
date_input = datetime.date.fromtimestamp(time.time())
output = ujson.ujson_dumps(date_input, date_unit='s')
tup = (date_input.year, date_input.month, date_input.day, 0, 0, 0)
expected = calendar.timegm(tup)
assert int(expected) == json.loads(output)
assert int(expected) == ujson.ujson_loads(output)
```

## Next Steps


---

*Source: test_ujson.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*