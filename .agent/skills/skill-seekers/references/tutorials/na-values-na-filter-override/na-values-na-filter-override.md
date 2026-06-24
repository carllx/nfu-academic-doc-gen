# How To: Na Values Na Filter Override

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test na values na filter override

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: request, all_parsers, na_filter, row_data, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B\n1,A\nnan,B\n3,C\n'

```python
data = 'A,B\n1,A\nnan,B\n3,C\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), na_values=['B'], na_filter=na_filter)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(row_data, columns=['A', 'B'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason="pyarrow doesn't support this.")
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: request, all_parsers, na_filter, row_data, using_infer_string

# Workflow
parser = all_parsers
if parser.engine == 'pyarrow':
    if not (using_infer_string and na_filter):
        mark = pytest.mark.xfail(reason="pyarrow doesn't support this.")
        request.applymarker(mark)
data = 'A,B\n1,A\nnan,B\n3,C\n'
result = parser.read_csv(StringIO(data), na_values=['B'], na_filter=na_filter)
expected = DataFrame(row_data, columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:445 | Complexity: Intermediate | Last updated: 2026-06-02*