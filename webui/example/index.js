function inviaComando()
{
 var comando = $("#comando").val();
 if(comando == undefined || comando == "")
   printAlert("err","Devi inserire un comando");
 else
 {
   var s = comando.split(" ");
   if(s[1] == undefined || s[1] == "")
     printAlert("err","Devi inserire un valore per il comando");
   else
     ajaxComando(s[0],s[1]);
 }
}
function changeLuce()
{
 if ($("#luce").attr("class") == "btn btn-lg btn-success")
   ajaxComando("luce", "on");
 else
   ajaxComando("luce", "off");
}
function changePir()
{
 if ($("#pir").attr("class") == "btn btn-lg btn-success")
   ajaxComando("pir", "on");
 else
   ajaxComando("pir", "off");
}
function tvCommand(txt)
{
 if(txt=="pow")
 {
   if($("#pow").attr("class") == "btn btn-lg btn-success glyphicon glyphicon-off")
      txt="on";
   else 
      txt="off";
 }
 ajaxComando("tv", txt);
}
function aggiorna()
{
 ajaxComando("refresh","all");
}
function printAlert(type, val)
{
 $("#alert").show();
 if(type=="ok")
 {
   $("#alert").attr("class","alert alert-success fade in alert-dismissable myAlert");
   $("#titAlert").text("Tutto bene: ");
   $("#textAlert").text(val);
 }
 else
 {
   $("#alert").attr("class","alert alert-danger fade in alert-dismissable myAlert");
   $("#titAlert").text("Errore: ");
   $("#textAlert").text(val);
 }
}
function closeAlert()
{
 $("#alert").hide();
}
function ajaxComando(tipo, val)
{
  $.get({
    url: "/comando",
    data: {"nodo" : tipo, "cmd" : val},
    success: function (data){
      var obj=JSON.parse(data);
      printAlert(obj.header,obj.payload);
      if(obj.header=="ok")
      {
          switch(tipo)
         {
            case "luce":
              if(val=="on"){
                 $("#luc").attr("class","label label-success");
                 $("#luc").text("ON");
                 $("#luce").attr("class","btn btn-lg btn-danger");
                 $("#luce").text("LUCE OFF");
              }
              else{
                 $("#luce").attr("class","btn btn-lg btn-success");
                 $("#luce").text("LUCE ON");
                 $("#luc").attr("class","label label-danger");
                 $("#luc").text("OFF");
             }
            break;
            case "pir":
              if(val=="on"){
                 $("#pi").attr("class","label label-success");
                 $("#pi").text("ON");
                 $("#pir").attr("class","btn btn-lg btn-danger");
                 $("#pir").text("PIR OFF");
              }
              else{
                 $("#pi").attr("class","label label-danger");
                 $("#pi").text("OFF");
                 $("#pir").attr("class","btn btn-lg btn-success");
                 $("#pir").text("PIR ON");
              }
            break;
            case "tv":
              if(val=="on")
                 $("#pow").attr("class","btn btn-lg btn-danger glyphicon glyphicon-off");
               if(val=="off")
                 $("#pow").attr("class","btn btn-lg btn-success glyphicon glyphicon-off");
            break;
            case "refresh":
                  var data = new Date();  
                  alert("Nuova presenza:"+data.getDate()+"-"+(data.getMonth()+1)+"-"+data.getFullYear()+" "+data.getHours()+":"+data.getMinutes());
            break;
         }
      }
    }
  });
}