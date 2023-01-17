import { transport } from "./transport.js"


export class handel_login extends transport {


    constructor(){
        
        super()
        this.initiate_transport()
        this.LOGIN_PATH = '/auth/registered_user/login/'
    }


    inititate_handel_login(){

        this.send_login_form();
        
        
    }


    send_login_form(){


        let data = {
            "username": "",
            "email": "apps@it-taas.com",
            "password": "Frooti@30"
        }


        console.log("good0");
        
        this.send_post(this.LOGIN_PATH, data, console.log, console.log);

        console.log("good1");

    }

}



