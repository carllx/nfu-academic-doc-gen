# How To: String Nas

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string nas

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C\na,b,c\nd,,f\n,g,h\n'

```python
data = 'A,B,C\na,b,c\nd,,f\n,g,h\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['a', 'b', 'c'], ['d', np.nan, 'f'], [np.nan, 'g', 'h']], columns=['A', 'B', 'C'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign unknown = None

```python
expected.loc[2, 'A'] = None
```

### Step 7: Assign unknown = None

```python
expected.loc[1, 'B'] = None
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'A,B,C\na,b,c\nd,,f\n,g,h\n'
result = parser.read_csv(StringIO(data))
expected = DataFrame([['a', 'b', 'c'], ['d', np.nan, 'f'], [np.nan, 'g', 'h']], columns=['A', 'B', 'C'])
if parser.engine == 'pyarrow':
    expected.loc[2, 'A'] = None
    expected.loc[1, 'B'] = None
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*