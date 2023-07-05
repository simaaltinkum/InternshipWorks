function updateTime() {
    var date = new Date().toLocaleString("tr-TR");
    document.getElementById("time").innerHTML = "Time right now: " + date;
}

updateTime(); // Call the function initially to display the time immediately

setInterval(updateTime, 1000); // Call the function every second to update the time