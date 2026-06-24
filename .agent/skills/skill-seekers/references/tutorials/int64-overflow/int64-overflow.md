# How To: Int64 Overflow

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int64 overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, conv, request
```

## Step-by-Step Guide

### Step 1: Assign data = 'ID\n00013007854817840016671868\n00013007854817840016749251\n00013007854817840016754630\n00013007854817840016781876\n00013007854817840017028824\n00013007854817840017963235\n00013007854817840018860166'

```python
data = 'ID\n00013007854817840016671868\n00013007854817840016749251\n00013007854817840016754630\n00013007854817840016781876\n00013007854817840017028824\n00013007854817840017963235\n00013007854817840018860166'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(['00013007854817840016671868', '00013007854817840016749251', '00013007854817840016754630', '00013007854817840016781876', '00013007854817840017028824', '00013007854817840017963235', '00013007854817840018860166'], columns=['ID'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = unknown.join(...)

```python
msg = '|'.join(['Python int too large to convert to C long', 'long too big to convert', 'int too big to convert'])
```

### Step 7: Assign err = OverflowError

```python
err = OverflowError
```

### Step 8: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='parses to float64')
```

### Step 9: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 10: Assign err = ValueError

```python
err = ValueError
```

### Step 11: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 12: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), converters={'ID': conv})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, conv, request

# Workflow
data = 'ID\n00013007854817840016671868\n00013007854817840016749251\n00013007854817840016754630\n00013007854817840016781876\n00013007854817840017028824\n00013007854817840017963235\n00013007854817840018860166'
parser = all_parsers
if conv is None:
    if parser.engine == 'pyarrow':
        mark = pytest.mark.xfail(reason='parses to float64')
        request.applymarker(mark)
    result = parser.read_csv(StringIO(data))
    expected = DataFrame(['00013007854817840016671868', '00013007854817840016749251', '00013007854817840016754630', '00013007854817840016781876', '00013007854817840017028824', '00013007854817840017963235', '00013007854817840018860166'], columns=['ID'])
    tm.assert_frame_equal(result, expected)
else:
    msg = '|'.join(['Python int too large to convert to C long', 'long too big to convert', 'int too big to convert'])
    err = OverflowError
    if parser.engine == 'pyarrow':
        err = ValueError
        msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(err, match=msg):
        parser.read_csv(StringIO(data), converters={'ID': conv})
```

## Next Steps


---

*Source: test_ints.py:131 | Complexity: Advanced | Last updated: 2026-06-02*