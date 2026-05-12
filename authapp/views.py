from django.shortcuts import render, redirect
import requests
from qr_menu.settings import CLIENT_ID, CLIENT_SECRET
def google_auth(request):
    url = ("https://accounts.google.com/o/oauth2/v2/auth"
           f"?client_id={CLIENT_ID}"
           "&redirect_uri=https://qrmenu.onrender.com/auth/google/callback"
           "&response_type=code"
           "&scope=openid email profile")
    return redirect(url)


def google_callback(request):
    code = request.GET.get('code')
    token_url = 'https://www.googleapis.com/oauth2/v1/token'
    data = {'code': code,
            'token_url': token_url,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code'}
    token_response = request.post(token_url, data=data)
    tokens = token_response.json()
    access_token = tokens.get('access_token')
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo",
                             headers={"Authorization": f"Bearer: {access_token}"}).json()
    return render(request, 'login_success.html', {'user_info': user_info})
