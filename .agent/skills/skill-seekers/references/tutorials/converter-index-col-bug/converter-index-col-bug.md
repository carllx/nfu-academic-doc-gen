# How To: Converter Index Col Bug

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test converter index col bug

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
# Fixtures: all_parsers, conv_f
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A;B\n1;2\n3;4'

```python
data = 'A;B\n1;2\n3;4'
```

### Step 3: Assign rs = parser.read_csv(...)

```python
rs = parser.read_csv(StringIO(data), sep=';', index_col='A', converters={'A': conv_f})
```

### Step 4: Assign xp = DataFrame(...)

```python
xp = DataFrame({'B': [2, 4]}, index=Index(['1', '3'], name='A'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, xp)
```

### Step 6: Assign msg = "The 'converters' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'converters' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), sep=';', index_col='A', converters={'A': conv_f})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, conv_f

# Workflow
parser = all_parsers
data = 'A;B\n1;2\n3;4'
if parser.engine == 'pyarrow':
    msg = "The 'converters' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), sep=';', index_col='A', converters={'A': conv_f})
    return
rs = parser.read_csv(StringIO(data), sep=';', index_col='A', converters={'A': conv_f})
xp = DataFrame({'B': [2, 4]}, index=Index(['1', '3'], name='A'))
tm.assert_frame_equal(rs, xp)
```

## Next Steps


---

*Source: test_converters.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*