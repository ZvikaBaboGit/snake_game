from game_parameters import get_random_bomb_data


COLOR_1 = "red"
COLOR_2 = "orange"
def chack_if_new_location(x,y,lst_1,lst_2):
    if (x,y) in lst_1:
        return
    else:
        for lst in lst_2:
            for i in lst:
                if i == (x,y):
                   return
        lst_1.append((x,y))

class Bomb:
    def __init__(self):
        self.bomb = get_random_bomb_data()
        self.__location = (self.bomb[0],self.bomb[1])
        self.__radius = self.bomb[2]
        self.__time = self.bomb[3]
        self.__color_before_explode = COLOR_1
        self.__color_after_explode = COLOR_2
    def get_bomb_location(self):
        return self.__location
    def get_bomb_radius(self):
        return self.__radius
    def get_bomb_time(self):
        return self.__time
    def create_new_bomb(self):
        self.bomb = get_random_bomb_data()
    def get_bomb_color_before_explode(self):
        return self.__color_before_explode
    def get_bomb_color_after_explode(self):
        return  self.__color_after_explode
    def get_radius_location_after_explode(self):
        counter = 0
        location_list = [[self.__location]]
        while counter <= self.__radius:
            temp_list = []
            for t in location_list[counter]:
                up_cell,down_cell,right_cell,left_cell = (t[0]+1,t[1]),(t[0]-1,t[1]),(t[0],t[1]+1),(t[0],t[1]-1)
                chack_if_new_location(up_cell[0],up_cell[1],temp_list,location_list)
                chack_if_new_location(down_cell[0],down_cell[1],temp_list,location_list)
                chack_if_new_location(right_cell[0],right_cell[1],temp_list,location_list)
                chack_if_new_location(left_cell[0],left_cell[1],temp_list,location_list)
            location_list.append(temp_list)
            counter+=1
        return location_list




