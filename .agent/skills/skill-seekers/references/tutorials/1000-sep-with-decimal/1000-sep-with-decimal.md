# How To: 1000 Sep With Decimal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test 1000 sep with decimal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, data, thousands, decimal
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 10], 'B': [2334.01, 13], 'C': [5, 10.0]})
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep='|', thousands=thousands, decimal=decimal)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = "The 'thousands' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'thousands' option is not supported with the 'pyarrow' engine"
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), sep='|', thousands=thousands, decimal=decimal)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, data, thousands, decimal

# Workflow
parser = all_parsers
expected = DataFrame({'A': [1, 10], 'B': [2334.01, 13], 'C': [5, 10.0]})
if parser.engine == 'pyarrow':
    msg = "The 'thousands' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), sep='|', thousands=thousands, decimal=decimal)
    return
result = parser.read_csv(StringIO(data), sep='|', thousands=thousands, decimal=decimal)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*