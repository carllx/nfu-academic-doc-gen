# How To: Buffer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test buffer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `math`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: df_from_dict
```

## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = [0, 1, -1]
```

**Verification:**
```python
assert dataBuf.bufsize > 0
```

### Step 2: Assign df = df_from_dict(...)

```python
df = df_from_dict({'a': arr})
```

**Verification:**
```python
assert dataBuf.ptr != 0
```

### Step 3: Assign dfX = df.__dataframe__(...)

```python
dfX = df.__dataframe__()
```

**Verification:**
```python
assert dataDtype[0] == 0
```

### Step 4: Assign colX = dfX.get_column(...)

```python
colX = dfX.get_column(0)
```

**Verification:**
```python
assert val == truth, f'Buffer at index {idx} mismatch'
```

### Step 5: Assign bufX = colX.get_buffers(...)

```python
bufX = colX.get_buffers()
```

### Step 6: Assign unknown = value

```python
dataBuf, dataDtype = bufX['data']
```

**Verification:**
```python
assert dataBuf.bufsize > 0
```

### Step 7: Assign unknown = dataBuf.__dlpack_device__(...)

```python
device, _ = dataBuf.__dlpack_device__()
```

**Verification:**
```python
assert dataDtype[0] == 0
```

### Step 8: Assign bitwidth = value

```python
bitwidth = dataDtype[1]
```

### Step 9: Assign ctype = value

```python
ctype = {8: ctypes.c_int8, 16: ctypes.c_int16, 32: ctypes.c_int32, 64: ctypes.c_int64}[bitwidth]
```

### Step 10: Assign val = value

```python
val = ctype.from_address(dataBuf.ptr + idx * (bitwidth // 8)).value
```

**Verification:**
```python
assert val == truth, f'Buffer at index {idx} mismatch'
```


## Complete Example

```python
# Setup
# Fixtures: df_from_dict

# Workflow
arr = [0, 1, -1]
df = df_from_dict({'a': arr})
dfX = df.__dataframe__()
colX = dfX.get_column(0)
bufX = colX.get_buffers()
dataBuf, dataDtype = bufX['data']
assert dataBuf.bufsize > 0
assert dataBuf.ptr != 0
device, _ = dataBuf.__dlpack_device__()
assert dataDtype[0] == 0
if device == 1:
    bitwidth = dataDtype[1]
    ctype = {8: ctypes.c_int8, 16: ctypes.c_int16, 32: ctypes.c_int32, 64: ctypes.c_int64}[bitwidth]
    for idx, truth in enumerate(arr):
        val = ctype.from_address(dataBuf.ptr + idx * (bitwidth // 8)).value
        assert val == truth, f'Buffer at index {idx} mismatch'
```

## Next Steps


---

*Source: test_spec_conformance.py:147 | Complexity: Advanced | Last updated: 2026-06-02*