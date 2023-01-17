

export class transport{


    constructor(){

                

    }


    initiate_transport(){

        console.log("this good");

        let jQueryScript = document.createElement('script');  
        jQueryScript.setAttribute('src','https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js');
        document.head.appendChild(jQueryScript);


    }


    get_csrf(data){

        data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val()


        return data

    }   
    
    
    send_post(path, data, success_callback, error_callback){

        
        $.post( path, this.get_csrf(data) )
        .done(function( json ) {
            
            success_callback(json)

        })
        .fail(function( jqxhr, textStatus, error ) {
            
            error_callback({json:jqxhr, textStatus:textStatus, error:error})

        });

    }



    
}