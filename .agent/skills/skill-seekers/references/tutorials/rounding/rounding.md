# How To: Rounding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rounding

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign formatter = EngFormatter(...)

```python
formatter = EngFormatter(accuracy=3, use_eng_prefix=True)
```

**Verification:**
```python
assert result == ' 0.000'
```

### Step 2: Assign in_out = value

```python
in_out = [(5.55555, ' 5.556'), (55.5555, ' 55.556'), (555.555, ' 555.555'), (5555.55, ' 5.556k'), (55555.5, ' 55.556k'), (555555, ' 555.555k')]
```

### Step 3: Call self.compare_all()

```python
self.compare_all(formatter, in_out)
```

### Step 4: Assign formatter = EngFormatter(...)

```python
formatter = EngFormatter(accuracy=1, use_eng_prefix=True)
```

### Step 5: Assign in_out = value

```python
in_out = [(5.55555, ' 5.6'), (55.5555, ' 55.6'), (555.555, ' 555.6'), (5555.55, ' 5.6k'), (55555.5, ' 55.6k'), (555555, ' 555.6k')]
```

### Step 6: Call self.compare_all()

```python
self.compare_all(formatter, in_out)
```

### Step 7: Assign formatter = EngFormatter(...)

```python
formatter = EngFormatter(accuracy=0, use_eng_prefix=True)
```

### Step 8: Assign in_out = value

```python
in_out = [(5.55555, ' 6'), (55.5555, ' 56'), (555.555, ' 556'), (5555.55, ' 6k'), (55555.5, ' 56k'), (555555, ' 556k')]
```

### Step 9: Call self.compare_all()

```python
self.compare_all(formatter, in_out)
```

### Step 10: Assign formatter = EngFormatter(...)

```python
formatter = EngFormatter(accuracy=3, use_eng_prefix=True)
```

### Step 11: Assign result = formatter(...)

```python
result = formatter(0)
```

**Verification:**
```python
assert result == ' 0.000'
```


## Complete Example

```python
# Workflow
formatter = EngFormatter(accuracy=3, use_eng_prefix=True)
in_out = [(5.55555, ' 5.556'), (55.5555, ' 55.556'), (555.555, ' 555.555'), (5555.55, ' 5.556k'), (55555.5, ' 55.556k'), (555555, ' 555.555k')]
self.compare_all(formatter, in_out)
formatter = EngFormatter(accuracy=1, use_eng_prefix=True)
in_out = [(5.55555, ' 5.6'), (55.5555, ' 55.6'), (555.555, ' 555.6'), (5555.55, ' 5.6k'), (55555.5, ' 55.6k'), (555555, ' 555.6k')]
self.compare_all(formatter, in_out)
formatter = EngFormatter(accuracy=0, use_eng_prefix=True)
in_out = [(5.55555, ' 6'), (55.5555, ' 56'), (555.555, ' 556'), (5555.55, ' 6k'), (55555.5, ' 56k'), (555555, ' 556k')]
self.compare_all(formatter, in_out)
formatter = EngFormatter(accuracy=3, use_eng_prefix=True)
result = formatter(0)
assert result == ' 0.000'
```

## Next Steps


---

*Source: test_eng_formatting.py:192 | Complexity: Advanced | Last updated: 2026-06-02*