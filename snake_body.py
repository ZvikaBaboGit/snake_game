




class Snake:
    def __init__(self):
        self.__snake_data = [(10,10),(10,9),(10,8)]
        self.__head = self.__snake_data[0]

    def get_snake_data(self):
        return self.__snake_data

    def get_snake_head(self):
        return self.__head

    def _unvalid_move(self,string):
        # This method is aמ internal method.
        if string == "Down" and self.__snake_data[1][1] == self.__snake_data[0][1]-1:return True
        elif string == "Up" and self.__snake_data[1][1] == self.__snake_data[0][1] + 1:return True
        elif string == "Right" and self.__snake_data[1][0] == self.__snake_data[0][0] + 1:return True
        elif string == "Left" and self.__snake_data[1][0] == self.__snake_data[0][0] - 1:return True
        return False

    def _move(self,index,direction):
        # This method is aמ internal method.
        tmp = self.__snake_data[0]
        t = list(self.__snake_data[0])
        t[index] += direction
        t = tuple(t)
        self.__snake_data[0] = t
        for i in range(1,len(self.__snake_data)):
            tmp_2 = self.get_snake_data()[i]
            self.get_snake_data()[i] = tmp
            tmp = tmp_2
    def _move_straight(self,direction):
        # This method is aמ internal method.
        if direction == "Up":self._move(1,1)
        elif direction == "Down":self._move(1,-1)
        elif direction == "Right":self._move(0,1)
        elif direction == "Left": self._move(0,-1)

    def _check_direction(self):
        # This method is aמ internal method.
        if self.__snake_data[0][1]-self.__snake_data[1][1]==1: return "Up"
        elif self.__snake_data[0][1]-self.__snake_data[1][1]==-1: return "Down"
        elif self.__snake_data[0][0]-self.__snake_data[1][0]==1: return "Right"
        elif self.__snake_data[0][0]-self.__snake_data[1][0]==-1: return "Left"

    def move_snake_direction(self,string):
        res = self.__snake_data[-1]
        if self._unvalid_move(string): return res
        elif string not in ['Up','Down','Right',"Left"]:
            self._move_straight(self._check_direction())
            return res
        elif string == "Up":
            self.__snake_data = [(self.__snake_data[0][0],self.__snake_data[0][1]+1)] + self.__snake_data
        elif string == "Down":
            self.__snake_data = [(self.__snake_data[0][0], self.__snake_data[0][1] - 1)] + self.__snake_data
        elif string == "Right":
            self.__snake_data = [(self.__snake_data[0][0]+1, self.__snake_data[0][1])] + self.__snake_data
        elif string == "Left":
            self.__snake_data = [(self.__snake_data[0][0] - 1, self.__snake_data[0][1])] + self.__snake_data

        self.__snake_data.pop()
        return res

