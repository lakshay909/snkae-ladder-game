// game.js

document.addEventListener("DOMContentLoaded", function() {
    // Add event listeners for user actions
});

function rollDice() {
    // Send a request to roll the dice and update the game state
    fetch('/roll_dice/<game_id>/')  // Replace <game_id> with the actual game ID
    .then(response => response.json())
    .then(data => handleRollResult(data));
}

function handleRollResult(result) {
    // Handle the result of rolling the dice
    console.log(result); // Example: { message: 'Player 1 rolled a 4 and moved to 14' }
    fetchGameState(); // Fetch updated game state after rolling the dice
}
