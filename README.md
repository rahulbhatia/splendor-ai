## Splendor AI Project
#### Purpose
  - Model a "real-world" system
  - Be able to create a complex state machine
  - Model interactions with that state machine in a simple to understand way
  - Build an ai solution that can make a decision on which move to play
  - Feature engineering on how to transform the game model into inputs to a statistical model

#### Part 1: Modeling
  - Model the Splendor Game by decomposition into Decks, Table, Banks, & Players
  - Model the Players as Banks, Cards, + Points
  - Model the Banks as dictionaries of Stacks (which are just unit counters)
  - Model the Table as face up set of cards
  - Be able to generate a realistic looking deck for either l1,l2,l3 card types
  
#### Part 2: Model State Change
  - Implement state change for each model type
  - Decks generate cards
  - Stacks can grow or decrease
  - Players can do one of a set of actions {take 2 coins of one color, take 3 different coins, buy a card}
  - Be able to apply a state change to a game and generate the resulting game object 
    - by this approach, a SplendorGame object is immutable; rather than mutate the state, we actually produce a new SplendorGame by applying a SplendorMove(or something similar)
    - We do this because our eventual ai system will need to apply all possible moves and evaluate the best one using some heuristic (trained or otherwise)
    
#### Part 3: Simulate Game Play
  - Construct a notation for gameplay
  - simulate gameplay as a random walk through space

#### Part 4: Build a Policy Model to evaluate the $P(Player_{x} Wins \mid  State )$
  - Generate a few potential models to evaluate the probability above
  - Have the models play each other to see who wins the most
