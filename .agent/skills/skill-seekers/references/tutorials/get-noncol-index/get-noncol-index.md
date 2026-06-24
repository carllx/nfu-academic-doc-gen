# How To: Get Noncol Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get noncol index

## Prerequisites

**Required Modules:**
- `contextlib`
- `operator`
- `re`
- `sqlalchemy`
- `provision`
- `provision`
- `schema`
- `schema`
- `engine`
- `engine`
- `engine`
- `exc`
- `exc`
- `schema`
- `schema`
- `sql.elements`
- `sql.schema`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `sqlalchemy`


## Step-by-Step Guide

### Step 1: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 2: Assign indexes = insp.get_indexes(...)

```python
indexes = insp.get_indexes(tname)
```

### Step 3: Assign expected_indexes = value

```python
expected_indexes = self.exp_indexes()[None, tname]
```

### Step 4: Call self._check_list()

```python
self._check_list(indexes, expected_indexes, self._required_index_keys)
```

### Step 5: Assign t = Table(...)

```python
t = Table(tname, MetaData(), autoload_with=connection)
```

### Step 6: Call eq_()

```python
eq_(len(t.indexes), 1)
```

### Step 7: Call is_()

```python
is_(list(t.indexes)[0].table, t)
```

### Step 8: Call eq_()

```python
eq_(list(t.indexes)[0].name, ixname)
```


## Complete Example

```python
# Workflow
insp = inspect(connection)
indexes = insp.get_indexes(tname)
expected_indexes = self.exp_indexes()[None, tname]
self._check_list(indexes, expected_indexes, self._required_index_keys)
t = Table(tname, MetaData(), autoload_with=connection)
eq_(len(t.indexes), 1)
is_(list(t.indexes)[0].table, t)
eq_(list(t.indexes)[0].name, ixname)
```

## Next Steps


---

*Source: test_reflection.py:2018 | Complexity: Advanced | Last updated: 2026-06-02*