# Pong Using RL
[![Join the chat at https://gitter.im/bdaybot/Lobby](https://badges.gitter.im/Pong-Using-RL/Lobby.svg)](https://gitter.im/Pong-Using-RL/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)   

Simple implementation for a single player pong game.

### Requirements:
- Pygame

The aim is to implement Reinforcement Learning concepts to make the AI win at this game. Refer to the article http://karpathy.github.io/2016/05/31/rl/ by Karpathy. 
 
Following is the link for "Pong from Pixel by Karpathy": https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5

## TODO
- Implement the code in Tensorflow.
- Improve Feature selection: Presently, the code rely totally on present frame for detecting features and training model. Therefore, It needs more than 5-6 hrs of training even on a standard GPU. The training time can be improved if we can provide other game states as features. 
- Generalize the architecture: The architecture of the network is pretty broad. and can be extended to other atari games also.  
