import requests

def get_ramdon_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data_json = response.json()
    if data_json['success'] and "data" in data_json:
        user_data = data_json['data']
        user_name = user_data['login']['username']
        user_fullname = f"{user_data['name']['title']}. {user_data['name']['first']} {user_data['name']['last']}"
        user_country = user_data['location']['country']
        print(user_name, user_fullname, user_country)
        return user_name, user_fullname, user_country
    else:
        raise Exception ('Failed to fetch user')


def main():
    try:
        user_name, user_fullname, user_country = get_ramdon_user()
        print(f"user_name: {user_name}, user_fullname: {user_fullname}, user_country: {user_country}")
    except Exception as e:
        print(f"Exception: {str(e)}")

if __name__ == "__main__":
    main()