// jshint esversion: 6

// Automatically dismiss messages
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);


// Dropdown exercises filters
$(document).ready(function(){
    $(".expand").click(function(){
        $(this).parent().next().slideToggle(600);
    
    });
});

const filters = document.querySelector('.filter-exercises');
const adjustDisplay = () => {
    const width = window.innerWidth;
    filters.style.display = width > 502 ? 'block' : 'none';
};
window.onload = () => adjustDisplay();
window.onresize = () => adjustDisplay();