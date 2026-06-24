# How To: Full Config

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full config

## Prerequisites

**Required Modules:**
- `datetime`
- `skill_seekers.sync.models`


## Step-by-Step Guide

### Step 1: Assign config = SyncConfig(...)

```python
config = SyncConfig(skill_config='configs/react.json', check_interval=1800, auto_update=True, notification_channels=['slack', 'webhook'], webhook_url='https://hooks.example.com/webhook', slack_webhook='https://hooks.slack.com/services/T000/B000/XXX', email_recipients=['dev@example.com'])
```

**Verification:**
```python
assert config.check_interval == 1800
```


## Complete Example

```python
# Workflow
config = SyncConfig(skill_config='configs/react.json', check_interval=1800, auto_update=True, notification_channels=['slack', 'webhook'], webhook_url='https://hooks.example.com/webhook', slack_webhook='https://hooks.slack.com/services/T000/B000/XXX', email_recipients=['dev@example.com'])
assert config.check_interval == 1800
assert config.auto_update is True
assert 'slack' in config.notification_channels
assert config.webhook_url == 'https://hooks.example.com/webhook'
assert 'dev@example.com' in config.email_recipients
```

## Next Steps


---

*Source: test_sync_models.py:122 | Complexity: Beginner | Last updated: 2026-06-02*