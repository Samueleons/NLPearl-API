import requests
import nlpearl  # To access the global api_key
from ._helpers import _process_date, _date_diff_in_days, _get_api_url


class Outbound:
    """
    Outbound class that automatically routes to V1 or V2 endpoints based on api_version.
    
    V1: Uses outbound_id
    V2: Uses pearl_id
    """
    
    @classmethod
    def _get_version(cls):
        """Get current API version."""
        return getattr(nlpearl, 'api_version', 'v2')
    
    @classmethod
    def _check_v1_only(cls, method_name):
        """Raise error if method is V1-only but V2 is selected."""
        if cls._get_version() == "v2":
            raise ValueError(
                f"{method_name}() is only available in API v1. "
                f"Current version is v2. Set pearl.api_version = 'v1' to use this method."
            )
    
    @classmethod
    def get_all(cls):
        """
        Get all outbounds.
        
        Available in: V1 only
        In V2: Use Pearl.get_all() instead
        """
        cls._check_v1_only("get_all")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def get(cls, outbound_id):
        """
        Get a specific outbound by ID.
        
        Available in: V1 only
        In V2: Use Pearl.get(pearl_id) instead
        """
        cls._check_v1_only("get")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound/{outbound_id}"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def set_active(cls, outbound_id, is_active):
        """
        Activate or deactivate an outbound.
        
        Available in: V1 only
        In V2: Use Pearl.set_active(pearl_id, is_active) instead
        """
        cls._check_v1_only("set_active")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{outbound_id}/Active"
        data = {"isActive": is_active}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_calls(cls, outbound_id, from_date, to_date, skip=0, limit=100, sort_prop=None, is_ascending=True,
                  tags=None):
        """
        Get calls for an outbound with optional filters.
        
        Available in: V1 only
        In V2: Use Pearl.get_calls(pearl_id, ...) instead
        
        Parameters:
            outbound_id (str): The unique identifier of the outbound.
            from_date: The start date for filtering (required; datetime/date object or ISO 8601 string).
            to_date: The end date for filtering (required; datetime/date object or ISO 8601 string).
            skip (int): Number of entries to skip for pagination.
            limit (int): Limit on the number of entries to return.
            sort_prop (str | None): Property name to sort by.
            is_ascending (bool): Whether the sort order is ascending.
            tags (list[str] | None): List of tags to filter by.

        Returns:
            dict: JSON response from the API (includes error details if any).
        """
        cls._check_v1_only("get_calls")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        # Process dates
        from_date_str = _process_date(from_date)
        to_date_str = _process_date(to_date)

        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{outbound_id}/Calls"
        data = {
            "skip": skip,
            "limit": limit,
            "isAscending": is_ascending,
            "fromDate": from_date_str,
            "toDate": to_date_str
        }
        if sort_prop:
            data["sortProp"] = sort_prop
        if tags:
            data["tags"] = tags

        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def add_lead(cls, id_param, phone_number, external_id=None, time_zone_id=None, call_data=None):
        """
        Add a lead to an outbound.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id

        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            phone_number (str): The phone number of the lead (required).
            external_id (str | None): An optional external identifier for the lead.
            time_zone_id (str | None): Optional time zone identifier for the lead.
            call_data (dict | None): Additional call data.

        Returns:
            dict: JSON response from the API.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        if not phone_number:
            raise ValueError("phone_number is required.")
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        
        version = cls._get_version()
        if version == "v1":
            url = f"{_get_api_url()}/Outbound/{id_param}/Lead"
            data = {"phoneNumber": phone_number}
            if external_id:
                data["externalId"] = external_id
            if time_zone_id:
                data["timeZoneId"] = time_zone_id
            if call_data:
                data["callData"] = call_data
            response = requests.put(url, headers=headers, json=data)
        else:  # v2
            url = f"{_get_api_url()}/Outbound/{id_param}/Lead"
            data = {"phoneNumber": phone_number}
            if external_id:
                data["externalId"] = external_id
            if time_zone_id:
                data["timeZoneId"] = time_zone_id
            if call_data:
                data["callData"] = call_data
            response = requests.post(url, headers=headers, json=data)
        
        return response.json()
    
    @classmethod
    def update_lead(cls, id_param, lead_id, phone_number=None, external_id=None, 
                    time_zone_id=None, call_data=None, status=None):
        """
        Updates the details of an existing lead.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id
        
        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            lead_id (str): The unique identifier of the lead to update.
            phone_number (str | None): The updated phone number of the lead.
            external_id (str | None): An updated external identifier for the lead.
            time_zone_id (str | None): Optional time zone identifier for the lead.
            call_data (dict | None): A dictionary containing additional lead information.
            status (int | None): The new status to assign to the lead.
                
        Returns:
            dict: JSON response with updated lead information.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{id_param}/Lead/{lead_id}"
        data = {}
        
        if phone_number is not None:
            data["phoneNumber"] = phone_number
        if external_id is not None:
            data["externalId"] = external_id
        if time_zone_id is not None:
            data["timeZoneId"] = time_zone_id
        if call_data is not None:
            data["callData"] = call_data
        if status is not None:
            data["status"] = status
            
        response = requests.put(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_leads(cls, id_param, skip=0, limit=100, sort_prop=None,
                  is_ascending=True, statuses=None, search_input=None, status=None):
        """
        Get leads for an outbound with optional filters.
        
        Available in: V1 and V2
        - V1: Uses outbound_id, supports 'status' parameter
        - V2: Uses pearl_id, supports 'statuses' parameter

        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            skip (int): Number of entries to skip for pagination.
            limit (int): Limit on the number of entries to return.
            sort_prop (str | None): Property name to sort by.
            is_ascending (bool): Whether the sort order is ascending.
            statuses (list[int] | None): List of status codes to filter by (V2).
            search_input (str | None): Text to filter by (V2).
            status (int | None): Filter leads by status (V1).

        Returns:
            dict: JSON response from the API.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{id_param}/Leads"
        data = {
            "skip": skip,
            "limit": limit,
            "isAscending": is_ascending,
        }
        if sort_prop:
            data["sortProp"] = sort_prop
        
        version = cls._get_version()
        if version == "v1":
            if status:
                data["status"] = status
        else:  # v2
            if statuses:
                data["statuses"] = statuses
            if search_input:
                data["searchInput"] = search_input
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_lead_by_id(cls, id_param, lead_id):
        """
        Get a specific lead by lead ID.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound/{id_param}/Lead/{lead_id}"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def get_lead_by_external_id(cls, id_param, external_id):
        """
        Get a lead by external ID.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound/{id_param}/Lead/External/{external_id}"
        response = requests.get(url, headers=headers)
        return response.json()
    
    @classmethod
    def get_lead_by_phone_number(cls, id_param, phone_number):
        """
        Get a lead by phone number.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id
        
        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            phone_number (str): The phone number of the lead to retrieve.
            
        Returns:
            dict: JSON response with lead information.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound/{id_param}/Lead/PhoneNumber/{phone_number}"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def make_call(cls, outbound_id, to, call_data=None):
        """
        Make a call in an outbound campaign.
        
        Available in: V1 only
        In V2: This functionality is handled differently
        """
        cls._check_v1_only("make_call")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{outbound_id}/Call"
        data = {"to": to}
        if call_data:
            data["callData"] = call_data
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_call_request(cls, request_id):
        """
        Get details of a specific call request.
        
        Available in: V1 only
        """
        cls._check_v1_only("get_call_request")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Outbound/CallRequest/{request_id}"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def get_call_requests(cls, outbound_id, from_date, to_date, skip=0, limit=100, sort_prop=None,
                          is_ascending=True):
        """
        Get call requests for an outbound with optional filters.
        
        Available in: V1 only

        Parameters:
            outbound_id (str): The unique identifier of the outbound.
            from_date: The start date for filtering (required; datetime/date or ISO 8601 string).
            to_date: The end date for filtering (required; datetime/date or ISO 8601 string).
            skip (int): Number of entries to skip for pagination.
            limit (int): Limit on the number of entries to return.
            sort_prop (str | None): Property name to sort by.
            is_ascending (bool): Whether the sort order is ascending.

        Returns:
            dict: JSON response from the API (including error details if any).
        """
        cls._check_v1_only("get_call_requests")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        from_date_str = _process_date(from_date)
        to_date_str = _process_date(to_date)
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{outbound_id}/CallRequest"
        data = {
            "skip": skip,
            "limit": limit,
            "isAscending": is_ascending,
            "fromDate": from_date_str,
            "toDate": to_date_str
        }
        if sort_prop:
            data["sortProp"] = sort_prop
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def delete_leads(cls, id_param, lead_ids):
        """
        Deletes one or more leads associated with a specific outbound campaign.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id

        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            lead_ids (list[str]): A list of lead IDs to be deleted.

        Returns:
            bool: True if deletion was successful.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")

        if not isinstance(lead_ids, list) or not lead_ids:
            raise ValueError("lead_ids must be a non-empty list of strings.")

        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{id_param}/Leads"
        data = {"leadIds": lead_ids}

        response = requests.delete(url, headers=headers, json=data)
        return response.json()
    
    @classmethod
    def delete_leads_by_external_id(cls, id_param, external_ids):
        """
        Deletes one or more leads by external ID.
        
        Available in: V1 and V2
        - V1: Uses outbound_id
        - V2: Uses pearl_id
        
        Parameters:
            id_param (str): The unique identifier (outbound_id in V1, pearl_id in V2).
            external_ids (list[str]): A list of external lead IDs to be deleted.
            
        Returns:
            bool: True if deletion was successful.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        if not isinstance(external_ids, list) or not external_ids:
            raise ValueError("external_ids must be a non-empty list of strings.")
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Outbound/{id_param}/Leads/External"
        data = {"leadExternalIds": external_ids}
        
        response = requests.delete(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_analytics(cls, outbound_id, from_date, to_date):
        """
        Retrieves analytics data for a specific outbound campaign within a given date range.
        The maximum allowed range is 90 days.
        
        Available in: V1 only
        In V2: Use Pearl.get_analytics(pearl_id, ...) instead

        Parameters:
            outbound_id (str): The unique identifier of the outbound campaign.
            from_date (str | datetime | date): Start date (inclusive).
            to_date (str | datetime | date): End date (inclusive).

        Returns:
            dict | str: Parsed JSON response or raw text if response is not JSON.

        Raises:
            ValueError: If the date range exceeds 90 days or API key is not set.
        """
        cls._check_v1_only("get_analytics")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")

        delta = _date_diff_in_days(from_date, to_date)
        if delta > 90:
            raise ValueError("Date range must not exceed 90 days.")

        from_str = _process_date(from_date)
        to_str = _process_date(to_date)

        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }

        url = f"{_get_api_url()}/Outbound/{outbound_id}/Analytics"
        data = {"from": from_str, "to": to_str}

        response = requests.post(url, headers=headers, json=data)
        return response.json()
