document.getElementById('prev-button').addEventListener('click', function() {
    const bestsellGrid = document.querySelector('.bestsell-grid');
    bestsellGrid.scrollLeft -= 200; // Adjust the scrolling distance as needed
});

document.getElementById('next-button').addEventListener('click', function() {
    const bestsellGrid = document.querySelector('.bestsell-grid');
    bestsellGrid.scrollLeft += 200; // Adjust the scrolling distance as needed
});
