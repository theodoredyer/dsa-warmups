class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        direction_map = {
            "north": [0,1],
            "west": [-1,0],
            "south": [0,-1],
            "east": [1,0]
        }

        def redirect(pivot, cur_direction):
            if cur_direction == "north" and pivot == "L" or cur_direction == "south" and pivot == "R":
                return "west"
            if cur_direction == "north" and pivot == "R" or cur_direction == "south" and pivot == "L":
                return "east"
            if cur_direction == "east" and pivot == "L" or cur_direction == "west" and pivot == "R":
                return "north"
            if cur_direction == "east" and pivot == "R" or cur_direction == "west" and pivot == "L":
                return "south"

        cur_direction = "north"
        cur_position = [0,0]

        for ch in instructions:
            if ch == "G":
                cur_position[0] += direction_map[cur_direction][0]
                cur_position[1] += direction_map[cur_direction][1]
            else:
                cur_direction = redirect(ch, cur_direction)
        print(cur_position)
        print(cur_direction)
        for ch in instructions:
            if ch == "G":
                cur_position[0] += direction_map[cur_direction][0]
                cur_position[1] += direction_map[cur_direction][1]
            else:
                cur_direction = redirect(ch, cur_direction)
        print(cur_position)
        print(cur_direction)
        for ch in instructions:
            if ch == "G":
                cur_position[0] += direction_map[cur_direction][0]
                cur_position[1] += direction_map[cur_direction][1]
            else:
                cur_direction = redirect(ch, cur_direction)
        print(cur_position)
        print(cur_direction)
        for ch in instructions:
            if ch == "G":
                cur_position[0] += direction_map[cur_direction][0]
                cur_position[1] += direction_map[cur_direction][1]
            else:
                cur_direction = redirect(ch, cur_direction)
        print(cur_position)
        print(cur_direction)
        return cur_position == [0,0]
            


"""
Set up a 2d mapping of trhe environment and just run through the simulation 
of the robot executing one round of instructions, if the robot ends upn back at the same 
exact location, we know that the robot will perpetually get stuck in a cycle of length 0. 

If we end up at a different location and facing the same direction, we know we are going to 
never converge. 

If we end up at a different location and facing a different direction, we are either about to just 
go straight back home on the next iteration if we are facing 2 turns in a different direction, or
we are going to go in a circle and end up back at home after 4 iterations. 

So if we run the simulation 4 times and we end up back at home, we know the robot just cycles in 
one of these four patterns. 

"""