function getVentStatus(concentration) {
 return concentration < 21;
}

let newMsg = {};
let newMsgType = {};
newMsg = {
    "method": "setValveState",
    "concentration": msg.concentration,
    "status": getVentStatus(msg.concentration) ? 1 : 0
};
newMsgType = "POST_ATTRIBUTES_REQUEST";
return {msg: newMsg, metadata: metadata, msgType: newMsgType};
