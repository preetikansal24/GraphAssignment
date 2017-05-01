/**
 * Created by preetikansal on 30/04/17.
 */

var imported = document.createElement('script');
imported.src = 'sample.js';
document.head.appendChild(imported);

var edgesArray = [];
function createEdge() {
    document.getElementById("fromContainer").innerHTML = "";
    document.getElementById("toContainer").innerHTML = "";
    console.log(nodesArray, "NodesArray accessed");
    var createSelectFrom = document.createElement("SELECT");
    createSelectFrom.id = "fromEdgeValue";
    var createSelectTo = document.createElement("SELECT");
    createSelectTo.id = "toEdgeValue";
    for(var index=0;index<nodesArray.length;index++) {
        var createOptionFrom = document.createElement("OPTION");
        var createOptionTo = document.createElement("OPTION");
        createOptionFrom.value = nodesArray[index].id;
        createOptionFrom.text = nodesArray[index].label;
        createOptionTo.value = nodesArray[index].id;
        createOptionTo.text = nodesArray[index].label;
        createSelectFrom.appendChild(createOptionFrom);
        createSelectTo.appendChild(createOptionTo);
    }

    console.log(" Select ", createSelectFrom, createSelectTo);
    document.getElementById("fromContainer").appendChild(createSelectFrom);
    document.getElementById("toContainer").appendChild(createSelectTo);
}

function addEdgeToNetwork () {
    console.log("here");
    var fromEdgeVal = document.getElementById("fromEdgeValue").value;
    var toEdgeVal = document.getElementById("toEdgeValue").value;
    var edge = {from: parseInt(fromEdgeVal), to: parseInt(toEdgeVal)};
    xdr("http://127.0.0.1:8000/v1/edge", "POST", edge, successEdgeCallback);
    //edgesArray.push(edge);
    //console.log("edgeArray ",edgesArray);
}

function successEdgeCallback(response){
    if (response !== null) {
        edgesArray.push(JSON.parse(response));
        console.log("edges array", edgesArray);
    }
}
