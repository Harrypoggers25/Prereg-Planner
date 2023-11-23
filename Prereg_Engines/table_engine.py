import copy

class TableEngine():
    def __init__(self):
        self.vcombinations = []
        self.vvrects = []
        self.select_index = 0

    def setVCombinations(self, vcombinations):
        self.vcombinations = vcombinations

        for combinations in self.vcombinations:
            n_vrects = []
            for table in combinations:
                n_rects = []
                for rects in table.vrects:
                    n_rects.extend(copy.deepcopy(rects)) # same list, different reference
                n_vrects.append(n_rects)
            self.vvrects.append(n_vrects)

    def selectCombinations(self, index):
        self.select_index = index

    def getResizedCombinations(self, SCREEN_SIZE_X, SCREEN_SIZE_Y):
        n_vrects = self.vvrects[self.select_index]
        n_lower = n_upper = n_left = n_right = 0

        for rects in n_vrects:
            for rect in rects:
                if n_lower == 0 and n_upper == 0 and n_left == 0 and n_right == 0:
                    n_lower = rect.y
                    n_upper = rect.y + rect.h
                    continue
                if rect.y < n_lower:
                    n_lower = rect.y
                if rect.y + rect.h > n_upper:
                    n_upper = rect.y + rect.h
                if rect.x < n_left:
                    n_left = rect.x
                if rect.x > n_right:
                    n_right = rect.x
        N_W = SCREEN_SIZE_X / (n_right - n_left + 1)  # day width constant
        N_H = SCREEN_SIZE_Y / (n_upper - n_lower)     # time height constant

        for i in range(len(self.vcombinations[self.select_index])):
            for j in range(len(self.vcombinations[self.select_index][i].vrects)):
                size_rects = len(self.vcombinations[self.select_index][i].vrects[j])
                for k in range(size_rects):
                    l = j * size_rects + k
                    rect = self.vcombinations[self.select_index][i].vrects[j][k]
                    
                    rect.x = n_vrects[i][l].x * N_W
                    rect.y = (n_vrects[i][l].y - n_lower) * N_H
                    rect.w = N_W
                    rect.h = n_vrects[i][l].h * N_H

        return self.vcombinations[self.select_index]