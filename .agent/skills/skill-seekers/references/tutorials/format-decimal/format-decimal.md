# How To: Format Decimal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test format decimal

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
# Fixtures: formatter, thousands, precision, func, col
```

## Step-by-Step Guide

### Step 1: Assign styler = value

```python
styler = DataFrame([[1000000.123456789]], index=[1000000.123456789]).style
```

**Verification:**
```python
assert '000_123' in result['body'][0][col]['display_value']
```

### Step 2: Assign result = getattr._translate(...)

```python
result = getattr(styler, func)(decimal='_', formatter=formatter, thousands=thousands, precision=precision)._translate(True, True)
```

**Verification:**
```python
assert '000_123' in result['body'][0][col]['display_value']
```

### Step 3: Assign styler = value

```python
styler = DataFrame([[1 + 1000000.123456789j]], index=[1 + 1000000.123456789j]).style
```

### Step 4: Assign result = getattr._translate(...)

```python
result = getattr(styler, func)(decimal='_', formatter=formatter, thousands=thousands, precision=precision)._translate(True, True)
```

**Verification:**
```python
assert '000_123' in result['body'][0][col]['display_value']
```


## Complete Example

```python
# Setup
# Fixtures: formatter, thousands, precision, func, col

# Workflow
styler = DataFrame([[1000000.123456789]], index=[1000000.123456789]).style
result = getattr(styler, func)(decimal='_', formatter=formatter, thousands=thousands, precision=precision)._translate(True, True)
assert '000_123' in result['body'][0][col]['display_value']
styler = DataFrame([[1 + 1000000.123456789j]], index=[1 + 1000000.123456789j]).style
result = getattr(styler, func)(decimal='_', formatter=formatter, thousands=thousands, precision=precision)._translate(True, True)
assert '000_123' in result['body'][0][col]['display_value']
```

## Next Steps


---

*Source: test_format.py:394 | Complexity: Intermediate | Last updated: 2026-06-02*