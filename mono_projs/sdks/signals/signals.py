import requests, sys, os, json, logging
from pathlib import Path
SUPER_BASE = Path(__file__).parent.parent.parent


with open(os.path.join(SUPER_BASE, 'conf', 'servers', 'server.json'), 'r') as f:

    SERVER = json.load(f)




def send_bpn_signal(key, user, message, log_obj):

    """ 
    bpn = background_process_notification
    @key: communication uuid key of application
    @user: user to which notification has to be sent
    @message: message dict
    @log_obj: log_obj of application

    """

    try:
            
        signal = SERVER['signals']

        url = signal['base_url'] + signal['bpn'] 

        resp = requests.post(url, data={"key":key, "user":user, "message":message})

        result = {"goAhead":False}

        if resp.status_code == 200:

            resp = resp.json()

            if resp["goAhead"]:

                log_obj.debug(f"bpn sent to {user}")

                result = {"goAhead":True}

            else:

                log_obj.error(f"bpn failed to {user} \n {resp['message']}", exc_info=True)


        else:

            log_obj.error(f"bpn failed to {user} \n {resp}", exc_info=True)



    except Exception as e:

        log_obj.exception("bpn signal error \n {e}", exc_info=True)


    return result