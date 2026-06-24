# How To: Format Thousands

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test format thousands

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: formatter, decimal, precision, func, col
```

## Step-by-Step Guide

### Step 1: Assign styler = value

```python
styler = DataFrame([[1000000.123456789]], index=[1000000.123456789]).style
```

**Verification:**
```python
assert '1_000_000' in result['body'][0][col]['display_value']
```

### Step 2: Assign result = getattr._translate(...)

```python
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
```

**Verification:**
```python
assert '1_000_000' in result['body'][0][col]['display_value']
```

### Step 3: Assign styler = value

```python
styler = DataFrame([[1000000]], index=[1000000]).style
```

**Verification:**
```python
assert '1_000_000' in result['body'][0][col]['display_value']
```

### Step 4: Assign result = getattr._translate(...)

```python
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
```

**Verification:**
```python
assert '1_000_000' in result['body'][0][col]['display_value']
```

### Step 5: Assign styler = value

```python
styler = DataFrame([[1 + 1000000.123456789j]], index=[1 + 1000000.123456789j]).style
```

### Step 6: Assign result = getattr._translate(...)

```python
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
```

**Verification:**
```python
assert '1_000_000' in result['body'][0][col]['display_value']
```


## Complete Example

```python
# Setup
# Fixtures: formatter, decimal, precision, func, col

# Workflow
styler = DataFrame([[1000000.123456789]], index=[1000000.123456789]).style
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
assert '1_000_000' in result['body'][0][col]['display_value']
styler = DataFrame([[1000000]], index=[1000000]).style
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
assert '1_000_000' in result['body'][0][col]['display_value']
styler = DataFrame([[1 + 1000000.123456789j]], index=[1 + 1000000.123456789j]).style
result = getattr(styler, func)(thousands='_', formatter=formatter, decimal=decimal, precision=precision)._translate(True, True)
assert '1_000_000' in result['body'][0][col]['display_value']
```

## Next Steps


---

*Source: test_format.py:370 | Complexity: Intermediate | Last updated: 2026-06-02*