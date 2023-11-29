// static/game.js
document.addEventListener('DOMContentLoaded', function () {
    const appContainer = document.getElementById('app');
    const gameStateContainer = document.createElement('div');
    gameStateContainer.id = 'game-state-container';
    appContainer.appendChild(gameStateContainer);
  
    // Dominion Game Logic
    class DominionGame {
      constructor() {
        this.state = {
          actions: 1,
          buys: 1,
          coins: 0,
          playerDeck: ['Copper', 'Copper', 'Copper', 'Estate', 'Estate', 'Estate'],
          supply: ['KingdomCard1', 'KingdomCard2', 'KingdomCard3'],
        };
        this.renderGameState();
      }
  
      renderGameState() {
        gameStateContainer.innerHTML = `
          <p>Actions: ${this.state.actions} | Buys: ${this.state.buys} | Coins: ${this.state.coins}</p>
          <p>Player Deck: ${this.renderCardImages(this.state.playerDeck)}</p>
          <p>Supply: ${this.renderCardImages(this.state.supply)}</p>
        `;
      }
  
      renderCardImages(cardList) {
        return cardList.map(card => `<img src="images/${card}.png" alt="${card}" class="card-image">`).join('');
      }
  
      playTurn() {
        // Send a POST request to the /play_turn endpoint
        fetch('/play_turn', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ player: 'player1' }), // Change 'player1' to 'player2' if needed
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          // Refresh the game state after the turn is played
          this.renderGameState();
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }
    }
  
    // Create an instance of the Dominion Game
    const dominionGame = new DominionGame();

    const playTurnButton = document.getElementById('playTurnButton');
    playTurnButton.addEventListener('click', () => dominionGame.playTurn());
  });
  