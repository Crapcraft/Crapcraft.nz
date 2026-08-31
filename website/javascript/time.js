// Source - https://stackoverflow.com/a/73791364
// Posted by EssXTee
// Retrieved 2026-07-27, License - CC BY-SA 4.0

const _DateAndTime = () => {
  document.querySelector("#currentTime").innerHTML = new Date().toLocaleDateString('en-nz', {hour: 'numeric', minute: 'numeric', hour12: true});
}

setInterval(_DateAndTime, 60000); // 60000 = T(m)
_DateAndTime();
//if you want to know what this does just goto the stack overflow page