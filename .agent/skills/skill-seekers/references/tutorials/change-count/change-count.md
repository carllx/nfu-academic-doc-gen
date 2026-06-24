# How To: Change Count

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate ChangeReport: test change count

## Prerequisites

**Required Modules:**
- `datetime`
- `skill_seekers.sync.models`


## Step-by-Step Guide

### Step 1: Assign report = ChangeReport(...)

```python
report = ChangeReport(skill_name='test-skill', total_pages=10, added=[PageChange(url='https://a.com', change_type=ChangeType.ADDED)], modified=[PageChange(url='https://b.com', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')], deleted=[PageChange(url='https://c.com', change_type=ChangeType.DELETED)])
```


## Complete Example

```python
# Workflow
report = ChangeReport(skill_name='test-skill', total_pages=10, added=[PageChange(url='https://a.com', change_type=ChangeType.ADDED)], modified=[PageChange(url='https://b.com', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')], deleted=[PageChange(url='https://c.com', change_type=ChangeType.DELETED)])
```

## Next Steps


---

*Source: test_sync_models.py:91 | Complexity: Beginner | Last updated: 2026-06-02*