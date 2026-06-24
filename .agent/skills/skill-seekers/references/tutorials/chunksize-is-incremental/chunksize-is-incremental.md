# How To: Chunksize Is Incremental

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test chunksize is incremental

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

### Step 1: Assign jsonl = value

```python
jsonl = '{"a": 1, "b": 2}\n        {"a": 3, "b": 4}\n        {"a": 5, "b": 6}\n        {"a": 7, "b": 8}\n' * 1000
```

**Verification:**
```python
assert len(list(read_json(reader, lines=True, chunksize=100))) > 1
```

### Step 2: Assign reader = MyReader(...)

```python
reader = MyReader(jsonl)
```

**Verification:**
```python
assert reader.read_count > 10
```

### Step 3: Assign self.read_count = 0

```python
self.read_count = 0
```

### Step 4: Assign self.stringio = StringIO(...)

```python
self.stringio = StringIO(contents)
```


## Complete Example

```python
# Workflow
jsonl = '{"a": 1, "b": 2}\n        {"a": 3, "b": 4}\n        {"a": 5, "b": 6}\n        {"a": 7, "b": 8}\n' * 1000

class MyReader:

    def __init__(self, contents) -> None:
        self.read_count = 0
        self.stringio = StringIO(contents)

    def read(self, *args):
        self.read_count += 1
        return self.stringio.read(*args)

    def __iter__(self) -> Iterator:
        self.read_count += 1
        return iter(self.stringio)
reader = MyReader(jsonl)
assert len(list(read_json(reader, lines=True, chunksize=100))) > 1
assert reader.read_count > 10
```

## Next Steps


---

*Source: test_readlines.py:379 | Complexity: Intermediate | Last updated: 2026-06-02*