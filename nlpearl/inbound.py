import requests
import nlpearl  # To access the global api_key
from ._helpers import _process_date, _date_diff_in_days, _get_api_url


class Inbound:
    @classmethod
    def _get_version(cls):
        """Get current API version."""
        return getattr(nlpearl, 'api_version', 'v2')
    
    @classmethod
    def _check_v1_only(cls, method_name):
        """Raise error if method is V1-only but V2 is selected."""
        if cls._get_version() == "v2":
            raise ValueError(
                f"Inbound.{method_name}() is only available in API v1. "
                f"In v2, use Pearl.{method_name}() instead. "
                f"Current version is v2. Set pearl.api_version = 'v1' to use Inbound methods."
            )
    
    @classmethod
    def get_all(cls):
        """
        Get all inbounds.
        
        Available in: V1 only
        In V2: Use Pearl.get_all() instead
        """
        cls._check_v1_only("get_all")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set. Set it using 'pearl.api_key = YOUR_API_KEY'.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Inbound"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def get(cls, inbound_id):
        """
        Get a specific inbound by ID.
        
        Available in: V1 only
        In V2: Use Pearl.get(pearl_id) instead
        """
        cls._check_v1_only("get")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Inbound/{inbound_id}"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def set_active(cls, inbound_id, is_active):
        """
        Activate or deactivate an inbound.
        
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
        url = f"{_get_api_url()}/Inbound/{inbound_id}/Active"
        data = {"isActive": is_active}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    @classmethod
    def get_calls(cls, inbound_id, from_date, to_date, skip=0, limit=100, sort_prop=None, is_ascending=True,
                  tags=None, statuses=None, search_input=None):
        """
        Retrieves the calls within a specific date range for an inbound, with additional filters.
        
        Available in: V1 only
        In V2: Use Pearl.get_calls(pearl_id, ...) instead

        Parameters:
            inbound_id (str): The unique identifier of the inbound configuration.
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
            dict: JSON response from the API (includes error details if any).
        """
        cls._check_v1_only("get_calls")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        # Process the date values using the private helper function.
        from_date_str = _process_date(from_date)
        to_date_str = _process_date(to_date)

        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Inbound/{inbound_id}/Calls"
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
    def get_ongoing_calls(cls, inbound_id):
        """
        Retrieves the number of ongoing calls and the number of calls in queue for a specific inbound.
        
        Available in: V1 only
        In V2: Use Pearl.get_ongoing_calls(pearl_id) instead

        Parameters:
            inbound_id (str): The unique identifier of the inbound.

        Returns:
            dict: The response from the API with ongoing calls information.
        """
        cls._check_v1_only("get_ongoing_calls")
        
        if nlpearl.api_key is None:
            raise ValueError("API key is not set.")
        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Inbound/{inbound_id}/OngoingCalls"
        response = requests.get(url, headers=headers)
        return response.json()

    @classmethod
    def get_analytics(cls, inbound_id, from_date, to_date):
        """
        Retrieves analytics data for a specific inbound campaign within a given date range.
        The maximum allowed range is 90 days.
        
        Available in: V1 only
        In V2: Use Pearl.get_analytics(pearl_id, ...) instead

        Parameters:
            inbound_id (str): The unique identifier of the inbound campaign.
            from_date (str | datetime | date): Start date (inclusive).
            to_date (str | datetime | date): End date (inclusive).

        Returns:
            dict: Parsed JSON response.

        Raises:
            ValueError: If date range exceeds 90 days.
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

        url = f"{_get_api_url()}/Inbound/{inbound_id}/Analytics"
        data = {"from": from_str, "to": to_str}

        response = requests.post(url, headers=headers, json=data)
        return response.json()

