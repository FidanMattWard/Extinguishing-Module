var details = {};
if (metadata.prevAlarmDetails) {
    details = JSON.parse(metadata.prevAlarmDetails);
    //remove prevAlarmDetails from metadata
    delete metadata.prevAlarmDetails;
    //now metadata is the same as it comes IN this rule node
}
details.status = msg.status;
details.concentration = msg.concentration

return details;
