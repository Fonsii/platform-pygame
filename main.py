from game_controller import GameController

WIDTH = 400
HEIGHT = 400

def main():
    controller = GameController(WIDTH, HEIGHT)  
    controller.start()  

if __name__ == '__main__':
    main()