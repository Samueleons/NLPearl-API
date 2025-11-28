# call.py
import requests
import nlpearl
from ._helpers import _get_api_url


class Call:
    @classmethod
    def get_call(cls, call_id):
        """
        Retrieves all the information about a call.
        
        Parameters:
            call_id (str): The unique identifier of the call.
            
        Returns:
            dict: JSON response with call information.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set. Set the api_key first using 'pearl.api_key = YOUR_API_KEY'")

        headers = {"Authorization": f"Bearer {nlpearl.api_key}"}
        url = f"{_get_api_url()}/Call/{call_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    @classmethod
    def delete_calls(cls, call_ids):
        """
        Deletes one or more calls.
        
        Parameters:
            call_ids (list[str]): List of unique call IDs to delete.
            
        Returns:
            bool: True if deletion was successful.
        """
        if nlpearl.api_key is None:
            raise ValueError("API key is not set. Set the api_key first using 'pearl.api_key = YOUR_API_KEY'")
        
        if not isinstance(call_ids, list) or not call_ids:
            raise ValueError("call_ids must be a non-empty list of strings.")
        
        headers = {
            "Authorization": f"Bearer {nlpearl.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{_get_api_url()}/Call"
        data = {"callIds": call_ids}
        
        response = requests.delete(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
