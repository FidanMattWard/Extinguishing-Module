function getVentStatus(concentration) {
 return concentration < 21;
}

let newMsg = {};
let newMsgType = {};
newMsg = {
    "method": "setValveState",
    "concentration": msg.concentration,
    "status": getVentStatus(msg.concentration)
};
newMsgType = "POST_ATTRIBUTES_REQUEST";
return {msg: newMsg, metadata: metadata, msgType: newMsgType};
