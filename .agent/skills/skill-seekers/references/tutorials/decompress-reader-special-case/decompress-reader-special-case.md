# How To: Decompress Reader Special Case

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test decompress reader special case

## Prerequisites

**Required Modules:**
- `gitdb.test.lib`
- `gitdb`
- `gitdb.util`
- `zlib`
- `gitdb.typ`
- `tempfile`
- `os`
- `io`


## Step-by-Step Guide

### Step 1: Assign odb = LooseObjectDB(...)

```python
odb = LooseObjectDB(fixture_path('objects'))
```

**Verification:**
```python
assert len(data) == ostream.size
```

### Step 2: Assign mdb = MemoryDB(...)

```python
mdb = MemoryDB()
```

**Verification:**
```python
assert dump.hexsha == sha
```

### Step 3: Assign ostream = odb.stream(...)

```python
ostream = odb.stream(hex_to_bin(sha))
```

### Step 4: Assign data = ostream.read(...)

```python
data = ostream.read()
```

**Verification:**
```python
assert len(data) == ostream.size
```

### Step 5: Assign dump = mdb.store(...)

```python
dump = mdb.store(IStream(ostream.type, ostream.size, BytesIO(data)))
```

**Verification:**
```python
assert dump.hexsha == sha
```


## Complete Example

```python
# Workflow
odb = LooseObjectDB(fixture_path('objects'))
mdb = MemoryDB()
for sha in (b'888401851f15db0eed60eb1bc29dec5ddcace911', b'7bb839852ed5e3a069966281bb08d50012fb309b'):
    ostream = odb.stream(hex_to_bin(sha))
    data = ostream.read()
    assert len(data) == ostream.size
    dump = mdb.store(IStream(ostream.type, ostream.size, BytesIO(data)))
    assert dump.hexsha == sha
```

## Next Steps


---

*Source: test_stream.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*