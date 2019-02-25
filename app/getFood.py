class Map():
    #creates empty grid
    #0 is empty, 1 is food, 2 is snake, 3 is potential snake
    def makeMap(self, data, size):
        # layout = []
        # for i in range(0, size):
            # column = []
            # for j in range(0, size):
                # column.append(0)
            # layout.append(column)
        sizeFull = size + 1
        layout = [[0 for x in range(0, sizeFull)] for y in range(0, sizeFull)]
        for n in range(0, sizeFull):
            for o in range(0, sizeFull):
                x = n
                y = o
                layout[x][y] = 0
        #fill in food locations
        foodLength = len(data['board']['food']) #- 1
        for k in range(0, foodLength):
            x = data['board']['food'][k]['x']
            y = data['board']['food'][k]['y']
            layout[x][y] = 1
        numSnakes = len(data['board']['snakes'])# - 1
        print(numSnakes)
        for l in range(0, numSnakes):
            snakeLength = len(data['board']['snakes'][l])# - 1
            print(snakeLength)
            print(data['board']['snakes'][0]['body'][0]['x'])
            x = data['board']['snakes'][l]['body'][0]['x']
            y = data['board']['snakes'][l]['body'][0]['y']
            layout[x][y] = 2
            x = x + 1
            if x < sizeFull:
                layout[x][y] = 3
            x = x - 2
            if x >= 0:
                layout[x][y] = 3
            x = x + 1
            y = y + 1
            if y < sizeFull:
                layout[x][y] = 3
            y = y - 2
            if y >= 0:
                layout[x][y] = 3
            y = y + 1
            for m in range(1, snakeLength):
                x = data['board']['snakes'][l]['body'][m]['x']
                y = data['board']['snakes'][l]['body'][m]['y']
                layout[x][y] = 2
        return layout