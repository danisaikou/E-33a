function addCurrentTime(fieldId) {
    // Get the current date and time
    var currentTime = new Date();

    // Format the date and time as a string
    var currentTimeString = currentTime.toISOString();

    // Get the form field element with the specified ID
    var field = document.getElementById(fieldId);

    // Set the value of the field to the current date and time
    field.value = currentTimeString;

    console.log("time entered")
}