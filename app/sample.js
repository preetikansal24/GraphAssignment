/**
 * Created by preetikansal on 01/05/17.
 */

function xdr(url, method, data, callback) {
    var req;
    if(XMLHttpRequest) {
        req = new XMLHttpRequest();

        if('withCredentials' in req) {
            req.open(method, url, true);
            //req.onerror = errback;
            req.onreadystatechange = function() {
                if (req.readyState === 4) {
                    if (req.status >= 200 && req.status < 400) {
                        console.log("response is " + req.responseText);
                        callback(req.responseText);
                        //return req.responseText;

                    } else {
                        console.log(new Error('Response returned with non-OK status'));
                        callback(null);
                        //return null;
                    }
                }
            };
            //req.setRequestHeader("Content-Type", "application/json")
            req.send(JSON.stringify(data));
        }
    } else if(XDomainRequest) {
        req = new XDomainRequest();
        req.open(method, url);
        req.onerror = errback;
        req.onload = function() {
            console.log("here" + req.responseText);
        };
        req.send(data);
    } else {
        console.log(new Error('CORS not supported'));
    }
}