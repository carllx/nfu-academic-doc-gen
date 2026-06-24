# How To: Deep Skip Rows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test deep skip rows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
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

### Step 2: Assign data = value

```python
data = 'a,b,c\n' + '\n'.join([','.join([str(i), str(i + 1), str(i + 2)]) for i in range(10)])
```

### Step 3: Assign condensed_data = value

```python
condensed_data = 'a,b,c\n' + '\n'.join([','.join([str(i), str(i + 1), str(i + 2)]) for i in [0, 1, 2, 3, 4, 6, 8, 9]])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), skiprows=[6, 8])
```

### Step 5: Assign condensed_result = parser.read_csv(...)

```python
condensed_result = parser.read_csv(StringIO(condensed_data))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, condensed_result)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b,c\n' + '\n'.join([','.join([str(i), str(i + 1), str(i + 2)]) for i in range(10)])
condensed_data = 'a,b,c\n' + '\n'.join([','.join([str(i), str(i + 1), str(i + 2)]) for i in [0, 1, 2, 3, 4, 6, 8, 9]])
result = parser.read_csv(StringIO(data), skiprows=[6, 8])
condensed_result = parser.read_csv(StringIO(condensed_data))
tm.assert_frame_equal(result, condensed_result)
```

## Next Steps


---

*Source: test_skiprows.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*