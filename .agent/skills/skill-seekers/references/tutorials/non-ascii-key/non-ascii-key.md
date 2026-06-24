# How To: Non Ascii Key

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non ascii key

## Prerequisites

**Required Modules:**
- `json`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.json._normalize`


## Step-by-Step Guide

### Step 1: Assign testjson = unknown.decode(...)

```python
testjson = b'[{"\xc3\x9cnic\xc3\xb8de":0,"sub":{"A":1, "B":2}},{"\xc3\x9cnic\xc3\xb8de":1,"sub":{"A":3, "B":4}}]'.decode('utf8')
```

### Step 2: Assign testdata = value

```python
testdata = {b'\xc3\x9cnic\xc3\xb8de'.decode('utf8'): [0, 1], 'sub.A': [1, 3], 'sub.B': [2, 4]}
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(testdata)
```

### Step 4: Assign result = json_normalize(...)

```python
result = json_normalize(json.loads(testjson))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
testjson = b'[{"\xc3\x9cnic\xc3\xb8de":0,"sub":{"A":1, "B":2}},{"\xc3\x9cnic\xc3\xb8de":1,"sub":{"A":3, "B":4}}]'.decode('utf8')
testdata = {b'\xc3\x9cnic\xc3\xb8de'.decode('utf8'): [0, 1], 'sub.A': [1, 3], 'sub.B': [2, 4]}
expected = DataFrame(testdata)
result = json_normalize(json.loads(testjson))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_normalize.py:411 | Complexity: Intermediate | Last updated: 2026-06-02*