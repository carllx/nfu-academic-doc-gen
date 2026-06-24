# How To: Converter Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converter multi index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,B\nX,Y,Z\n1,2,3'

```python
data = 'A,B,B\nX,Y,Z\n1,2,3'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=list(range(2)), converters={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({('A', 'X'): np.int32([1]), ('B', 'Y'): np.int32([2]), ('B', 'Z'): np.float32([3])})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=list(range(2)), converters={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'A,B,B\nX,Y,Z\n1,2,3'
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), header=list(range(2)), converters={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
    return
result = parser.read_csv(StringIO(data), header=list(range(2)), converters={('A', 'X'): np.int32, ('B', 'Y'): np.int32, ('B', 'Z'): np.float32})
expected = DataFrame({('A', 'X'): np.int32([1]), ('B', 'Y'): np.int32([2]), ('B', 'Z'): np.float32([3])})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_converters.py:226 | Complexity: Intermediate | Last updated: 2026-06-02*