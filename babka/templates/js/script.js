document.addEventListener("DOMContentLoaded", function() {
// Отображение текущей даты и времени в подвале
    var footer = document.querySelector("footer");
    var currentDate = new Date();
    var dateString = currentDate.toLocaleDateString("ru-RU");
    var timeString = currentDate.toLocaleTimeString("ru-RU", { hour:
"2-digit", minute: "2-digit" });

var dateTimeString = dateString + ", " + timeString;
footer.innerHTML = dateTimeString + " © Камнев И.С.";
});