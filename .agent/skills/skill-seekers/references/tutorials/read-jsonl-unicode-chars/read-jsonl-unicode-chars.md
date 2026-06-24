# How To: Read Jsonl Unicode Chars

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read jsonl unicode chars

## Prerequisites

**Required Modules:**
- `collections.abc`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json._json`


## Step-by-Step Guide

### Step 1: Assign json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'

```python
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
```

### Step 2: Assign json = StringIO(...)

```python
json = StringIO(json)
```

### Step 3: Assign result = read_json(...)

```python
result = read_json(json, lines=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'

```python
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
```

### Step 7: Assign result = read_json(...)

```python
result = read_json(StringIO(json), lines=True)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
json = StringIO(json)
result = read_json(json, lines=True)
expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
json = '{"a": "foo”", "b": "bar"}\n{"a": "foo", "b": "bar"}\n'
result = read_json(StringIO(json), lines=True)
expected = DataFrame([['foo”', 'bar'], ['foo', 'bar']], columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_readlines.py:76 | Complexity: Advanced | Last updated: 2026-06-02*