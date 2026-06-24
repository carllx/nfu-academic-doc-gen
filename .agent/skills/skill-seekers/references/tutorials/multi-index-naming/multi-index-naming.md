# How To: Multi Index Naming

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multi index naming

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, index_names, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = unknown.join(...)

```python
data = ','.join(index_names + ['col\na,c,1\na,d,2\nb,c,3\nb,d,4'])
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=[0, 1])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col': [1, 2, 3, 4]}, index=MultiIndex.from_product([['a', 'b'], ['c', 'd']]))
```

### Step 5: Assign expected.index.names = value

```python
expected.index.names = [name if name else None for name in index_names]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='One case raises, others are wrong')
```

### Step 8: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, index_names, request

# Workflow
parser = all_parsers
if parser.engine == 'pyarrow' and '' in index_names:
    mark = pytest.mark.xfail(reason='One case raises, others are wrong')
    request.applymarker(mark)
data = ','.join(index_names + ['col\na,c,1\na,d,2\nb,c,3\nb,d,4'])
result = parser.read_csv(StringIO(data), index_col=[0, 1])
expected = DataFrame({'col': [1, 2, 3, 4]}, index=MultiIndex.from_product([['a', 'b'], ['c', 'd']]))
expected.index.names = [name if name else None for name in index_names]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index_col.py:168 | Complexity: Advanced | Last updated: 2026-06-02*