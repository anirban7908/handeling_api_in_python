import requests
from typing import Tuple, Dict


class RandomUserAPIError(Exception):
    """Custom exception for Random User API errors."""
    pass


def get_random_user(timeout: int = 5) -> Dict[str, str]:
    """
    Fetch a random user from the FreeAPI Random User endpoint.

    Args:
        timeout (int): Timeout in seconds for the HTTP request.

    Returns:
        dict: Dictionary with keys 'username', 'fullname', 'country'.

    Raises:
        RandomUserAPIError: If the API request fails or response is invalid.
    """
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad status codes
    except requests.exceptions.RequestException as e:
        raise RandomUserAPIError(f"Network error while fetching user: {e}")

    try:
        data_json = response.json()
    except ValueError as e:
        raise RandomUserAPIError(f"Failed to parse JSON: {e}")

    if not data_json.get('success') or 'data' not in data_json:
        raise RandomUserAPIError("API response missing 'success' or 'data' fields")

    user_data = data_json['data']
    username = user_data.get('login', {}).get('username', 'N/A')
    name_info = user_data.get('name', {})
    fullname = f"{name_info.get('title', '')}. {name_info.get('first', '')} {name_info.get('last', '')}".strip()
    country = user_data.get('location', {}).get('country', 'N/A')

    return {"username": username, "fullname": fullname, "country": country}


def main():
    try:
        user = get_random_user()
        print(f"Username: {user['username']}, Full Name: {user['fullname']}, Country: {user['country']}")
    except RandomUserAPIError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
