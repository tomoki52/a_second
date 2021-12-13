// For toggle button;

function toggleClass() {

    const body = document.querySelector('body');
    body.classList.toggle('light');
    body.style.transition = `0.3s linear`;
}

// for time;
const deg = 6;
// 360 / (12 * 5);

const hr = document.querySelector('#hr');
const mn = document.querySelector('#mn');
const sc = document.querySelector('#sc');
let day = new Date();
let hh = day.getHours() * 30;
let mm = day.getMinutes() * deg;
let ss = day.getSeconds() * deg;
let msec = day.getMilliseconds();
let a_second = 0.3 //人によって変わる

setInterval(() => {

    // VERY IMPORTANT STEP:
    ss = ss + deg;
    console.log("ss:" + ss)
    if (ss % 360 == 0) {
        console.log("minute")
        mm = mm + deg;

        if (mm % 360 == 0) {
            hh = hh + 30;
        }
    }

    console.log("mm:" + mm)
    hr.style.transform = `rotateZ(${hh}deg)`;
    mn.style.transform = `rotateZ(${mm}deg)`;
    sc.style.transform = `rotateZ(${ss}deg)`;

    // gives the smooth transitioning effect, but there's a bug here!
    // sc.style.transition = `1s`;


}, a_second * 1000);

