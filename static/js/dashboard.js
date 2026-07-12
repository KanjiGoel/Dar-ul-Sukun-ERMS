/*=========================================
    LIVE DATE & TIME
=========================================*/

function updateDateTime() {

    const now = new Date();

    const options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
    };

    const date = now.toLocaleDateString("en-US", options);

    const time = now.toLocaleTimeString();

    const dateTime = document.getElementById("datetime");

    if (dateTime) {
        dateTime.innerHTML = `
            <div>${date}</div>
            <div>${time}</div>
        `;
    }

}

updateDateTime();

setInterval(updateDateTime, 1000);



/*=========================================
    NOTIFICATION BELL
=========================================*/

const bell = document.querySelector(".fa-bell");

if (bell) {

    bell.addEventListener("click", () => {

        alert(
`Notifications

• Employee Added

• Salary Updated

• Promotion Added

• Document Uploaded`
        );

    });

}



/*=========================================
    MOBILE SIDEBAR
=========================================*/

const menuBtn = document.getElementById("menuBtn");

const sidebar = document.querySelector(".sidebar");

if (menuBtn && sidebar) {

    menuBtn.addEventListener("click", () => {

        sidebar.classList.toggle("active");

    });

}



/*=========================================
    CARD HOVER EFFECT
=========================================*/

const cards = document.querySelectorAll(".card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-6px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});



/*=========================================
    QUICK ACTION BUTTONS
=========================================*/

const buttons = document.querySelectorAll(".quick-actions button");

buttons.forEach(btn => {

    btn.addEventListener("click", () => {

        console.log(btn.innerText + " Clicked");

    });

});



/*=========================================
    READY FOR FUTURE
=========================================*/

// Chart.js

// AJAX Notifications

// Employee Search

// Dashboard Statistics

// Real-Time Updates