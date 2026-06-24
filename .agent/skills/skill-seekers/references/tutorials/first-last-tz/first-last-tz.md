# How To: First Last Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test first last tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, expected_first, expected_last
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 2: Assign result = df.groupby.first(...)

```python
result = df.groupby('id', as_index=False).first()
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_first)
```

### Step 4: Assign cols = value

```python
cols = ['id', 'time', 'foo']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result[cols], expected[cols])
```

### Step 6: Assign result = unknown.first(...)

```python
result = df.groupby('id', as_index=False)['time'].first()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected[['id', 'time']])
```

### Step 8: Assign result = df.groupby.last(...)

```python
result = df.groupby('id', as_index=False).last()
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_last)
```

### Step 10: Assign cols = value

```python
cols = ['id', 'time', 'foo']
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result[cols], expected[cols])
```

### Step 12: Assign result = unknown.last(...)

```python
result = df.groupby('id', as_index=False)['time'].last()
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected[['id', 'time']])
```


## Complete Example

```python
# Setup
# Fixtures: data, expected_first, expected_last

# Workflow
df = DataFrame(data)
result = df.groupby('id', as_index=False).first()
expected = DataFrame(expected_first)
cols = ['id', 'time', 'foo']
tm.assert_frame_equal(result[cols], expected[cols])
result = df.groupby('id', as_index=False)['time'].first()
tm.assert_frame_equal(result, expected[['id', 'time']])
result = df.groupby('id', as_index=False).last()
expected = DataFrame(expected_last)
cols = ['id', 'time', 'foo']
tm.assert_frame_equal(result[cols], expected[cols])
result = df.groupby('id', as_index=False)['time'].last()
tm.assert_frame_equal(result, expected[['id', 'time']])
```

## Next Steps


---

*Source: test_nth.py:384 | Complexity: Advanced | Last updated: 2026-06-02*