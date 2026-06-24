# How To: Empty With Nrows Chunksize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test empty with nrows chunksize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, iterator
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['foo', 'bar'])
```

### Step 3: Assign nrows = 10

```python
nrows = 10
```

### Step 4: Assign data = StringIO(...)

```python
data = StringIO('foo,bar\n')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The '(nrows|chunksize)' option is not supported with the 'pyarrow' engine"

```python
msg = "The '(nrows|chunksize)' option is not supported with the 'pyarrow' engine"
```

### Step 7: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(data, nrows=nrows)
```

### Step 8: Assign result = next(...)

```python
result = next(iter(reader))
```

### Step 9: Call parser.read_csv()

```python
parser.read_csv(data, nrows=nrows)
```

### Step 10: Call next()

```python
next(iter(reader))
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, iterator

# Workflow
parser = all_parsers
expected = DataFrame(columns=['foo', 'bar'])
nrows = 10
data = StringIO('foo,bar\n')
if parser.engine == 'pyarrow':
    msg = "The '(nrows|chunksize)' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        if iterator:
            with parser.read_csv(data, chunksize=nrows) as reader:
                next(iter(reader))
        else:
            parser.read_csv(data, nrows=nrows)
    return
if iterator:
    with parser.read_csv(data, chunksize=nrows) as reader:
        result = next(iter(reader))
else:
    result = parser.read_csv(data, nrows=nrows)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_chunksize.py:268 | Complexity: Advanced | Last updated: 2026-06-02*