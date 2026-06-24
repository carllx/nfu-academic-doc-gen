# How To: Fwf For Uint8

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fwf for uint8

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.parsers`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign data = '1421302965.213420    PRI=3 PGN=0xef00      DST=0x17 SRC=0x28    04 154 00 00 00 00 00 127\n1421302964.226776    PRI=6 PGN=0xf002               SRC=0x47    243 00 00 255 247 00 00 71'

```python
data = '1421302965.213420    PRI=3 PGN=0xef00      DST=0x17 SRC=0x28    04 154 00 00 00 00 00 127\n1421302964.226776    PRI=6 PGN=0xf002               SRC=0x47    243 00 00 255 247 00 00 71'
```

### Step 2: Assign df = read_fwf(...)

```python
df = read_fwf(StringIO(data), colspecs=[(0, 17), (25, 26), (33, 37), (49, 51), (58, 62), (63, 1000)], names=['time', 'pri', 'pgn', 'dst', 'src', 'data'], converters={'pgn': lambda x: int(x, 16), 'src': lambda x: int(x, 16), 'dst': lambda x: int(x, 16), 'data': lambda x: len(x.split(' '))})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1421302965.21342, 3, 61184, 23, 40, 8], [1421302964.226776, 6, 61442, None, 71, 8]], columns=['time', 'pri', 'pgn', 'dst', 'src', 'data'])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected['dst'] = expected['dst'].astype(object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
data = '1421302965.213420    PRI=3 PGN=0xef00      DST=0x17 SRC=0x28    04 154 00 00 00 00 00 127\n1421302964.226776    PRI=6 PGN=0xf002               SRC=0x47    243 00 00 255 247 00 00 71'
df = read_fwf(StringIO(data), colspecs=[(0, 17), (25, 26), (33, 37), (49, 51), (58, 62), (63, 1000)], names=['time', 'pri', 'pgn', 'dst', 'src', 'data'], converters={'pgn': lambda x: int(x, 16), 'src': lambda x: int(x, 16), 'dst': lambda x: int(x, 16), 'data': lambda x: len(x.split(' '))})
expected = DataFrame([[1421302965.21342, 3, 61184, 23, 40, 8], [1421302964.226776, 6, 61442, None, 71, 8]], columns=['time', 'pri', 'pgn', 'dst', 'src', 'data'])
expected['dst'] = expected['dst'].astype(object)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:326 | Complexity: Intermediate | Last updated: 2026-06-02*