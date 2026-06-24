# How To: Replace Inplace

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace inplace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame, float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
datetime_frame.loc[datetime_frame.index[:5], 'A'] = np.nan
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign unknown = value

```python
datetime_frame.loc[datetime_frame.index[-5:], 'A'] = np.nan
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign tsframe = datetime_frame.copy(...)

```python
tsframe = datetime_frame.copy()
```

### Step 4: Assign return_value = tsframe.replace(...)

```python
return_value = tsframe.replace(np.nan, 0, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))
```

### Step 6: Assign mf = float_string_frame

```python
mf = float_string_frame
```

### Step 7: Assign unknown = value

```python
mf.iloc[5:20, mf.columns.get_loc('foo')] = np.nan
```

### Step 8: Assign unknown = value

```python
mf.iloc[-10:, mf.columns.get_loc('A')] = np.nan
```

### Step 9: Assign result = float_string_frame.replace(...)

```python
result = float_string_frame.replace(np.nan, 0)
```

### Step 10: Assign expected = float_string_frame.copy(...)

```python
expected = float_string_frame.copy()
```

### Step 11: Assign unknown = unknown.astype(...)

```python
expected['foo'] = expected['foo'].astype(object)
```

### Step 12: Assign expected = expected.fillna(...)

```python
expected = expected.fillna(value=0)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign tsframe = datetime_frame.copy(...)

```python
tsframe = datetime_frame.copy()
```

### Step 15: Assign return_value = tsframe.replace(...)

```python
return_value = tsframe.replace([np.nan], [0], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame, float_string_frame

# Workflow
datetime_frame.loc[datetime_frame.index[:5], 'A'] = np.nan
datetime_frame.loc[datetime_frame.index[-5:], 'A'] = np.nan
tsframe = datetime_frame.copy()
return_value = tsframe.replace(np.nan, 0, inplace=True)
assert return_value is None
tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))
mf = float_string_frame
mf.iloc[5:20, mf.columns.get_loc('foo')] = np.nan
mf.iloc[-10:, mf.columns.get_loc('A')] = np.nan
result = float_string_frame.replace(np.nan, 0)
expected = float_string_frame.copy()
expected['foo'] = expected['foo'].astype(object)
expected = expected.fillna(value=0)
tm.assert_frame_equal(result, expected)
tsframe = datetime_frame.copy()
return_value = tsframe.replace([np.nan], [0], inplace=True)
assert return_value is None
tm.assert_frame_equal(tsframe, datetime_frame.fillna(0))
```

## Next Steps


---

*Source: test_replace.py:31 | Complexity: Advanced | Last updated: 2026-06-02*