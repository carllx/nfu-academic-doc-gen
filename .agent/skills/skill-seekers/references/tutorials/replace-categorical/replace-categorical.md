# How To: Replace Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: to_replace, value, result, expected_error_msg
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b'])
```

### Step 2: Assign expected = Categorical(...)

```python
expected = Categorical(result)
```

### Step 3: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

### Step 4: Assign warn = value

```python
warn = FutureWarning if expected_error_msg is not None else None
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 6: Assign ser = pd.Series(...)

```python
ser = pd.Series(cat, copy=False)
```

### Step 7: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, expected)
```

### Step 8: Assign result = value

```python
result = pd.Series(cat, copy=False).replace(to_replace, value)._values
```

### Step 9: Call ser.replace()

```python
ser.replace(to_replace, value, inplace=True)
```

### Step 10: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, expected)
```


## Complete Example

```python
# Setup
# Fixtures: to_replace, value, result, expected_error_msg

# Workflow
cat = Categorical(['a', 'b'])
expected = Categorical(result)
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
warn = FutureWarning if expected_error_msg is not None else None
with tm.assert_produces_warning(warn, match=msg):
    result = pd.Series(cat, copy=False).replace(to_replace, value)._values
tm.assert_categorical_equal(result, expected)
if to_replace == 'b':
    with pytest.raises(AssertionError, match=expected_error_msg):
        tm.assert_categorical_equal(cat, expected)
ser = pd.Series(cat, copy=False)
with tm.assert_produces_warning(warn, match=msg):
    ser.replace(to_replace, value, inplace=True)
tm.assert_categorical_equal(cat, expected)
```

## Next Steps


---

*Source: test_replace.py:62 | Complexity: Advanced | Last updated: 2026-06-02*