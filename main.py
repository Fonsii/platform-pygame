from game_controller import GameController

WIDTH = 600
HEIGHT = 600

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()