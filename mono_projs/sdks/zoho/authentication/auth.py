""" 
    module for logging in zoho account through customer proxy 

"""


import requests, json
import dill as pickel
import os
from conf.defaults.defaults import ZOHO_STORE





def log_error(response, log):


    if response.status_code > 400:

        log.error(f"zoho_error_registered {response.content}")


    return response




def pickel_login(django_zoho_obj, log):


    creds = django_zoho_obj

    SESSION = requests.Session()

    password = json.dumps({'passwordauth':{'password':creds.zoho_user_pwd}})

    log_error(SESSION.get(f"https://inventory.zoho{creds.zoho_org_domain}"))

    accounts = log_error(SESSION.get(f'https://accounts.zoho{creds.zoho_org_domain}/signin?servicename=ZohoInventory&signupurl=https://www.zoho{creds.zoho_org_domain}/inventory/signup&serviceurl=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}%2Fapp%2F{creds.zoho_org_id}'))
    cookies = accounts.cookies.get_dict()


    SESSION.headers = {'Accept': '*/*',
                    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Host': 'accounts.zoho.in',
                    'Origin': f'https://accounts.zoho{creds.zoho_org_domain}',
                    'Referer': f'https://accounts.zoho{creds.zoho_org_domain}/signin?servicename=ZohoInventory&signupurl=https://www.zoho{creds.zoho_org_domain}/inventory/signup&serviceurl=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}%2Fapp%2F{creds.zoho_org_id}',
                    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
                    'X-ZCSRF-TOKEN': f'iamcsrcoo={cookies["iamcsr"]}'}

    getUser = log_error(SESSION.post(f"https://accounts.zoho{creds.zoho_org_domain}/signin/v2/lookup/{creds.zoho_user_name}", data=f'mode=primary&cli_time={int(time.time())}&servicename=ZohoInventory&serviceurl=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}%2Fapp%2F{creds.zoho_org_id}&signupurl=https%3A%2F%2Fwww.zoho{creds.zoho_org_domain}%2Finventory%2Fsignup'))

    user = getUser.json()

    pwdUser = log_error(SESSION.post(f'https://accounts.zoho{creds.zoho_org_domain}/signin/v2/primary/{user["lookup"]["identifier"]}/password?digest={user["lookup"]["digest"]}&cli_time={int(time.time())}&servicename=ZohoInventory&serviceurl=https%3A%2F%2Finventory.zoho{creds.zoho_org_domain}%2Fapp%2F{creds.zoho_org_id}&signupurl=https%3A%2F%2Fwww.zoho{creds.zoho_org_domain}%2Finventory%2Fsignup', data=password))

    SESSION.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Host': f'inventory.zoho{creds.zoho_org_domain}',
                        'Referer': f'https://accounts.zoho{creds.zoho_org_domain}/',
                        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    
    
    
    
    with open(os.path.join(ZOHO_STORE, f"{creds.zoho_user_name}.pkl"), 'wb') as f:

        pickel.dump(SESSION, f)

















    