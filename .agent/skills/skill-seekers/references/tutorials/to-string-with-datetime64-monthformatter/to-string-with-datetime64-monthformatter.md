# How To: To String With Datetime64 Monthformatter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to string with datetime64 monthformatter

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `re`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign months = value

```python
months = [datetime(2016, 1, 1), datetime(2016, 2, 2)]
```

**Verification:**
```python
assert result.strip() == expected
```

### Step 2: Assign x = DataFrame(...)

```python
x = DataFrame({'months': months})
```

### Step 3: Assign result = x.to_string(...)

```python
result = x.to_string(formatters={'months': format_func})
```

### Step 4: Assign expected = dedent(...)

```python
expected = dedent('            months\n            0 2016-01\n            1 2016-02')
```

**Verification:**
```python
assert result.strip() == expected
```


## Complete Example

```python
# Workflow
months = [datetime(2016, 1, 1), datetime(2016, 2, 2)]
x = DataFrame({'months': months})

def format_func(x):
    return x.strftime('%Y-%m')
result = x.to_string(formatters={'months': format_func})
expected = dedent('            months\n            0 2016-01\n            1 2016-02')
assert result.strip() == expected
```

## Next Steps


---

*Source: test_to_string.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*