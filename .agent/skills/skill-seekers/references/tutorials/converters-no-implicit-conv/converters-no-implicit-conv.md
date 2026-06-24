# How To: Converters No Implicit Conv

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converters no implicit conv

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pandas`
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

### Step 2: Assign data = '000102,1.2,A\n001245,2,B'

```python
data = '000102,1.2,A\n001245,2,B'
```

### Step 3: Assign converters = value

```python
converters = {0: lambda x: x.strip()}
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, converters=converters)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([['000102', 1.2, 'A'], ['001245', 2, 'B']])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), header=None, converters=converters)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '000102,1.2,A\n001245,2,B'
converters = {0: lambda x: x.strip()}
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), header=None, converters=converters)
    return
result = parser.read_csv(StringIO(data), header=None, converters=converters)
expected = DataFrame([['000102', 1.2, 'A'], ['001245', 2, 'B']])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_converters.py:58 | Complexity: Advanced | Last updated: 2026-06-02*