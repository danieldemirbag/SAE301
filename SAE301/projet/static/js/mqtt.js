const host = "test.mosquitto.org";

const port = 8080;
const topic = "Courgette/banane/lièvre";
const topic2 = "Courgette/banane/lièvre2";
let client;


function connect(){
	try{
		client = new Paho.MQTT.Client(host, port, "");

		client.onConnectionLost = function(){console.log('Connection lost')};
		client.onMessageArrived = onMessage;

		client.connect({
			onSuccess : () => {
			    console.log("connected");

				client.subscribe(topic);
			},
			onFailure : () => {
				console.log("failed to connect");
			}
		});
	}
	catch(err){
		console.log(err);
	}
}


function connect2(){
	try{
		client = new Paho.MQTT.Client(host, port, "");

		client.onConnectionLost = function(){console.log('Connection lost')};
		client.onMessageArrived = onMessage;

		client.connect({
			onSuccess : () => {
			    console.log("connected");

				client.subscribe(topic2);
			},
			onFailure : () => {
				console.log("failed to connect");
			}
		});
	}
	catch(err){
		console.log(err);
	}
}


// calls when message arrives
function onMessage(mgs){
  	mgs = JSON.stringify(mgs.payloadParse);
}



// publish a message
function publish(){
	let data = JSON.stringify("1");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	mgs.destinationName = topic;
	client.send(mgs);

	document.getElementById('message').value = '';
}

function publish2(){
	let data = JSON.stringify("0");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	mgs.destinationName = topic;
	client.send(mgs);

	document.getElementById('message').value = '';
}


function publish3(){
	let data = JSON.stringify("1");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	mgs.destinationName = topic2;
	client.send(mgs);

	document.getElementById('message').value = '';
}

function publish4(){
	let data = JSON.stringify("0");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	mgs.destinationName = topic2;
	client.send(mgs);

	document.getElementById('message').value = '';
}

function publish5(){
	let data = JSON.stringify("1");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	let mgs2 = new Paho.MQTT.Message(a);
	mgs.destinationName = topic;
	mgs2.destinationName = topic2;
	client.send(mgs);
    client.send(mgs2);

	document.getElementById('message').value = '';
}

function publish6(){
	let data = JSON.stringify("0");
	const a = JSON.parse(data);
	let mgs = new Paho.MQTT.Message(a);
	let mgs2 = new Paho.MQTT.Message(a);
	mgs.destinationName = topic;
	mgs2.destinationName = topic2;
	client.send(mgs);
    client.send(mgs2);

	document.getElementById('message').value = '';
}