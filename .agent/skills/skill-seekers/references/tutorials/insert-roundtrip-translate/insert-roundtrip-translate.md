# How To: Insert Roundtrip Translate

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Table: test insert roundtrip translate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `assertions`
- `assertions`
- `config`
- `provision`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: connection, implicit_returning
```

## Step-by-Step Guide

### Step 1: Assign seq_no_returning = Table(...)

```python
seq_no_returning = Table('seq_no_returning_sch', MetaData(), Column('id', Integer, normalize_sequence(config, Sequence('noret_sch_id_seq', schema='alt_schema')), primary_key=True), Column('data', String(50)), implicit_returning=implicit_returning, schema='alt_schema')
```


## Complete Example

```python
# Setup
# Fixtures: connection, implicit_returning

# Workflow
seq_no_returning = Table('seq_no_returning_sch', MetaData(), Column('id', Integer, normalize_sequence(config, Sequence('noret_sch_id_seq', schema='alt_schema')), primary_key=True), Column('data', String(50)), implicit_returning=implicit_returning, schema='alt_schema')
```

## Next Steps


---

*Source: test_sequence.py:129 | Complexity: Beginner | Last updated: 2026-06-02*