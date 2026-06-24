# How To: To Jsonl

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to jsonl

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = df.to_json(...)

```python
result = df.to_json(orient='records', lines=True)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = '{"a":1,"b":2}\n{"a":1,"b":2}\n'

```python
expected = '{"a":1,"b":2}\n{"a":1,"b":2}\n'
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame([['foo}', 'bar'], ['foo"', 'bar']], columns=['a', 'b'])
```

### Step 5: Assign result = df.to_json(...)

```python
result = df.to_json(orient='records', lines=True)
```

### Step 6: Assign expected = '{"a":"foo}","b":"bar"}\n{"a":"foo\\"","b":"bar"}\n'

```python
expected = '{"a":"foo}","b":"bar"}\n{"a":"foo\\"","b":"bar"}\n'
```

**Verification:**
```python
assert result == expected
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(read_json(StringIO(result), lines=True), df)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame([['foo\\', 'bar'], ['foo"', 'bar']], columns=['a\\', 'b'])
```

### Step 9: Assign result = df.to_json(...)

```python
result = df.to_json(orient='records', lines=True)
```

### Step 10: Assign expected = '{"a\\\\":"foo\\\\","b":"bar"}\n{"a\\\\":"foo\\"","b":"bar"}\n'

```python
expected = '{"a\\\\":"foo\\\\","b":"bar"}\n{"a\\\\":"foo\\"","b":"bar"}\n'
```

**Verification:**
```python
assert result == expected
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(read_json(StringIO(result), lines=True), df)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2], [1, 2]], columns=['a', 'b'])
result = df.to_json(orient='records', lines=True)
expected = '{"a":1,"b":2}\n{"a":1,"b":2}\n'
assert result == expected
df = DataFrame([['foo}', 'bar'], ['foo"', 'bar']], columns=['a', 'b'])
result = df.to_json(orient='records', lines=True)
expected = '{"a":"foo}","b":"bar"}\n{"a":"foo\\"","b":"bar"}\n'
assert result == expected
tm.assert_frame_equal(read_json(StringIO(result), lines=True), df)
df = DataFrame([['foo\\', 'bar'], ['foo"', 'bar']], columns=['a\\', 'b'])
result = df.to_json(orient='records', lines=True)
expected = '{"a\\\\":"foo\\\\","b":"bar"}\n{"a\\\\":"foo\\"","b":"bar"}\n'
assert result == expected
tm.assert_frame_equal(read_json(StringIO(result), lines=True), df)
```

## Next Steps


---

*Source: test_readlines.py:94 | Complexity: Advanced | Last updated: 2026-06-02*