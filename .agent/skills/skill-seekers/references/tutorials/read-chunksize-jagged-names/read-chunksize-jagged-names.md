# How To: Read Chunksize Jagged Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read chunksize jagged names

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = unknown.join(...)

```python
data = '\n'.join(['0'] * 7 + [','.join(['0'] * 10)])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0] + [np.nan] * 9] * 7 + [[0] * 10])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 6: Assign result = concat(...)

```python
result = concat(reader)
```

### Step 7: Call concat()

```python
concat(reader)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '\n'.join(['0'] * 7 + [','.join(['0'] * 10)])
expected = DataFrame([[0] + [np.nan] * 9] * 7 + [[0] * 10])
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with parser.read_csv(StringIO(data), names=range(10), chunksize=4) as reader:
            concat(reader)
    return
with parser.read_csv(StringIO(data), names=range(10), chunksize=4) as reader:
    result = concat(reader)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_chunksize.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*