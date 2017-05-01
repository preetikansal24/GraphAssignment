/**
 * Created by preetikansal on 30/04/17.
 */

var imported = document.createElement('script');
imported.src = 'sample.js';
document.head.appendChild(imported);
var selectedObjects = [];

var nodeIndex = 1;
var nodesArray = [];
var network = new vis.Network();
var subGraphData = {};
console.log("loaded");
function createNode() {
    var nodeDiv = document.getElementById("nodeDiv");
        console.log("Click event registered");
        if (nodeDiv.style.display === 'none') {
            nodeDiv.style.display = 'block';
        }
}

function addNodeToNetwork() {
    var nodeName = document.getElementById("nodeName");
    var nodeDiv = document.getElementById("nodeDiv");
    var node = {
        id: nodeIndex,
        label: nodeName.value
    };
    xdr("http://127.0.0.1:8000/v1/node", "POST", node, successNodeCallback);
}

function successNodeCallback(response){
    if (response !== null) {
        nodesArray.push(JSON.parse(response));
        nodeIndex++;
        console.log("nodesArray", nodesArray);
        nodeDiv.style.display = 'none';
    }
}

function showGraph() {
    var nodes = new vis.DataSet(nodesArray);
    var edges = new vis.DataSet(edgesArray);
    var container = document.getElementById('mynetwork');
    selectedObjects = [];
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {
        clickToUse: true,
        interaction:{
            dragNodes:true,
            dragView: true,
            hideEdgesOnDrag: false,
            hideNodesOnDrag: false,
            hover: false,
            hoverConnectedEdges: true,
            keyboard: {
              enabled: false,
              speed: {x: 10, y: 10, zoom: 0.02},
              bindToWindow: true
            },
            multiselect: true,
            navigationButtons: true,
            selectable: true,
            selectConnectedEdges: true,
            tooltipDelay: 300,
            zoomView: true
        }
    };
    network = new vis.Network(container, data, options);
    network.on("click", function (params) {
        console.log(params);
        selectedObjects.push(params);
        console.log("selected obects" + selectedObjects);
    });
}

function showSubgraph() {
    data = {}
    var container1 = document.getElementById('mynetwork1');
    console.log("Data here ", selectedObjects);
    var nodeArr=[];
    var edgeArr=[];
    for(var i=0;i<selectedObjects.length;i++) {
        var node = {
            id: selectedObjects[i].nodes.valueOf(0)
        };
        var edge = {
            id: selectedObjects[i].edges.valueOf(0)
        };
        nodeArr.push(node);
        edgeArr.push(edge);
    }
    debugger;

    data.nodes = nodeArr;
    data.edges = edgeArr;
    /*{
            nodes: network.getSelectedNodes(),
            edges: network.getSelectedEdges()
        }*/
        var net1 = new vis.Network(container1, data, {});


}

function createGraph() {
    var graphName = document.getElementById('graphName').value;
    console.log("graph name is " + graphName);
    var payload = {
        "nodes" : nodesArray,
        "edges" : edgesArray,
        "graphName" : graphName
    };
    xdr("http://127.0.0.1:8000/v1/graph", "POST", payload, successGraphCallback);
}

function successGraphCallback(response) {
    if (response != null)
    {
        window.alert("Graph created successfully");
    }
    else{
        window.alert("Failed to create graph");
    }
}


//console.log("Get Slected Nodes",network.getSelectedNodes());