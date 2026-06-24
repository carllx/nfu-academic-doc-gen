# How To: To Dict

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to dict

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

### Step 1: Assign d = value

```python
d = {'key': 31337}
```

**Verification:**
```python
assert dec == d
```

### Step 2: Assign o = DictTest(...)

```python
o = DictTest()
```

### Step 3: Assign output = ujson.ujson_dumps(...)

```python
output = ujson.ujson_dumps(o)
```

### Step 4: Assign dec = ujson.ujson_loads(...)

```python
dec = ujson.ujson_loads(output)
```

**Verification:**
```python
assert dec == d
```


## Complete Example

```python
# Workflow
d = {'key': 31337}

class DictTest:

    def toDict(self):
        return d
o = DictTest()
output = ujson.ujson_dumps(o)
dec = ujson.ujson_loads(output)
assert dec == d
```

## Next Steps


---

*Source: test_ujson.py:615 | Complexity: Intermediate | Last updated: 2026-06-02*