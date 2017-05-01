/**
 * Created by preetikansal on 30/04/17.
 */

function createNodeRequest(data) {
  console.log("came to backend", data);
  url = "http://127.0.0.1:8000/v1/graph";
  $.ajax({
    beforeSend: function(xhr){
    xhr.setRequestHeader('Access-Control-Allow-origin', '*');
    },
    type: "POST",
    url: url,
    dataType: 'json',
    crossDomain: true,
    data:JSON.stringify(data),
    contentType:'application/json',
    success: function(response) {
      console.log("abc"  + response);
    },
    error: function(response){
      console.log("error response is " + response.data);
    }
  });
}
