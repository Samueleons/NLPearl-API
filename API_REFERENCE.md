# NLPearl API Reference - V1 & V2

## Quick Reference

### Setup
```python
import nlpearl as pearl

pearl.api_key = "account_id:secret_key"
pearl.api_version = "v2"  # or "v1"
```

## Complete Method Reference

### Legend
- ✅ Available
- ❌ Not available (will raise error)
- 🔄 Available in both (automatically routes)

## Account Methods

| Method | V1 | V2 | Parameters |
|--------|----|----|------------|
| `Account.get_account()` | ✅ | ✅ | None |

**Returns:** Account information (name, creditBalance, totalAgents, status)

---

## Call Methods

| Method | V1 | V2 | Parameters |
|--------|----|----|------------|
| `Call.get_call(call_id)` | ✅ | ✅ | `call_id: str` |
| `Call.delete_calls(call_ids)` | ✅ | ✅ | `call_ids: list[str]` |

**Returns:** Call information or deletion confirmation

---

## Inbound Methods (V1 Only)

| Method | V1 | V2 | V2 Alternative |
|--------|----|----|----------------|
| `Inbound.get_all()` | ✅ | ❌ | `Pearl.get_all()` |
| `Inbound.get(inbound_id)` | ✅ | ❌ | `Pearl.get(pearl_id)` |
| `Inbound.set_active(inbound_id, is_active)` | ✅ | ❌ | `Pearl.set_active(pearl_id, is_active)` |
| `Inbound.get_ongoing_calls(inbound_id)` | ✅ | ❌ | `Pearl.get_ongoing_calls(pearl_id)` |
| `Inbound.get_calls(inbound_id, ...)` | ✅ | ❌ | `Pearl.get_calls(pearl_id, ...)` |
| `Inbound.get_analytics(inbound_id, ...)` | ✅ | ❌ | `Pearl.get_analytics(pearl_id, ...)` |

---

## Pearl Methods

| Method | V1 | V2 | Parameters |
|--------|----|----|------------|
| `Pearl.reset_customer_memory(pearl_id, phone)` | ✅ | ✅ | `pearl_id: str, phone_number: str` |
| `Pearl.reset_memory(pearl_id, phone)` | ✅ | ✅ | Same as above |
| `Pearl.get_all()` | ❌ | ✅ | None |
| `Pearl.get(pearl_id)` | ❌ | ✅ | `pearl_id: str` |
| `Pearl.set_active(pearl_id, is_active)` | ❌ | ✅ | `pearl_id: str, is_active: bool` |
| `Pearl.get_ongoing_calls(pearl_id)` | ❌ | ✅ | `pearl_id: str` |
| `Pearl.get_calls(pearl_id, ...)` | ❌ | ✅ | See parameters below |
| `Pearl.get_analytics(pearl_id, ...)` | ❌ | ✅ | See parameters below |

### Pearl.get_calls() Parameters (V2 Only)
```python
Pearl.get_calls(
    pearl_id: str,
    from_date: datetime | str,
    to_date: datetime | str,
    skip: int = 0,
    limit: int = 100,
    sort_prop: str | None = None,
    is_ascending: bool = True,
    tags: list[str] | None = None,
    statuses: list[int] | None = None,
    search_input: str | None = None
)
```

### Pearl.get_analytics() Parameters (V2 Only)
```python
Pearl.get_analytics(
    pearl_id: str,
    from_date: datetime | str,
    to_date: datetime | str  # Max 90 days range
)
```

---

## Outbound Methods

### V1 Only Methods

| Method | V1 | V2 | V2 Alternative |
|--------|----|----|----------------|
| `Outbound.get_all()` | ✅ | ❌ | `Pearl.get_all()` |
| `Outbound.get(outbound_id)` | ✅ | ❌ | `Pearl.get(pearl_id)` |
| `Outbound.set_active(outbound_id, is_active)` | ✅ | ❌ | `Pearl.set_active(pearl_id, is_active)` |
| `Outbound.get_calls(outbound_id, ...)` | ✅ | ❌ | `Pearl.get_calls(pearl_id, ...)` |
| `Outbound.make_call(outbound_id, to, ...)` | ✅ | ❌ | Different mechanism in V2 |
| `Outbound.get_call_request(request_id)` | ✅ | ❌ | Not in V2 |
| `Outbound.get_call_requests(outbound_id, ...)` | ✅ | ❌ | Not in V2 |
| `Outbound.get_analytics(outbound_id, ...)` | ✅ | ❌ | `Pearl.get_analytics(pearl_id, ...)` |

### Shared Methods (Work in Both V1 & V2)

| Method | V1 | V2 | ID Parameter |
|--------|----|----|--------------|
| `Outbound.add_lead(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.update_lead(id, lead_id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.get_lead_by_id(id, lead_id)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.get_lead_by_external_id(id, ext_id)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.get_lead_by_phone_number(id, phone)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.get_leads(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.delete_leads(id, lead_ids)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| `Outbound.delete_leads_by_external_id(id, ext_ids)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |

### Outbound.add_lead() Parameters
```python
Outbound.add_lead(
    id_param: str,  # outbound_id (V1) or pearl_id (V2)
    phone_number: str,  # Required
    external_id: str | None = None,
    time_zone_id: str | None = None,
    call_data: dict | None = None
)
```

### Outbound.get_leads() Parameters
```python
# V1
Outbound.get_leads(
    outbound_id: str,
    skip: int = 0,
    limit: int = 100,
    sort_prop: str | None = None,
    is_ascending: bool = True,
    status: int | None = None  # Single status in V1
)

# V2
Outbound.get_leads(
    pearl_id: str,
    skip: int = 0,
    limit: int = 100,
    sort_prop: str | None = None,
    is_ascending: bool = True,
    statuses: list[int] | None = None,  # Multiple statuses in V2
    search_input: str | None = None  # New in V2
)
```

---

## Status Codes

### Lead Status
| Code | Name | Description |
|------|------|-------------|
| 1 | New | Lead just added |
| 10 | NeedRetry | Needs to be called again |
| 20 | InCallQueue | Waiting in queue |
| 30 | WrongCountryCode | Invalid country code |
| 40 | OnCall | Currently on call |
| 70 | VoiceMailLeft | Voicemail was left |
| 100 | Success | Successfully completed |
| 110 | NotSuccessful | Not successful |
| 130 | Completed | Fully completed |
| 150 | Unreachable | Cannot be reached |
| 220 | Blacklisted | Blacklisted number |
| 500 | Error | Error occurred |

### Call Status
| Code | Name | Description |
|------|------|-------------|
| 3 | InProgress | Call in progress |
| 4 | Completed | Call completed |
| 5 | Busy | Line was busy |
| 6 | Failed | Call failed |
| 7 | NoAnswer | No answer |
| 8 | Canceled | Call canceled |

### Activity Status
| Code | Name | Description |
|------|------|-------------|
| 1 | Running | Active and running |
| 2 | Paused | Paused |
| 3 | Suspended | Suspended |
| 10 | TemporaryMaintenance | Under maintenance |

---

## Complete Endpoint Summary

### V1 API: 26 Endpoints
1. Account (1)
2. Call (2)
3. Inbound (6)
4. Outbound Management (5)
5. Lead Management (8)
6. Outbound Calling (3)
7. Memory (1)

### V2 API: 19 Endpoints
1. Account (1)
2. Call (2)
3. Pearl (6)
4. Lead Management (8)
5. Memory (2)

### Shared Across Versions: 11 Endpoints
- Account.get_account()
- Call.get_call()
- Call.delete_calls()
- Outbound.add_lead() *
- Outbound.update_lead() *
- Outbound.get_lead_by_id() *
- Outbound.get_lead_by_external_id() *
- Outbound.get_lead_by_phone_number() *
- Outbound.get_leads() *
- Outbound.delete_leads() *
- Outbound.delete_leads_by_external_id() *

\* Uses different ID parameter: `outbound_id` (V1) vs `pearl_id` (V2)

---

## Error Messages

### Using V2-only method in V1:
```
ValueError: get_all() is only available in API v2. 
Current version is v1. Set pearl.api_version = 'v2' to use this method.
```

### Using V1-only method in V2:
```
ValueError: Inbound.get_all() is only available in API v1. 
In v2, use Pearl.get_all() instead. 
Current version is v2. Set pearl.api_version = 'v1' to use Inbound methods.
```

---

**For complete usage examples, see:**
- `example_v1_usage.py` - All V1 endpoints
- `example_v2_usage.py` - All V2 endpoints
- `TESTING_GUIDE.md` - How to test everything

