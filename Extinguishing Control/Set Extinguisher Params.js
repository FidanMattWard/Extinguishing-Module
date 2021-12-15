function getSupplyInergenStatus(concentration, flag) {
    return flag && concentration > 5;
}

let newMsg = {};
let newMsgType = {};
newMsg = {
    "method": "setValveState",
    "concentration": msg.concentration,
    "inergen": getSupplyInergenStatus(msg.concentration, msg.flag)
};
newMsgType = "POST_ATTRIBUTES_REQUEST";
return {msg: newMsg, metadata: metadata, msgType: newMsgType};
