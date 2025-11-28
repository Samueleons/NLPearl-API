import requests
import nlpearl  # To access the global api_key
from ._helpers import _get_api_url, _process_date, _date_diff_in_days


class Pearl:
    @classmethod
    def _get_version(cls):
        """Get current API version."""
        return getattr(nlpearl, 'api_version', 'v2')
    
    @classmethod
    def _check_v2_only(cls, method_name):
        """Raise error if method is V2-only but V1 is selected."""
        if cls._get_version() == "v1":
            raise ValueError(
                f"{method_name}() is only available in API v2. "
                f"Current version is v1. Set pearl.api_version = 'v2' to use this method."
            )
    
    @classmethod
    def reset_customer_memory(cls, pearl_id, phone_number):
        """
        Resets stored memory associated with a specific customer's phone number for a given Pearl.
        
        Note: In API v2, use reset_memory() instead.

        Parameters:
            pearl_id (str): The unique identifier of the Pearl whose memory should be reset.
            phone_number (str): The phone number associated with the customer whose memory should be reset.

        Returns:
            The response from the API.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set. Set it using 'pearl.api_key = YOUR_API_KEY'.")

        if not phone_number.startswith("+"):
            phone_number = f"+{phone_number}"

        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        
        # V1 uses URL parameter, V2 uses request body
        api_version = getattr(nlpearl, 'api_version', 'v2')
        if api_version == "v1":
            url = f"{_get_api_url()}/Pearl/{pearl_id}/Memory/{phone_number}/Reset"
            response = requests.put(url, headers=headers)
        else:  # v2
            url = f"{_get_api_url()}/Pearl/{pearl_id}/ResetMemory"
            data = {"phoneNumber": phone_number}
            response = requests.put(url, headers=headers, json=data)
        
        try:
            return response.json()
        except ValueError:
            return response.text
    
    @classmethod
    def reset_memory(cls, pearl_id, phone_number):
        """
        Resets stored memory associated with a specific customer's phone number for a given Pearl.
        
        This is the V2 API method. For V1 compatibility, use reset_customer_memory().

        Parameters:
            pearl_id (str): The unique identifier of the Pearl whose memory should be reset.
            phone_number (str): The phone number associated with the customer whose memory should be reset.

        Returns:
            bool: True if memory reset was successful.
        """
        return cls.reset_customer_memory(pearl_id, phone_number)
    
    @classmethod
    def get_all(cls):
        """
        Retrieves all Pearls.
        
        Available in: V2 only
        
        Returns:
            list: List of all pearls for the client.
        """
        cls._check_v2_only("get_all")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Pearl"
        response = requests.get(url, headers=headers)
        return response.json()
    
    @classmethod
    def get(cls, pearl_id):
        """
        Retrieves a specific Pearl by its ID.
        
        Available in: V2 only
        
        Parameters:
            pearl_id (str): The unique identifier of the Pearl.
            
        Returns:
            dict: Details of the specific Pearl.
        """
        cls._check_v2_only("get")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Pearl/{pearl_id}"
        response = requests.get(url, headers=headers)
        return response.json()
    
    @classmethod
    def set_active(cls, pearl_id, is_active):
        """
        Activates or deactivates a specified Pearl.
        
        Available in: V2 only
        
        Parameters:
            pearl_id (str): The unique identifier of the Pearl.
            is_active (bool): True to activate, False to deactivate.
            
        Returns:
            int: The active state of the Pearl (eActivityStatus).
        """
        cls._check_v2_only("set_active")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Pearl/{pearl_id}/Active"
        data = {"isActive": is_active}
        response = requests.put(url, headers=headers, json=data)
        return response.json()
    
    @classmethod
    def get_calls(cls, pearl_id, from_date, to_date, skip=0, limit=100, sort_prop=None, 
                  is_ascending=True, tags=None, statuses=None, search_input=None):
        """
        Retrieves the calls within a specific date range for a Pearl.
        
        Available in: V2 only
        
        Parameters:
            pearl_id (str): The unique identifier of the Pearl.
            from_date: The start date for filtering (required; datetime/date object or ISO 8601 string).
            to_date: The end date for filtering (required; datetime/date object or ISO 8601 string).
            skip (int): Number of entries to skip for pagination.
            limit (int): Limit on the number of entries to return.
            sort_prop (str | None): Property name to sort by.
            is_ascending (bool): Whether the sort order is ascending.
            tags (list[str] | None): List of tags to filter by.
            statuses (list[int] | None): List of status codes to filter by.
            search_input (str | None): Text to filter by.
            
        Returns:
            dict: JSON response with calls data.
        """
        cls._check_v2_only("get_calls")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        from_date_str = _process_date(from_date)
        to_date_str = _process_date(to_date)
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Pearl/{pearl_id}/Calls"
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
        if statuses:
            data["statuses"] = statuses
        if search_input:
            data["searchInput"] = search_input
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    @classmethod
    def get_ongoing_calls(cls, pearl_id):
        """
        Returns the number of active calls currently in progress for the specified Pearl.
        If the Pearl has inbound configurations, it also returns the number of calls in queue.
        
        Available in: V2 only
        
        Parameters:
            pearl_id (str): The unique identifier of the Pearl.
            
        Returns:
            dict: JSON response with ongoing calls information.
        """
        cls._check_v2_only("get_ongoing_calls")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Pearl/{pearl_id}/OngoingCalls"
        response = requests.get(url, headers=headers)
        return response.json()
    
    @classmethod
    def get_analytics(cls, pearl_id, from_date, to_date):
        """
        Retrieves analytics data for a specific Pearl within a given date range.
        The maximum allowed range is 90 days.
        
        Available in: V2 only
        
        Parameters:
            pearl_id (str): The unique identifier of the Pearl.
            from_date (str | datetime | date): Start date (inclusive).
            to_date (str | datetime | date): End date (inclusive).
            
        Returns:
            dict: Parsed JSON response with analytics data.
            
        Raises:
            ValueError: If date range exceeds 90 days.
        """
        cls._check_v2_only("get_analytics")
        
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
        
        url = f"{_get_api_url()}/Pearl/{pearl_id}/Analytics"
        data = {"from": from_str, "to": to_str}
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()