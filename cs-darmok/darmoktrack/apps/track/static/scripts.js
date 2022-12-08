// // Initialize the time clock with a starting time of 0
// let time = 0;

// // Initialize the timer variable to null
// let timer = null;

// // Function to start the timer
// function startTimer() {
//   // If the timer is not running, start it
//   if (!timer) {
//     timer = setInterval(function() {
//       time++;
//       // Update the time display with the new time
//       updateTimeDisplay();
//     }, 1000);
//   }
// }

// // Function to stop the timer
// function stopTimer() {
//   // If the timer is running, stop it
//   if (timer) {
//     clearInterval(timer);
//     timer = null;
//   }
// }

// // Function to update the time display
// function updateTimeDisplay() {
//   // Get the current time in hours, minutes, and seconds
//   let hours = Math.floor(time / 3600);
//   let minutes = Math.floor((time % 3600) / 60);
//   let seconds = time % 60;

//   // Format the time as a string (e.g. "01:23:45")
//   let timeString = `${hours.toString().padStart(2, "0")}:${minutes
//     .toString()
//     .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

//   // Update the time display with the formatted time string
//   document.getElementById("time-display").innerHTML = timeString;
// }
