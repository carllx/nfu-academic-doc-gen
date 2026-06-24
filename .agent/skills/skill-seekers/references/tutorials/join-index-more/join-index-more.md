# How To: Join Index More

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join index more

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign af = value

```python
af = float_frame.loc[:, ['A', 'B']]
```

### Step 2: Assign bf = value

```python
bf = float_frame.loc[::2, ['C', 'D']]
```

### Step 3: Assign expected = af.copy(...)

```python
expected = af.copy()
```

### Step 4: Assign unknown = value

```python
expected['C'] = float_frame['C'][::2]
```

### Step 5: Assign unknown = value

```python
expected['D'] = float_frame['D'][::2]
```

### Step 6: Assign result = af.join(...)

```python
result = af.join(bf)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = af.join(...)

```python
result = af.join(bf, how='right')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected[::2])
```

### Step 10: Assign result = bf.join(...)

```python
result = bf.join(af, how='right')
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.loc[:, result.columns])
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
af = float_frame.loc[:, ['A', 'B']]
bf = float_frame.loc[::2, ['C', 'D']]
expected = af.copy()
expected['C'] = float_frame['C'][::2]
expected['D'] = float_frame['D'][::2]
result = af.join(bf)
tm.assert_frame_equal(result, expected)
result = af.join(bf, how='right')
tm.assert_frame_equal(result, expected[::2])
result = bf.join(af, how='right')
tm.assert_frame_equal(result, expected.loc[:, result.columns])
```

## Next Steps


---

*Source: test_join.py:305 | Complexity: Advanced | Last updated: 2026-06-02*