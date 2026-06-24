# How To: Categorical Dtype Single

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical dtype single

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, dtype, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c\n1,a,3.4\n1,a,3.4\n2,b,4.5'

```python
data = 'a,b,c\n1,a,3.4\n1,a,3.4\n2,b,4.5'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 1, 2], 'b': Categorical(['a', 'a', 'b']), 'c': [3.4, 3.4, 4.5]})
```

### Step 4: Assign actual = parser.read_csv(...)

```python
actual = parser.read_csv(StringIO(data), dtype=dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(strict=False, reason='Flaky test sometimes gives object dtype instead of Categorical')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, dtype, request

# Workflow
parser = all_parsers
data = 'a,b,c\n1,a,3.4\n1,a,3.4\n2,b,4.5'
expected = DataFrame({'a': [1, 1, 2], 'b': Categorical(['a', 'a', 'b']), 'c': [3.4, 3.4, 4.5]})
if parser.engine == 'pyarrow':
    mark = pytest.mark.xfail(strict=False, reason='Flaky test sometimes gives object dtype instead of Categorical')
    request.applymarker(mark)
actual = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_categorical.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*