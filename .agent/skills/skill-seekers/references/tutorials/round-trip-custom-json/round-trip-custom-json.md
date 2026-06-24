# How To: Round Trip Custom Json

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test round trip custom json

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `json`
- `re`
- `uuid`
- `assertions`
- `assertions`
- `assertions`
- `config`
- `schema`
- `schema`
- `orm`
- `orm`
- `sql`
- `sql.sqltypes`
- `sql.sqltypes`


## Step-by-Step Guide

### Step 1: Assign data_table = value

```python
data_table = self.tables.data_table
```

### Step 2: Assign data_element = value

```python
data_element = {'key1': 'data1'}
```

### Step 3: Assign js = mock.Mock(...)

```python
js = mock.Mock(side_effect=json.dumps)
```

### Step 4: Assign jd = mock.Mock(...)

```python
jd = mock.Mock(side_effect=json.loads)
```

### Step 5: Assign engine = engines.testing_engine(...)

```python
engine = engines.testing_engine(options=dict(json_serializer=js, json_deserializer=jd))
```

### Step 6: Call data_table.create()

```python
data_table.create(engine, checkfirst=True)
```

### Step 7: Call conn.execute()

```python
conn.execute(data_table.insert(), {'name': 'row1', 'data': data_element})
```

### Step 8: Assign row = conn.execute.first(...)

```python
row = conn.execute(select(data_table.c.data)).first()
```

### Step 9: Call eq_()

```python
eq_(row, (data_element,))
```

### Step 10: Call eq_()

```python
eq_(js.mock_calls, [mock.call(data_element)])
```

### Step 11: Call eq_()

```python
eq_(jd.mock_calls, [mock.call(json.dumps(data_element).encode())])
```

### Step 12: Call eq_()

```python
eq_(jd.mock_calls, [mock.call(json.dumps(data_element))])
```


## Complete Example

```python
# Workflow
data_table = self.tables.data_table
data_element = {'key1': 'data1'}
js = mock.Mock(side_effect=json.dumps)
jd = mock.Mock(side_effect=json.loads)
engine = engines.testing_engine(options=dict(json_serializer=js, json_deserializer=jd))
data_table.create(engine, checkfirst=True)
with engine.begin() as conn:
    conn.execute(data_table.insert(), {'name': 'row1', 'data': data_element})
    row = conn.execute(select(data_table.c.data)).first()
    eq_(row, (data_element,))
    eq_(js.mock_calls, [mock.call(data_element)])
    if testing.requires.json_deserializer_binary.enabled:
        eq_(jd.mock_calls, [mock.call(json.dumps(data_element).encode())])
    else:
        eq_(jd.mock_calls, [mock.call(json.dumps(data_element))])
```

## Next Steps


---

*Source: test_types.py:1593 | Complexity: Advanced | Last updated: 2026-06-02*