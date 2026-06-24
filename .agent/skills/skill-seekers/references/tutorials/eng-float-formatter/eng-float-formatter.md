# How To: Eng Float Formatter

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eng float formatter

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1.41, 141.0, 14100, 1410000.0]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Call set_eng_float_format()

```python
set_eng_float_format()
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = df.to_string(...)

```python
result = df.to_string()
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = '             A\n0    1.410E+00\n1  141.000E+00\n2   14.100E+03\n3    1.410E+06'

```python
expected = '             A\n0    1.410E+00\n1  141.000E+00\n2   14.100E+03\n3    1.410E+06'
```

**Verification:**
```python
assert result == expected
```

### Step 5: Call set_eng_float_format()

```python
set_eng_float_format(use_eng_prefix=True)
```

### Step 6: Assign result = df.to_string(...)

```python
result = df.to_string()
```

### Step 7: Assign expected = '         A\n0    1.410\n1  141.000\n2  14.100k\n3   1.410M'

```python
expected = '         A\n0    1.410\n1  141.000\n2  14.100k\n3   1.410M'
```

**Verification:**
```python
assert result == expected
```

### Step 8: Call set_eng_float_format()

```python
set_eng_float_format(accuracy=0)
```

### Step 9: Assign result = df.to_string(...)

```python
result = df.to_string()
```

### Step 10: Assign expected = '         A\n0    1E+00\n1  141E+00\n2   14E+03\n3    1E+06'

```python
expected = '         A\n0    1E+00\n1  141E+00\n2   14E+03\n3    1E+06'
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1.41, 141.0, 14100, 1410000.0]})
set_eng_float_format()
result = df.to_string()
expected = '             A\n0    1.410E+00\n1  141.000E+00\n2   14.100E+03\n3    1.410E+06'
assert result == expected
set_eng_float_format(use_eng_prefix=True)
result = df.to_string()
expected = '         A\n0    1.410\n1  141.000\n2  14.100k\n3   1.410M'
assert result == expected
set_eng_float_format(accuracy=0)
result = df.to_string()
expected = '         A\n0    1E+00\n1  141E+00\n2   14E+03\n3    1E+06'
assert result == expected
```

## Next Steps


---

*Source: test_eng_formatting.py:33 | Complexity: Advanced | Last updated: 2026-06-02*