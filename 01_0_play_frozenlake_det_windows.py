import gym
from gym.envs.registration import register

# http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
import readchar  # pip3 install readchar

#  coding: utf-8
import gym
from gym.envs.registration import register
import readchar
from KBHit import KBHit
from colorama import init
init(autoreset=True)



def test1():

    #env = gym.make("SpaceInvaders-v0") \
    #env = gym.make("Taxi-v2")
    env = gym.make("FrozenLake-v0") 
    env.reset() 
    for _ in range(1000): 
        env.render() 
        env.step(env.action_space.sample())
def test2():
    KB = KBHit()
    k = KB.getarrow()
    print(k)

def play_frozenlake_det():
    # MACROS
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3
    
    # Key mapping
    arrow_keys = {
        '\x1b[A': UP,
        '\x1b[B': DOWN,
        '\x1b[C': RIGHT,
        '\x1b[D': LEFT}
    
    # Register FrozenLake with is_slippery False
    register(
        id='FrozenLake-v3',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name': '4x4', 'is_slippery': False}
    )
    
    env = gym.make('FrozenLake-v3')
    env.render()  # Show the initial board
    
    while True:
        # Choose an action from keyboard
        key = readchar.readkey()
        if key not in arrow_keys.keys():
            print("Game aborted!")
            break
    
        action = arrow_keys[key]
        state, reward, done, info = env.step(action)
        env.render()  # Show the board after action
        print("State: ", state, "Action: ", action,
              "Reward: ", reward, "Info: ", info)
    
        if done:
            print("Finished with reward", reward)
            break
    


def play_frozenlake_det_windows():
    
    # Register FrozenLake with is_slippery False
    register(
        id='FrozenLake-v3',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name': '4x4', 'is_slippery': False}
    )
    
    env = gym.make('FrozenLake-v3')
    env.render()  # Show the initial board
    KB = KBHit()
    while True:
        # Choose an action from keyboard
        action = KB.getarrow()
        if action not in [0, 1, 2, 3]:
            print("Game aborted!")
            break
        state, reward, done, info = env.step(action)
        env.render()  # Show the board after action
        print("State: ", state, "Action: ", action,
              "Reward: ", reward, "Info: ", info)
    
        if done:
            print("Finished with reward", reward)
            break




if __name__ == "__main__":    
    play_frozenlake_det_windows()
