"""
Complete V1 API Usage Example
All available endpoints in API V1

To use this example:
1. Set your API key below
2. Uncomment the sections you want to test
3. Replace placeholder IDs with real ones from your account
"""
import nlpearl as pearl
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================
pearl.api_key = "your_api_key_here"  # <-- SET YOUR API KEY
pearl.api_version = "v1"

print("=" * 60)
print("NLPearl API V1 - Complete Usage Example")
print("=" * 60)
print(f"API Version: {pearl.api_version}")
print(f"API URL: https://api.nlpearl.ai/v1")
print("=" * 60)

# ============================================================
# 1. ACCOUNT
# ============================================================
print("\n### 1. ACCOUNT ###")
print("-" * 60)

# Get Account Information
print("\n[1.1] Get Account")
try:
    account_info = pearl.Account.get_account()
    print(f"[OK] Account Name: {account_info['name']}")
    print(f"[OK] Credit Balance: {account_info['creditBalance']}")
    print(f"[OK] Total Agents: {account_info['totalAgents']}")
    print(f"[OK] Status: {account_info['status']}")
except Exception as e:
    print(f"[ERROR] {e}")

# ============================================================
# 2. CALL OPERATIONS
# ============================================================
print("\n### 2. CALL OPERATIONS ###")
print("-" * 60)

# Get Call Information
print("\n[2.1] Get Call")
# call_id = "your_call_id_here"  # <-- REPLACE WITH REAL CALL ID
# try:
#     call_info = pearl.Call.get_call(call_id)
#     print(f"[OK] Call ID: {call_info['id']}")
#     print(f"[OK] Status: {call_info['status']}")
#     print(f"[OK] Duration: {call_info['duration']} seconds")
#     print(f"[OK] From: {call_info['from']}")
#     print(f"[OK] To: {call_info['to']}")
#     print(f"[OK] Conversation Status: {call_info['conversationStatus']}")
#     if call_info.get('tags'):
#         print(f"[OK] Tags: {', '.join(call_info['tags'])}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set call_id to test")

# Delete Calls
print("\n[2.2] Delete Calls")
# call_ids = ["call_id_1", "call_id_2"]  # <-- REPLACE WITH REAL CALL IDs
# try:
#     result = pearl.Call.delete_calls(call_ids)
#     print(f"[OK] Calls deleted: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set call_ids to test")

# ============================================================
# 3. INBOUND OPERATIONS
# ============================================================
print("\n### 3. INBOUND OPERATIONS ###")
print("-" * 60)

# Get All Inbounds
print("\n[3.1] Get All Inbounds")
try:
    inbounds = pearl.Inbound.get_all()
    print(f"[OK] Total Inbounds: {len(inbounds)}")
    for inbound in inbounds:
        print(f"  - {inbound['name']} (ID: {inbound['id']}, Status: {inbound['status']})")
except Exception as e:
    print(f"[ERROR] Error: {e}")

# Get Specific Inbound
print("\n[3.2] Get Specific Inbound")
# inbound_id = "your_inbound_id"  # <-- REPLACE WITH REAL INBOUND ID
# try:
#     inbound = pearl.Inbound.get(inbound_id)
#     print(f"[OK] Name: {inbound['name']}")
#     print(f"[OK] Status: {inbound['status']}")
#     print(f"[OK] Phone Number: {inbound.get('phoneNumber', 'N/A')}")
#     print(f"[OK] Total Agents: {inbound['totalAgents']}")
#     print(f"[OK] Today's Calls: {inbound.get('totalTodayCalls', 0)}")
#     print(f"[OK] Ongoing Calls: {inbound.get('totalOngoingCalls', 0)}")
#     print(f"[OK] Calls in Queue: {inbound.get('totalOnQueue', 0)}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set inbound_id to test")

# Set Inbound Active Status
print("\n[3.3] Set Inbound Active/Inactive")
# inbound_id = "your_inbound_id"  # <-- REPLACE WITH REAL INBOUND ID
# try:
#     # Activate
#     status = pearl.Inbound.set_active(inbound_id, is_active=True)
#     print(f"[OK] Activated: Status = {status}")
#     
#     # Deactivate
#     status = pearl.Inbound.set_active(inbound_id, is_active=False)
#     print(f"[OK] Deactivated: Status = {status}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set inbound_id to test")

# Get Ongoing Calls
print("\n[3.4] Get Inbound Ongoing Calls")
# inbound_id = "your_inbound_id"  # <-- REPLACE WITH REAL INBOUND ID
# try:
#     ongoing = pearl.Inbound.get_ongoing_calls(inbound_id)
#     print(f"[OK] Ongoing Calls: {ongoing['totalOngoingCalls']}")
#     print(f"[OK] Calls in Queue: {ongoing.get('totalOnQueue', 0)}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set inbound_id to test")

# Search Calls
print("\n[3.5] Search Inbound Calls")
# inbound_id = "your_inbound_id"  # <-- REPLACE WITH REAL INBOUND ID
# try:
#     calls = pearl.Inbound.get_calls(
#         inbound_id,
#         from_date=datetime(2024, 1, 1),
#         to_date=datetime(2024, 1, 31),
#         skip=0,
#         limit=10,
#         sort_prop="startTime",
#         is_ascending=False,
#         tags=["important"],  # Optional
#         statuses=[100, 130],  # Optional: 100=Success, 130=Completed
#         search_input="test"  # Optional
#     )
#     print(f"[OK] Total Calls Found: {calls['count']}")
#     for call in calls.get('results', [])[:5]:
#         print(f"  - Call {call['id']}: Status={call['status']}, Duration={call['duration']}s")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set inbound_id to test")

# Get Analytics
print("\n[3.6] Get Inbound Analytics")
# inbound_id = "your_inbound_id"  # <-- REPLACE WITH REAL INBOUND ID
# try:
#     analytics = pearl.Inbound.get_analytics(
#         inbound_id,
#         from_date="2024-01-01T00:00:00.000Z",
#         to_date="2024-01-31T23:59:59.999Z"
#     )
#     overview = analytics['callsStatusOverview']
#     print(f"[OK] Total Calls: {overview['totalCalls']}")
#     print(f"[OK] Successful: {overview['successful']}")
#     print(f"[OK] Unsuccessful: {overview['unsuccessful']}")
#     print(f"[OK] Need Retry: {overview['needRetry']}")
#     print(f"[OK] Completed: {overview['completed']}")
#     
#     sentiment = analytics['callsSentimentOverview']
#     print(f"[OK] Sentiment - Positive: {sentiment['positive']}, Negative: {sentiment['negative']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set inbound_id to test")

# ============================================================
# 4. OUTBOUND OPERATIONS
# ============================================================
print("\n### 4. OUTBOUND OPERATIONS ###")
print("-" * 60)

# Get All Outbounds
print("\n[4.1] Get All Outbounds")
try:
    outbounds = pearl.Outbound.get_all()
    print(f"[OK] Total Outbounds: {len(outbounds)}")
    for outbound in outbounds:
        print(f"  - {outbound['name']} (ID: {outbound['id']}, Status: {outbound['status']})")
        print(f"    Total Leads: {outbound['totalLeads']}")
except Exception as e:
    print(f"[ERROR] Error: {e}")

# Get Specific Outbound
print("\n[4.2] Get Specific Outbound")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     outbound = pearl.Outbound.get(outbound_id)
#     print(f"[OK] Name: {outbound['name']}")
#     print(f"[OK] Status: {outbound['status']}")
#     print(f"[OK] Phone Number: {outbound.get('phoneNumber', 'N/A')}")
#     print(f"[OK] Total Leads: {outbound['totalLeads']}")
#     print(f"[OK] Completed Leads: {outbound.get('totalLeadsCompleted', 0)}")
#     print(f"[OK] Successful Leads: {outbound.get('totalLeadsSuccess', 0)}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Set Outbound Active Status
print("\n[4.3] Set Outbound Active/Inactive")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     # Activate
#     status = pearl.Outbound.set_active(outbound_id, is_active=True)
#     print(f"[OK] Activated: Status = {status}")
#     
#     # Deactivate
#     status = pearl.Outbound.set_active(outbound_id, is_active=False)
#     print(f"[OK] Deactivated: Status = {status}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Get Outbound Calls
print("\n[4.4] Get Outbound Calls")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     calls = pearl.Outbound.get_calls(
#         outbound_id,
#         from_date=datetime(2024, 1, 1),
#         to_date=datetime(2024, 1, 31),
#         skip=0,
#         limit=10,
#         sort_prop="startTime",
#         is_ascending=False,
#         tags=["important"]  # Optional
#     )
#     print(f"[OK] Total Calls Found: {calls['count']}")
#     for call in calls.get('results', [])[:5]:
#         print(f"  - Call {call['id']}: Status={call['status']}, Duration={call['duration']}s")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Get Outbound Analytics
print("\n[4.5] Get Outbound Analytics")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     analytics = pearl.Outbound.get_analytics(
#         outbound_id,
#         from_date="2024-01-01T00:00:00.000Z",
#         to_date="2024-01-31T23:59:59.999Z"
#     )
#     overview = analytics['callsStatusOverview']
#     print(f"[OK] Total Calls: {overview['totalCalls']}")
#     print(f"[OK] Total Leads: {overview['totalLeads']}")
#     print(f"[OK] Successful: {overview['successful']}")
#     print(f"[OK] Need Retry: {overview['needRetry']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# ============================================================
# 5. LEAD MANAGEMENT
# ============================================================
print("\n### 5. LEAD MANAGEMENT ###")
print("-" * 60)

# Add Lead
print("\n[5.1] Add Lead")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     new_lead = pearl.Outbound.add_lead(
#         outbound_id,
#         phone_number="+1234567890",
#         external_id="ext_test_123",
#         time_zone_id="Pacific Standard Time",
#         call_data={
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "john.doe@example.com",
#             "company": "Test Corp"
#         }
#     )
#     print(f"[OK] Lead Created: {new_lead}")
#     lead_id = new_lead.get('leadId')
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Get Lead by ID
print("\n[5.2] Get Lead by ID")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# lead_id = "your_lead_id"  # <-- REPLACE WITH REAL LEAD ID
# try:
#     lead = pearl.Outbound.get_lead_by_id(outbound_id, lead_id)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] External ID: {lead.get('externalId', 'N/A')}")
#     print(f"[OK] Status: {lead['status']}")
#     print(f"[OK] Call Data: {lead.get('callData', {})}")
#     print(f"[OK] Collected Data: {lead.get('collectedData', {})}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and lead_id to test")

# Get Lead by External ID
print("\n[5.3] Get Lead by External ID")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# external_id = "ext_test_123"  # <-- REPLACE WITH REAL EXTERNAL ID
# try:
#     lead = pearl.Outbound.get_lead_by_external_id(outbound_id, external_id)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] Status: {lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and external_id to test")

# Get Lead by Phone Number
print("\n[5.4] Get Lead by Phone Number")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# phone_number = "+1234567890"  # <-- REPLACE WITH REAL PHONE NUMBER
# try:
#     lead = pearl.Outbound.get_lead_by_phone_number(outbound_id, phone_number)
#     print(f"[OK] Lead ID: {lead['id']}")
#     print(f"[OK] Phone Number: {lead['phoneNumber']}")
#     print(f"[OK] Status: {lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and phone_number to test")

# Update Lead
print("\n[5.5] Update Lead")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# lead_id = "your_lead_id"  # <-- REPLACE WITH REAL LEAD ID
# try:
#     updated_lead = pearl.Outbound.update_lead(
#         outbound_id,
#         lead_id,
#         phone_number="+9876543210",  # Optional
#         external_id="updated_ext_id",  # Optional
#         status=100,  # Optional: 100=Success
#         call_data={"notes": "Updated lead", "preferredContact": "evening"}  # Optional
#     )
#     print(f"[OK] Lead Updated: {updated_lead['id']}")
#     print(f"[OK] New Status: {updated_lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and lead_id to test")

# Search Leads
print("\n[5.6] Search Leads")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     leads = pearl.Outbound.get_leads(
#         outbound_id,
#         skip=0,
#         limit=10,
#         sort_prop="created",
#         is_ascending=False,
#         status=1  # Optional: 1=New, 10=NeedRetry, 100=Success, 130=Completed
#     )
#     print(f"[OK] Total Leads Found: {leads['count']}")
#     for lead in leads.get('results', [])[:5]:
#         print(f"  - Lead {lead['id']}: Phone={lead['phoneNumber']}, Status={lead['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Delete Leads
print("\n[5.7] Delete Leads")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# lead_ids = ["lead_id_1", "lead_id_2"]  # <-- REPLACE WITH REAL LEAD IDs
# try:
#     result = pearl.Outbound.delete_leads(outbound_id, lead_ids)
#     print(f"[OK] Leads Deleted: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and lead_ids to test")

# Delete Leads by External ID
print("\n[5.8] Delete Leads by External ID")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# external_ids = ["ext_id_1", "ext_id_2"]  # <-- REPLACE WITH REAL EXTERNAL IDs
# try:
#     result = pearl.Outbound.delete_leads_by_external_id(outbound_id, external_ids)
#     print(f"[OK] Leads Deleted: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id and external_ids to test")

# ============================================================
# 6. OUTBOUND CALLING (V1 ONLY)
# ============================================================
print("\n### 6. OUTBOUND CALLING (V1 ONLY) ###")
print("-" * 60)

# Make Call
print("\n[6.1] Make Call")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     result = pearl.Outbound.make_call(
#         outbound_id,
#         to="+1234567890",
#         call_data={"firstName": "Jane", "urgency": "high"}
#     )
#     print(f"[OK] Call Initiated: {result['id']}")
#     print(f"[OK] From: {result['from']}")
#     print(f"[OK] To: {result['to']}")
#     print(f"[OK] Queue Position: {result['queuePosition']}")
#     request_id = result['id']
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# Get Call Request
print("\n[6.2] Get Call Request")
# request_id = "your_request_id"  # <-- REPLACE WITH REAL REQUEST ID
# try:
#     request = pearl.Outbound.get_call_request(request_id)
#     print(f"[OK] Request ID: {request['id']}")
#     print(f"[OK] Status: {request['status']}")
#     print(f"[OK] Outbound ID: {request['outboundId']}")
#     print(f"[OK] Created: {request['created']}")
#     if request.get('callId'):
#         print(f"[OK] Call ID: {request['callId']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set request_id to test")

# Search Call Requests
print("\n[6.3] Search Call Requests")
# outbound_id = "your_outbound_id"  # <-- REPLACE WITH REAL OUTBOUND ID
# try:
#     requests = pearl.Outbound.get_call_requests(
#         outbound_id,
#         from_date=datetime(2024, 1, 1),
#         to_date=datetime(2024, 1, 31),
#         skip=0,
#         limit=10,
#         sort_prop="created",
#         is_ascending=False
#     )
#     print(f"[OK] Total Requests Found: {requests['count']}")
#     for req in requests.get('results', [])[:5]:
#         print(f"  - Request {req['id']}: Status={req['status']}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set outbound_id to test")

# ============================================================
# 7. PEARL / MEMORY MANAGEMENT
# ============================================================
print("\n### 7. PEARL / MEMORY MANAGEMENT ###")
print("-" * 60)

# Reset Customer Memory
print("\n[7.1] Reset Customer Memory")
# pearl_id = "your_pearl_id"  # <-- REPLACE WITH REAL PEARL ID
# phone_number = "+1234567890"  # <-- REPLACE WITH REAL PHONE NUMBER
# try:
#     result = pearl.Pearl.reset_customer_memory(pearl_id, phone_number)
#     print(f"[OK] Memory Reset: {result}")
# except Exception as e:
#     print(f"[ERROR] Error: {e}")
print(">> Uncomment code above and set pearl_id and phone_number to test")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("V1 API Testing Complete!")
print("=" * 60)
print("\nEndpoints Tested:")
print("  1. Account: get_account()")
print("  2. Call: get_call(), delete_calls()")
print("  3. Inbound: get_all(), get(), set_active(), get_calls(),")
print("              get_ongoing_calls(), get_analytics()")
print("  4. Outbound: get_all(), get(), set_active(), get_calls(),")
print("               get_analytics()")
print("  5. Leads: add_lead(), get_lead_by_id(), get_lead_by_external_id(),")
print("            get_lead_by_phone_number(), update_lead(), get_leads(),")
print("            delete_leads(), delete_leads_by_external_id()")
print("  6. Calling: make_call(), get_call_request(), get_call_requests()")
print("  7. Memory: reset_customer_memory()")
print("\nTotal: 24+ endpoints")
print("=" * 60)
