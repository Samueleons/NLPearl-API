# NLPearl Python Wrapper - Final Implementation

## ✅ Implementation Complete

Date: November 28, 2025  
Version: 1.0.7  
Default API Version: V2

---

## 🎯 What You Requested

✅ **Unified API** - Same class names for V1 and V2  
✅ **Automatic routing** - Set version once, methods route automatically  
✅ **Clear errors** - Methods that don't exist in selected version raise helpful errors  
✅ **No separate V2 classes** - Just use `pearl.Outbound`, not `pearl.OutboundV2`  
✅ **All documentation in English** - No French in customer-facing code  

---

## 📦 Package Structure

```
nlpearl/
├── __init__.py          # Exports: Account, Call, Inbound, Outbound, Pearl
├── _helpers.py          # _get_api_url(), _process_date(), etc.
├── account.py           # Account.get_account()
├── call.py              # Call operations
├── inbound.py           # Inbound operations (V1 only)
├── outbound.py          # Outbound operations (unified V1/V2)
└── pearl.py             # Pearl operations
```

---

## 🚀 Usage

### Set Version Once
```python
import nlpearl as pearl

pearl.api_key = "your_key"
pearl.api_version = "v2"  # Default
```

### Use Same Class Names

**V2 (Default):**
```python
pearl.api_version = "v2"

# Pearl operations
pearls = pearl.Pearl.get_all()
analytics = pearl.Pearl.get_analytics(pearl_id, from_date, to_date)

# Lead operations (same class name!)
pearl.Outbound.add_lead(pearl_id, phone_number="+123...")
lead = pearl.Outbound.get_lead_by_id(pearl_id, lead_id)
```

**V1:**
```python
pearl.api_version = "v1"

# Inbound/Outbound operations
inbounds = pearl.Inbound.get_all()
outbounds = pearl.Outbound.get_all()

# Lead operations (same class name!)
pearl.Outbound.add_lead(outbound_id, phone_number="+123...")
lead = pearl.Outbound.get_lead_by_id(outbound_id, lead_id)
```

---

## 📚 Documentation Files

### For Users
- **`README.md`** - Complete guide in English
- **`example_v1_usage.py`** - All 26 V1 endpoints with examples
- **`example_v2_usage.py`** - All 19 V2 endpoints with examples
- **`TESTING_GUIDE.md`** - How to test the examples
- **`API_REFERENCE.md`** - Quick reference for all methods

### For Developers
- **`test_version.py`** - Version selection tests
- **`test_unified_api.py`** - Unified API tests
- **`UNIFIED_API_SUMMARY.md`** - Technical implementation details

---

## 🧪 Testing

### Run Tests
```bash
python test_version.py
python test_unified_api.py
```

### Test Examples
```bash
# Set your API key in the file first
python example_v1_usage.py
python example_v2_usage.py
```

**All tests pass:** ✅

---

## 📊 Complete Endpoint List

### V1 API (26 Endpoints)

**Account (1)**
- get_account()

**Call (2)**
- get_call()
- delete_calls()

**Inbound (6)**
- get_all()
- get()
- set_active()
- get_ongoing_calls()
- get_calls()
- get_analytics()

**Outbound (5)**
- get_all()
- get()
- set_active()
- get_calls()
- get_analytics()

**Lead Management (8)**
- add_lead()
- update_lead()
- get_lead_by_id()
- get_lead_by_external_id()
- get_lead_by_phone_number()
- get_leads()
- delete_leads()
- delete_leads_by_external_id()

**Outbound Calling (3)**
- make_call()
- get_call_request()
- get_call_requests()

**Memory (1)**
- reset_customer_memory()

### V2 API (19 Endpoints)

**Account (1)**
- get_account()

**Call (2)**
- get_call()
- delete_calls()

**Pearl (6)**
- get_all()
- get()
- set_active()
- get_ongoing_calls()
- get_calls()
- get_analytics()

**Lead Management (8)**
- add_lead() (uses pearl_id)
- update_lead()
- get_lead_by_id()
- get_lead_by_external_id()
- get_lead_by_phone_number()
- get_leads()
- delete_leads()
- delete_leads_by_external_id()

**Memory (2)**
- reset_memory()
- reset_customer_memory()

---

## 🔑 Key Differences V1 vs V2

| Aspect | V1 | V2 |
|--------|----|----|
| **Default** | No | **Yes** |
| **Structure** | Separate Inbound/Outbound | Unified Pearl |
| **ID Parameter** | `outbound_id`, `inbound_id` | `pearl_id` |
| **Get All** | `Inbound.get_all()`, `Outbound.get_all()` | `Pearl.get_all()` |
| **Analytics** | `Outbound.get_analytics()` | `Pearl.get_analytics()` |
| **Lead Add** | `Outbound.add_lead(outbound_id, ...)` | `Outbound.add_lead(pearl_id, ...)` |
| **Lead Search** | Uses `status` (single) | Uses `statuses` (list) |
| **Add Lead HTTP** | PUT | POST |

---

## 🎓 How to Use

### Step 1: Install
```bash
pip install nlpearl
```

### Step 2: Configure
```python
import nlpearl as pearl
pearl.api_key = "your_key"
pearl.api_version = "v2"  # or "v1"
```

### Step 3: Make Calls
```python
# V2
pearls = pearl.Pearl.get_all()
pearl.Outbound.add_lead(pearl_id, phone_number="+123...")

# V1
outbounds = pearl.Outbound.get_all()
pearl.Outbound.add_lead(outbound_id, phone_number="+123...")
```

---

## ⚠️ Important Notes

1. **Default is V2** - If you want V1, set `pearl.api_version = "v1"`
2. **ID parameters change** - `outbound_id` in V1, `pearl_id` in V2
3. **Inbound class** - Only works in V1, use `Pearl` in V2
4. **Clear error messages** - You'll know if you use wrong version

---

## 📞 Support

- Email: support@nlpearl.ai
- API Key: samuel@nlpearl.ai
- Documentation: README.md

---

## ✨ Ready for Production

- ✅ Full V1 support
- ✅ Full V2 support
- ✅ Unified API
- ✅ All endpoints implemented
- ✅ Comprehensive examples
- ✅ Complete documentation
- ✅ All tests passing
- ✅ English only

**Package is ready to use!** 🎉

