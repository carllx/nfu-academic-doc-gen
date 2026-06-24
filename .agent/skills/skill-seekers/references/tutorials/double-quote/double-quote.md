# How To: Double Quote

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test double quote

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `csv`
- `io`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, doublequote, exp_data, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b\n3,"4 "" 5"'

```python
data = 'a,b\n3,"4 "" 5"'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), quotechar='"', doublequote=doublequote)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_data, columns=['a', 'b'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Mismatched result')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, doublequote, exp_data, request

# Workflow
parser = all_parsers
data = 'a,b\n3,"4 "" 5"'
if parser.engine == 'pyarrow' and (not doublequote):
    mark = pytest.mark.xfail(reason='Mismatched result')
    request.applymarker(mark)
result = parser.read_csv(StringIO(data), quotechar='"', doublequote=doublequote)
expected = DataFrame(exp_data, columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quoting.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*