# How To: Euro Decimal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test euro decimal

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

### Step 1: Assign data = '12345,67\n345,678'

```python
data = '12345,67\n345,678'
```

### Step 2: Assign reader = TextReader(...)

```python
reader = TextReader(StringIO(data), delimiter=':', decimal=',', header=None)
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([12345.67, 345.678])
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result[0], expected)
```


## Complete Example

```python
# Workflow
data = '12345,67\n345,678'
reader = TextReader(StringIO(data), delimiter=':', decimal=',', header=None)
result = reader.read()
expected = np.array([12345.67, 345.678])
tm.assert_almost_equal(result[0], expected)
```

## Next Steps


---

*Source: test_textreader.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*