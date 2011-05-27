$(document).ready(function(){
     options = {
        dataType:  'json', 
        success:function(data){
            $("#edit_person textarea, select, input").attr('disabled','')
            $('#load').hide()
            processJson(data)
        },
        beforeSubmit: function(){
            $("#edit_person  textarea, select, input").attr('disabled','disabled')
            $('#load').show()
        },
        error:function(){
            alert('ajax error')
            $("#edit_person textarea, select, input").attr('disabled','')
            $('#load').hide()
        }
    }

    $("#edit_person_form").ajaxForm(options)

 function processJson( data) { 
     if (data) {
         $('.errors').remove()
         if (! eval(data.success)) {
             errors = eval(data.errors);
             $.each(errors, function(fieldname,errmsg)
             {   
                 id = "#id_" + fieldname;
                 iderr =  "id_" + fieldname + '_errror';
 
                 if ($('#' + iderr).length == 0){ 
                     $(id).parent().after($("<span class='errors' id='"+iderr+"'></span>"));    
                 }   
                 $('#'+iderr).html( errmsg );
             })  
             $("#form textarea, select, input").attr('disabled','')
 
         }else{
             $("#edit_person_form").clearForm();
             $('#edit_person_form').populate(data.data)
             //alert('operation is complited')
         }   
     } else {
         alert("Ajax error : no data received. ")
     }   
 }
 })
