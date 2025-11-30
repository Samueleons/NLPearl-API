# NLPearl Python Wrapper

NLPearl is a Python wrapper for the NLPearl API, allowing developers to interact seamlessly with NLPearl's services. This package supports both API V1 and V2 with a unified interface.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Quick Start](#quick-start)
- [API Versions](#api-versions)
- [Usage Guide](#usage-guide)
  - [V2 API (Default)](#v2-api-default)
  - [V1 API](#v1-api)
  - [Shared Methods](#shared-methods)
- [Complete API Reference](#complete-api-reference)
- [Migration Guide](#migration-guide)
- [License](#license)

## Installation

```bash
pip install nlpearl
```

## Getting Started

1. Get your API key from [NLPearl](mailto:samuel@nlpearl.ai)
2. Set your API version (V2 is default)
3. Start making API calls!

```python
import nlpearl as pearl

# Configuration
pearl.api_key = "your_api_key_here"
pearl.api_version = "v2"  # Default, can be "v1" or "v2"
```

## Quick Start

### V2 Example (Default)

```python
import nlpearl as pearl

pearl.api_key = "your_key"
pearl.api_version = "v2"  # Default

# Get all pearls
pearls = pearl.Pearl.get_all()

# Add a lead using pearl_id
pearl.Outbound.add_lead(
    pearl_id,
    phone_number="+1234567890",
    call_data={"firstName": "John"}
)

# Get analytics
analytics = pearl.Pearl.get_analytics(
    pearl_id,
    from_date="2024-01-01T00:00:00.000Z",
    to_date="2024-01-31T23:59:59.999Z"
)
```

### V1 Example

```python
import nlpearl as pearl

pearl.api_key = "your_key"
pearl.api_version = "v1"

# Get all inbounds
inbounds = pearl.Inbound.get_all()

# Add a lead using outbound_id
pearl.Outbound.add_lead(
    outbound_id,
    phone_number="+1234567890",
    call_data={"firstName": "John"}
)

# Get analytics
analytics = pearl.Outbound.get_analytics(
    outbound_id,
    from_date="2024-01-01T00:00:00.000Z",
    to_date="2024-01-31T23:59:59.999Z"
)
```

## API Versions

**The wrapper uses the same class names for both V1 and V2**, automatically routing to the correct endpoints based on `pearl.api_version`.

### Version Differences

| Feature | V1 | V2 |
|---------|----|----|
| **Default** | No | **Yes** |
| **Structure** | Separate Inbound/Outbound | Unified Pearl |
| **ID Parameter** | `outbound_id`, `inbound_id` | `pearl_id` |
| **Classes** | `Inbound`, `Outbound` | `Pearl` |
| **Lead Operations** | `Outbound.add_lead(outbound_id, ...)` | `Outbound.add_lead(pearl_id, ...)` |

### Unified API Approach

✅ **Same class names** - Use `pearl.Outbound`, `pearl.Pearl`, `pearl.Inbound`  
✅ **Automatic routing** - Methods route to correct version based on `api_version`  
✅ **Clear errors** - Helpful messages when using wrong version  
✅ **Version switching** - Change `api_version` anytime  

**No separate V2 classes needed!** Just set the version once and use the same API.

## Usage Guide

### V2 API (Default)

#### Pearl Management

```python
pearl.api_version = "v2"

# Get all pearls
pearls = pearl.Pearl.get_all()

# Get specific pearl
pearl_details = pearl.Pearl.get(pearl_id)

# Activate/Deactivate
pearl.Pearl.set_active(pearl_id, is_active=True)

# Get ongoing calls
ongoing = pearl.Pearl.get_ongoing_calls(pearl_id)

# Get calls with filters
calls = pearl.Pearl.get_calls(
    pearl_id,
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 1, 31),
    tags=["important"],
    statuses=[100, 130]
)

# Get analytics
analytics = pearl.Pearl.get_analytics(pearl_id, from_date, to_date)
```

#### Lead Management (V2)

```python
# Add lead (using pearl_id)
lead = pearl.Outbound.add_lead(
    pearl_id,
    phone_number="+1234567890",
    external_id="ext123",
    time_zone_id="Pacific Standard Time",
    call_data={"firstName": "John", "lastName": "Doe"}
)

# Get lead
lead = pearl.Outbound.get_lead_by_id(pearl_id, lead_id)
lead = pearl.Outbound.get_lead_by_external_id(pearl_id, "ext123")
lead = pearl.Outbound.get_lead_by_phone_number(pearl_id, "+1234567890")

# Update lead
pearl.Outbound.update_lead(
    pearl_id,
    lead_id,
    status=100,  # Mark as Success
    call_data={"notes": "Contact successful"}
)

# Search leads
leads = pearl.Outbound.get_leads(
    pearl_id,
    statuses=[1, 10],  # New and NeedRetry
    search_input="John",
    limit=50
)

# Delete leads
pearl.Outbound.delete_leads(pearl_id, [lead_id1, lead_id2])
pearl.Outbound.delete_leads_by_external_id(pearl_id, ["ext1", "ext2"])
```

### V1 API

#### Inbound Operations (V1 Only)

```python
pearl.api_version = "v1"

# Get all inbounds
inbounds = pearl.Inbound.get_all()

# Get specific inbound
inbound = pearl.Inbound.get(inbound_id)

# Activate/Deactivate
pearl.Inbound.set_active(inbound_id, is_active=True)

# Get ongoing calls
ongoing = pearl.Inbound.get_ongoing_calls(inbound_id)

# Get calls
calls = pearl.Inbound.get_calls(
    inbound_id,
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 1, 31),
    tags=["important"]
)

# Get analytics
analytics = pearl.Inbound.get_analytics(inbound_id, from_date, to_date)
```

#### Outbound Operations (V1)

```python
# Get all outbounds
outbounds = pearl.Outbound.get_all()

# Get specific outbound
outbound = pearl.Outbound.get(outbound_id)

# Activate/Deactivate
pearl.Outbound.set_active(outbound_id, is_active=True)

# Get calls
calls = pearl.Outbound.get_calls(
    outbound_id,
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 1, 31)
)

# Make a call
result = pearl.Outbound.make_call(
    outbound_id,
    to="+1234567890",
    call_data={"firstName": "Jane"}
)

# Get call requests
requests = pearl.Outbound.get_call_requests(
    outbound_id,
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 1, 31)
)

# Get analytics
analytics = pearl.Outbound.get_analytics(outbound_id, from_date, to_date)
```

#### Lead Management (V1)

```python
# Add lead (using outbound_id)
lead = pearl.Outbound.add_lead(
    outbound_id,  # Note: outbound_id in V1, pearl_id in V2
    phone_number="+1234567890",
    external_id="ext123",
    call_data={"firstName": "John"}
)

# Update lead
pearl.Outbound.update_lead(outbound_id, lead_id, status=100)

# Search leads
leads = pearl.Outbound.get_leads(
    outbound_id,
    status=1  # Note: V1 uses 'status', V2 uses 'statuses'
)

# Other lead methods work the same
lead = pearl.Outbound.get_lead_by_id(outbound_id, lead_id)
pearl.Outbound.delete_leads(outbound_id, [lead_id1, lead_id2])
```

### Shared Methods

These methods work in **both V1 and V2**:

#### Account

```python
# Works in both versions
account = pearl.Account.get_account()
print(f"Balance: {account['creditBalance']}")
```

#### Call Operations

```python
# Get call info (both versions)
call = pearl.Call.get_call(call_id)

# Delete calls (both versions)
pearl.Call.delete_calls([call_id1, call_id2])
```

#### Memory Management

```python
# V1
pearl.Pearl.reset_customer_memory(pearl_id, phone_number)

# V2 (same method works)
pearl.Pearl.reset_memory(pearl_id, phone_number)
```

## Complete API Reference

### Method Availability

| Class | Method | V1 | V2 | Notes |
|-------|--------|----|----|-------|
| **Account** | `get_account()` | ✅ | ✅ | |
| **Call** | `get_call(call_id)` | ✅ | ✅ | |
| **Call** | `delete_calls(call_ids)` | ✅ | ✅ | |
| **Inbound** | `get_all()` | ✅ | ❌ | Use `Pearl.get_all()` in V2 |
| **Inbound** | `get(inbound_id)` | ✅ | ❌ | Use `Pearl.get(pearl_id)` in V2 |
| **Inbound** | `set_active(...)` | ✅ | ❌ | Use `Pearl.set_active(...)` in V2 |
| **Inbound** | `get_calls(...)` | ✅ | ❌ | Use `Pearl.get_calls(...)` in V2 |
| **Inbound** | `get_ongoing_calls(...)` | ✅ | ❌ | Use `Pearl.get_ongoing_calls(...)` in V2 |
| **Inbound** | `get_analytics(...)` | ✅ | ❌ | Use `Pearl.get_analytics(...)` in V2 |
| **Outbound** | `get_all()` | ✅ | ❌ | Use `Pearl.get_all()` in V2 |
| **Outbound** | `get(outbound_id)` | ✅ | ❌ | Use `Pearl.get(pearl_id)` in V2 |
| **Outbound** | `set_active(...)` | ✅ | ❌ | Use `Pearl.set_active(...)` in V2 |
| **Outbound** | `get_calls(...)` | ✅ | ❌ | Use `Pearl.get_calls(...)` in V2 |
| **Outbound** | `add_lead(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `update_lead(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `get_leads(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `get_lead_by_id(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `get_lead_by_external_id(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `get_lead_by_phone_number(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `delete_leads(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `delete_leads_by_external_id(id, ...)` | ✅ | ✅ | V1: outbound_id, V2: pearl_id |
| **Outbound** | `make_call(...)` | ✅ | ❌ | V1 only |
| **Outbound** | `get_call_request(...)` | ✅ | ❌ | V1 only |
| **Outbound** | `get_call_requests(...)` | ✅ | ❌ | V1 only |
| **Outbound** | `get_analytics(...)` | ✅ | ❌ | Use `Pearl.get_analytics(...)` in V2 |
| **Pearl** | `reset_customer_memory(...)` | ✅ | ✅ | |
| **Pearl** | `reset_memory(...)` | ✅ | ✅ | Same as above |
| **Pearl** | `get_all()` | ❌ | ✅ | V2 only |
| **Pearl** | `get(pearl_id)` | ❌ | ✅ | V2 only |
| **Pearl** | `set_active(...)` | ❌ | ✅ | V2 only |
| **Pearl** | `get_calls(...)` | ❌ | ✅ | V2 only |
| **Pearl** | `get_ongoing_calls(...)` | ❌ | ✅ | V2 only |
| **Pearl** | `get_analytics(...)` | ❌ | ✅ | V2 only |

### Status Codes

#### Lead Status
- `1` - New
- `10` - NeedRetry
- `100` - Success
- `110` - NotSuccessful
- `130` - Completed
- `150` - Unreachable
- `220` - Blacklisted
- `500` - Error

#### Call Status
- `3` - InProgress
- `4` - Completed
- `5` - Busy
- `6` - Failed
- `7` - NoAnswer
- `8` - Canceled

#### Activity Status
- `1` - Running
- `2` - Paused
- `3` - Suspended
- `10` - TemporaryMaintenance

## Migration Guide

### From V1 to V2

**Before (V1):**
```python
pearl.api_version = "v1"

# Get outbounds
outbounds = pearl.Outbound.get_all()

# Add lead
pearl.Outbound.add_lead(outbound_id, phone_number="+123...")

# Get analytics
analytics = pearl.Outbound.get_analytics(outbound_id, from_date, to_date)
```

**After (V2):**
```python
pearl.api_version = "v2"

# Get pearls (replaces outbounds/inbounds)
pearls = pearl.Pearl.get_all()

# Add lead (same method, different ID)
pearl.Outbound.add_lead(pearl_id, phone_number="+123...")

# Get analytics (use Pearl class)
analytics = pearl.Pearl.get_analytics(pearl_id, from_date, to_date)
```

### Key Changes

1. **Replace `outbound_id`/`inbound_id` with `pearl_id`**
2. **Use `Pearl` class** for analytics, calls, and pearl management
3. **Keep using `Outbound`** for lead operations (just change the ID)
4. **`Inbound` class** is V1-only, use `Pearl` in V2

## Error Handling

The wrapper provides clear error messages when using methods in the wrong version:

```python
pearl.api_version = "v2"
pearl.Inbound.get_all()
# ValueError: Inbound.get_all() is only available in API v1.
# In v2, use Pearl.get_all() instead.
```

## License

BSD 3-Clause License - see [LICENSE](LICENSE) file for details.

## Contact

- **Support**: [support@nlpearl.ai](mailto:support@nlpearl.ai)
- **Documentation**: This README
- **API Key**: Contact [support@nlpearl.ai](mailto:samuel@nlpearl.ai)

---

**Version**: 2.0.0
**Python**: 3.6+  
**API Versions**: V1 and V2 supported
