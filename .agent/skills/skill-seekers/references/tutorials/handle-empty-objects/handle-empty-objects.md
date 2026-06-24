# How To: Handle Empty Objects

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test handle empty objects

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=list('abcd'))
```

### Step 2: Assign dfcopy = unknown.copy(...)

```python
dfcopy = df[:5].copy()
```

### Step 3: Assign unknown = 'bar'

```python
dfcopy['foo'] = 'bar'
```

### Step 4: Assign empty = value

```python
empty = df[5:5]
```

### Step 5: Assign frames = value

```python
frames = [dfcopy, empty, empty, df[5:]]
```

### Step 6: Assign concatted = concat(...)

```python
concatted = concat(frames, axis=0, sort=sort)
```

### Step 7: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=['a', 'b', 'c', 'd', 'foo'])
```

### Step 8: Assign unknown = unknown.astype(...)

```python
expected['foo'] = expected['foo'].astype(object if not using_infer_string else 'str')
```

### Step 9: Assign unknown = 'bar'

```python
expected.loc[0:4, 'foo'] = 'bar'
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted, expected)
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(10000)}, index=date_range('20130101', periods=10000, freq='s'))
```

### Step 12: Assign empty = DataFrame(...)

```python
empty = DataFrame()
```

### Step 13: Assign result = concat(...)

```python
result = concat([df, empty], axis=1)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 15: Assign result = concat(...)

```python
result = concat([empty, df], axis=1)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 17: Assign result = concat(...)

```python
result = concat([df, empty])
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 19: Assign result = concat(...)

```python
result = concat([empty, df])
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: sort, using_infer_string

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=list('abcd'))
dfcopy = df[:5].copy()
dfcopy['foo'] = 'bar'
empty = df[5:5]
frames = [dfcopy, empty, empty, df[5:]]
concatted = concat(frames, axis=0, sort=sort)
expected = df.reindex(columns=['a', 'b', 'c', 'd', 'foo'])
expected['foo'] = expected['foo'].astype(object if not using_infer_string else 'str')
expected.loc[0:4, 'foo'] = 'bar'
tm.assert_frame_equal(concatted, expected)
df = DataFrame({'A': range(10000)}, index=date_range('20130101', periods=10000, freq='s'))
empty = DataFrame()
result = concat([df, empty], axis=1)
tm.assert_frame_equal(result, df)
result = concat([empty, df], axis=1)
tm.assert_frame_equal(result, df)
result = concat([df, empty])
tm.assert_frame_equal(result, df)
result = concat([empty, df])
tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_empty.py:18 | Complexity: Advanced | Last updated: 2026-06-02*