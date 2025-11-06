import requests

API_URL = "http://16.170.255.189:3000/api/project.all"
api_key = "fLTiFwuMatdRriuqNaSYpMKlPxQjwJeTXJiBQsLbaKigcMCDMTMetxReZarvPkVj"
app_name = "job-portal-frontend-qsflic"
 
def get_application_id():
    """Fetch Application ID"""
    headers = {
        "accept": "application/json",
        "x-api-key": api_key,
    }
    try:
        req = requests.get(API_URL, headers=headers, timeout=30)
        req.raise_for_status()
        data = req.json()

        # Find application by name
        for project in data or []:
            environments = project.get("environments", [])
            for env in environments:
                applications = env.get("applications", [])
                for app in applications:
                    if app.get("appName") == app_name:
                        application_id = app.get("applicationId")
                        print(f"Found applicationId: {application_id} - dockploy.py:26")
                        return application_id

        print(f"No application found with name: {app_name} - dockploy.py:29")
        return None

    except requests.RequestException as e:
        print(f"Error fetching application ID: {e} - dockploy.py:33")
        return None

# Call the function
get_application_id()
