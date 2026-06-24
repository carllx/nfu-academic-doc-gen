# How To: Encode Recursion Max

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test encode recursion max

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

### Step 1: Assign decoded_input = O1(...)

```python
decoded_input = O1()
```

### Step 2: Assign decoded_input.member = O2(...)

```python
decoded_input.member = O2()
```

### Step 3: Assign decoded_input.member.member = decoded_input

```python
decoded_input.member.member = decoded_input
```

### Step 4: Assign member = 0

```python
member = 0
```

### Step 5: Assign member = 0

```python
member = 0
```

### Step 6: Call ujson.ujson_dumps()

```python
ujson.ujson_dumps(decoded_input)
```


## Complete Example

```python
# Workflow
class O2:
    member = 0

class O1:
    member = 0
decoded_input = O1()
decoded_input.member = O2()
decoded_input.member.member = decoded_input
with pytest.raises(OverflowError, match='Maximum recursion level reached'):
    ujson.ujson_dumps(decoded_input)
```

## Next Steps


---

*Source: test_ujson.py:430 | Complexity: Intermediate | Last updated: 2026-06-02*