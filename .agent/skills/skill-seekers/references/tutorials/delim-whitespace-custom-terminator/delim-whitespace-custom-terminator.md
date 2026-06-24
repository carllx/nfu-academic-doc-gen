# How To: Delim Whitespace Custom Terminator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delim whitespace custom terminator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only
```

## Step-by-Step Guide

### Step 1: Assign data = 'a b c~1 2 3~4 5 6~7 8 9'

```python
data = 'a b c~1 2 3~4 5 6~7 8 9'
```

### Step 2: Assign parser = c_parser_only

```python
parser = c_parser_only
```

### Step 3: Assign depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Assign df = parser.read_csv(...)

```python
df = parser.read_csv(StringIO(data), lineterminator='~', delim_whitespace=True)
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only

# Workflow
data = 'a b c~1 2 3~4 5 6~7 8 9'
parser = c_parser_only
depr_msg = "The 'delim_whitespace' keyword in pd.read_csv is deprecated"
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    df = parser.read_csv(StringIO(data), lineterminator='~', delim_whitespace=True)
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_c_parser_only.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*