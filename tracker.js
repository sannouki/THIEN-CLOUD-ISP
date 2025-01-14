// tracker.js

// Get references to the tracker elements
const counterElement = document.getElementById('counter');
const incrementButton = document.getElementById('increment');

// Initialize the counter (default 0)
let counter = 0;

// Function to update the displayed counter
function updateCounter() {
    counterElement.textContent = counter;
}

//Increase Count button
incrementButton.addEventListener('click', () => { 
counter += 1; // Increase counter by 1
updateCounter();
});

//updateCounter();
