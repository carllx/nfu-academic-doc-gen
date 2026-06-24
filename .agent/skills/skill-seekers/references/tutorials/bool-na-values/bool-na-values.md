# How To: Bool Na Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bool na values

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A,B,C\nTrue,False,True\nNA,True,False\nFalse,NA,True'

```python
data = 'A,B,C\nTrue,False,True\nNA,True,False\nFalse,NA,True'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': np.array([True, np.nan, False], dtype=object), 'B': np.array([False, True, np.nan], dtype=object), 'C': [True, False, True]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign unknown = None

```python
expected.loc[1, 'A'] = None
```

### Step 7: Assign unknown = None

```python
expected.loc[2, 'B'] = None
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'A,B,C\nTrue,False,True\nNA,True,False\nFalse,NA,True'
parser = all_parsers
result = parser.read_csv(StringIO(data))
expected = DataFrame({'A': np.array([True, np.nan, False], dtype=object), 'B': np.array([False, True, np.nan], dtype=object), 'C': [True, False, True]})
if parser.engine == 'pyarrow':
    expected.loc[1, 'A'] = None
    expected.loc[2, 'B'] = None
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*