# How To: Repr Binary Type

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr binary type

## Prerequisites

**Required Modules:**
- `string`
- `pandas._config.config`
- `pandas.io.formats`


## Step-by-Step Guide

### Step 1: Assign letters = value

```python
letters = string.ascii_letters
```

**Verification:**
```python
assert res == repr(b)
```

### Step 2: Assign b = str(...)

```python
b = str(raw.decode('utf-8'))
```

**Verification:**
```python
assert res == b
```

### Step 3: Assign res = printing.pprint_thing(...)

```python
res = printing.pprint_thing(b, quote_strings=True)
```

**Verification:**
```python
assert res == repr(b)
```

### Step 4: Assign res = printing.pprint_thing(...)

```python
res = printing.pprint_thing(b, quote_strings=False)
```

**Verification:**
```python
assert res == b
```

### Step 5: Assign raw = bytes(...)

```python
raw = bytes(letters, encoding=cf.get_option('display.encoding'))
```

### Step 6: Assign raw = bytes(...)

```python
raw = bytes(letters)
```


## Complete Example

```python
# Workflow
letters = string.ascii_letters
try:
    raw = bytes(letters, encoding=cf.get_option('display.encoding'))
except TypeError:
    raw = bytes(letters)
b = str(raw.decode('utf-8'))
res = printing.pprint_thing(b, quote_strings=True)
assert res == repr(b)
res = printing.pprint_thing(b, quote_strings=False)
assert res == b
```

## Next Steps


---

*Source: test_printing.py:20 | Complexity: Advanced | Last updated: 2026-06-02*