# How To: Dtype Per Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dtype per column

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'one,two\n1,2.5\n2,3.5\n3,4.5\n4,5.5'

```python
data = 'one,two\n1,2.5\n2,3.5\n3,4.5\n4,5.5'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, '2.5'], [2, '3.5'], [3, '4.5'], [4, '5.5']], columns=['one', 'two'])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
expected['one'] = expected['one'].astype(np.float64)
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype={'one': np.float64, 1: str})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'one,two\n1,2.5\n2,3.5\n3,4.5\n4,5.5'
expected = DataFrame([[1, '2.5'], [2, '3.5'], [3, '4.5'], [4, '5.5']], columns=['one', 'two'])
expected['one'] = expected['one'].astype(np.float64)
result = parser.read_csv(StringIO(data), dtype={'one': np.float64, 1: str})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes_basic.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*