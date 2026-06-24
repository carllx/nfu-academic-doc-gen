# How To: Add Timedeltaarraylike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add timedeltaarraylike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: tda
```

## Step-by-Step Guide

### Step 1: Assign tda_nano = tda.astype(...)

```python
tda_nano = tda.astype('m8[ns]')
```

### Step 2: Assign expected = value

```python
expected = tda_nano * 2
```

### Step 3: Assign res = value

```python
res = tda_nano + tda
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```

### Step 5: Assign res = value

```python
res = tda + tda_nano
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```

### Step 7: Assign expected = value

```python
expected = tda_nano * 0
```

### Step 8: Assign res = value

```python
res = tda - tda_nano
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```

### Step 10: Assign res = value

```python
res = tda_nano - tda
```

### Step 11: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tda

# Workflow
tda_nano = tda.astype('m8[ns]')
expected = tda_nano * 2
res = tda_nano + tda
tm.assert_extension_array_equal(res, expected)
res = tda + tda_nano
tm.assert_extension_array_equal(res, expected)
expected = tda_nano * 0
res = tda - tda_nano
tm.assert_extension_array_equal(res, expected)
res = tda_nano - tda
tm.assert_extension_array_equal(res, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:179 | Complexity: Advanced | Last updated: 2026-06-02*