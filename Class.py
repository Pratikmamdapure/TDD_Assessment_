#This File Contains class with all opeartions,and testing of each opeartion of class

import unittest
'''---------Spacecraft class with all operation---------'''
class Chandrayaan:

    #x axis is in direction of E/W
    #y axis is in direction of N/S
    #z axis is in direction of UP/Down
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    #Forward Motion
    def move_forward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y + 1, z)
        elif self.direction == 'S':
            self.position = (x, y - 1, z)
        elif self.direction == 'E':
            self.position = (x + 1, y, z)
        elif self.direction == 'W':
            self.position = (x - 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z + 1)
        elif self.direction == 'Down':
            self.position = (x, y, z - 1)
        pass


    #Backward Motion
    def move_backward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y - 1, z)
        elif self.direction == 'S':
            self.position = (x, y + 1, z)
        elif self.direction == 'E':
            self.position = (x - 1, y, z)
        elif self.direction == 'W':
            self.position = (x + 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z - 1)
        elif self.direction == 'Down':
            self.position = (x, y, z + 1)
        pass
    #Rotating Left Operation
    def rotate_left(self):
        
        if self.direction == 'N':
            self.direction='W'
        elif self.direction == 'S':
            self.direction='E'
        elif self.direction == 'E':
            self.direction='N'
        elif self.direction == 'W':
            self.direction='S'
        elif self.direction=='Up':
            self.direction='N'
        elif self.direction=='Down':
            self.direction='S'
        pass

        
    #Rotating Right Operation
    def rotate_right(self):
        if self.direction == 'N':
            self.direction='E'
        elif self.direction == 'S':
            self.direction='W'
        elif self.direction == 'E':
            self.direction='S'
        elif self.direction == 'W':
            self.direction='N'
        elif self.direction=='Up':
            self.direction='S'
        elif self.direction=='Down':
            self.direction='N'
        pass
    #Rotating Up Operation
    def turn_up(self):
        
        self.direction = 'Up'
        
        pass
    #Rotating Down Operation
    def turn_down(self):
        
        self.direction = 'Down'
        pass
    #Function to execute a set of commands
    def Execute(self,commands):

        for command in commands:
            if command=='f':
                self.move_forward()
            elif command=='b':
                self.move_backward()
            elif command=='r':
                self.rotate_right()
            elif command=='l':
                self.rotate_left()
            elif command=='u':
                self.turn_up()
            elif command=='d':
                self.turn_down()

    def get_position(self):
        return self.position
    
    def get_direction(self):
        return self.direction

'''--------------TDD PART-----------------'''
#Testing using Unittest Module
class Test(unittest.TestCase):
    
    #testinf the forward opeartion using forward commands
    def test_move_forward(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
        
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.position, (0, 1, 0))
        print("Move Forward-->")
        print("Expected Output:",(0,1,0),'N')
        print("Actual Output:",spacecraft.position,spacecraft.direction)
        
        
    #tetsing move backward operation
    def test_move_backward(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.move_backward()
        self.assertEqual(spacecraft.position, (0, -1, 0))
        print("Move Backward-->")
        print("Expected Output:",(0,-1,0),'N')
        print("Actual Output:",spacecraft.position,spacecraft.direction)


    #testing move right 
    def test_rotate_right(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.rotate_right()
        self.assertEqual(spacecraft.direction, 'E')

        print("Rotate Right-->")
        print("Expected Output:",(0,0,0),'E')
        print("Actual Output:",spacecraft.position,spacecraft.direction)


    #testing move left
    def test_move_left(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
      
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.direction, 'W')
        print("Rotate left-->")
        print("Expected Output:",(0,0,0),'W')
        print("Actual Output:",spacecraft.position,spacecraft.direction)


    #testing turn up operation
    def test_turn_up(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
       
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, 'Up')

        print("Turn Up-->")
        print("Expected Output:",(0,0,0),'Up')
        print("Actual Output:",spacecraft.position,spacecraft.direction)

    #testings turn down operation
    def test_turn_down(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
        command=['d']
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, 'Down')

        print("Turn Down-->")
        print("Expected Output:",(0,0,0),'Down')
        print("Actual Output:",spacecraft.position,spacecraft.direction)

    #Testing for set of commands
    def test_execute(self):
        initial_position=(0,0,0)
        x,y,z=initial_position
        initila_direction='N'
        command=['f','r','u','b','l']
        spacecraft=Chandrayaan(x,y,z,initila_direction)
        spacecraft.Execute(command)
        self.assertEqual(spacecraft.position,(0,1,-1))
        self.assertEqual(spacecraft.direction, 'N')
        print("--Testing Set of Commands-----------------")
        print("Initial Position &direction :",initial_position, initila_direction)
        
        print("Commands :",command)
        print("")
        print("Expected Output:",(0,1,-1),'N')
        print("Actual Output:",spacecraft.position,spacecraft.direction)
        print("--Testing each operation -----------------")
        



if __name__=='__main__':

    unittest.main()

    '''
    Commands: [“f”, “r”, “u”, “b”, “l”]

    Starting Position: (0, 0, 0)

    Initial Direction: N

    “f” - (0, 1, 0) - N
    “r” - (0, 1, 0) - E
    “u” - (0, 1, 0) - U
    “b” - (0, 1, -1) - U
    “l” - (0, 1, -1) - N
    Final Position: (0, 1, -1)

    Final Direction: N
    '''


#OUTPUT

'''
--Testing Set of Commands-----------------
Initial Position &direction : (0, 0, 0) N
Commands : ['f', 'r', 'u', 'b', 'l']

Expected Output: (0, 1, -1) N
Actual Output: (0, 1, -1) N
--Testing each operation -----------------
.Move Backward-->
Expected Output: (0, -1, 0) N
Actual Output: (0, -1, 0) N
.Move Forward-->
Expected Output: (0, 1, 0) N
Actual Output: (0, 1, 0) N
.Rotate left-->
Expected Output: (0, 0, 0) W
Actual Output: (0, 0, 0) W
.Rotate Right-->
Expected Output: (0, 0, 0) E
Actual Output: (0, 0, 0) E
.Turn Down-->
Expected Output: (0, 0, 0) Down
Actual Output: (0, 0, 0) Down
.Turn Up-->
Expected Output: (0, 0, 0) Up
Actual Output: (0, 0, 0) Up
.
----------------------------------------------------------------------
Ran 7 tests in 0.007s

OK
'''