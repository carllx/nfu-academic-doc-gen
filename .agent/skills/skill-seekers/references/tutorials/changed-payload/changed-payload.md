# How To: Changed Payload

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate ChangeReport: changed payload

## Prerequisites

**Required Modules:**
- `pytest`
- `unittest.mock`
- `skill_seekers.sync.notifier`
- `skill_seekers.sync.models`


## Step-by-Step Guide

### Step 1: Assign report = ChangeReport(...)

```python
report = ChangeReport(skill_name='test-skill', total_pages=5, added=[PageChange(url='https://new.page', change_type=ChangeType.ADDED)], modified=[PageChange(url='https://mod.page', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')], deleted=[PageChange(url='https://del.page', change_type=ChangeType.DELETED)])
```


## Complete Example

```python
# Workflow
report = ChangeReport(skill_name='test-skill', total_pages=5, added=[PageChange(url='https://new.page', change_type=ChangeType.ADDED)], modified=[PageChange(url='https://mod.page', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')], deleted=[PageChange(url='https://del.page', change_type=ChangeType.DELETED)])
```

## Next Steps


---

*Source: test_sync_notifier.py:20 | Complexity: Beginner | Last updated: 2026-06-02*