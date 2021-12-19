function getAlarmStatus(concentration) {
 return concentration > 30;
}

let newMsg = {};
let newMsgType = {};
newMsg = {
    "method": "setValveState",
    "concentration": msg.concentration,
    "alarm": getAlarmStatus(msg.concentration) ? 1 : 0
};
newMsgType = "POST_ATTRIBUTES_REQUEST";
return {msg: newMsg, metadata: metadata, msgType: newMsgType};
