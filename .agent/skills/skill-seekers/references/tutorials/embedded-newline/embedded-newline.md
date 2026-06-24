# How To: Embedded Newline

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test embedded newline

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas._libs.parsers`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`


## Step-by-Step Guide

### Step 1: Assign data = 'a\n"hello\nthere"\nthis'

```python
data = 'a\n"hello\nthere"\nthis'
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), header=None)
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array(['a', 'hello\nthere', 'this'], dtype=np.object_)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[0], expected)
```


## Complete Example

```python
# Workflow
data = 'a\n"hello\nthere"\nthis'
reader = TextReader(StringIO(data), header=None)
result = reader.read()
expected = np.array(['a', 'hello\nthere', 'this'], dtype=np.object_)
tm.assert_numpy_array_equal(result[0], expected)
```

## Next Steps


---

*Source: test_textreader.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*