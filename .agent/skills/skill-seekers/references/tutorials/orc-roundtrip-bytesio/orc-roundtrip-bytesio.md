# How To: Orc Roundtrip Bytesio

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc roundtrip bytesio

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pyarrow`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign data = value

```python
data = {'boolean1': np.array([False, True], dtype='bool'), 'byte1': np.array([1, 100], dtype='int8'), 'short1': np.array([1024, 2048], dtype='int16'), 'int1': np.array([65536, 65536], dtype='int32'), 'long1': np.array([9223372036854775807, 9223372036854775807], dtype='int64'), 'float1': np.array([1.0, 2.0], dtype='float32'), 'double1': np.array([-15.0, -5.0], dtype='float64'), 'bytes1': np.array([b'\x00\x01\x02\x03\x04', b''], dtype='object'), 'string1': np.array(['hi', 'bye'], dtype='object')}
```

### Step 3: Assign expected = pd.DataFrame.from_dict(...)

```python
expected = pd.DataFrame.from_dict(data)
```

### Step 4: Assign bytes = expected.to_orc(...)

```python
bytes = expected.to_orc()
```

### Step 5: Assign got = read_orc(...)

```python
got = read_orc(BytesIO(bytes))
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(expected, got)
```


## Complete Example

```python
# Workflow
pytest.importorskip('pyarrow')
data = {'boolean1': np.array([False, True], dtype='bool'), 'byte1': np.array([1, 100], dtype='int8'), 'short1': np.array([1024, 2048], dtype='int16'), 'int1': np.array([65536, 65536], dtype='int32'), 'long1': np.array([9223372036854775807, 9223372036854775807], dtype='int64'), 'float1': np.array([1.0, 2.0], dtype='float32'), 'double1': np.array([-15.0, -5.0], dtype='float64'), 'bytes1': np.array([b'\x00\x01\x02\x03\x04', b''], dtype='object'), 'string1': np.array(['hi', 'bye'], dtype='object')}
expected = pd.DataFrame.from_dict(data)
bytes = expected.to_orc()
got = read_orc(BytesIO(bytes))
tm.assert_equal(expected, got)
```

## Next Steps


---

*Source: test_orc.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*