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
                    n_rects.extend(rects)
                n_vrects.append(n_rects)
            self.vvrects.append(n_vrects)

    def selectCombinations(self, index): # UNUSED
        self.select_index = index

    def getResizedRect(self, SCREEN_SIZE_X, SCREEN_SIZE_Y):
        vrects = self.vvrects[self.select_index].copy()
        n_lower = n_upper = n_left = n_right = 0

        for rects in vrects:
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

        for i in range(len(vrects)):
            for j in range(len(vrects[i])):
                vrects[i][j].x = vrects[i][j].x * N_W
                vrects[i][j].y = (vrects[i][j].y - n_lower) * N_H
                vrects[i][j].w = N_W
                vrects[i][j].h = vrects[i][j].h * N_H

        return vrects
        # for tbl_combinations in self.vcombinations:
        #     # get bounds => dimension constants
        #     n_lower = 0
        #     n_upper = 0
        #     n_left = 0
        #     n_right = 0
        #     for tbl_course in tbl_combinations:
        #         for rects in tbl_course.vrects:
        #             for rect in rects:
        #                 if n_lower == 0 and n_upper == 0 and n_left == 0 and n_right == 0:
        #                     n_lower = rect.y
        #                     n_upper = rect.y + rect.h
        #                     continue
        #                 if rect.y < n_lower:
        #                     n_lower = rect.y
        #                 if rect.y + rect.h > n_upper:
        #                     n_upper = rect.y + rect.h
        #                 if rect.x < n_left:
        #                     n_left = rect.x
        #                 if rect.x > n_right:
        #                     n_right = rect.x
        #     N_W = SCREEN_SIZE_X / (n_right - n_left + 1)  # day width constant
        #     N_H = SCREEN_SIZE_Y / (n_upper - n_lower)     # time height constant

        #     for i in range(len(tbl_combinations)):
        #         for j in range(len(tbl_combinations[i].vrects)):
        #             for k in range(len(tbl_combinations[i].vrects[j])):
        #                 n_x = tbl_combinations[i].vrects[j][k].x
        #                 n_y = tbl_combinations[i].vrects[j][k].y
        #                 n_h = tbl_combinations[i].vrects[j][k].h

        #                 tbl_combinations[i].vrects[j][k].x = n_x * N_W
        #                 tbl_combinations[i].vrects[j][k].y = n_y * N_H
        #                 tbl_combinations[i].vrects[j][k].w = N_W
        #                 tbl_combinations[i].vrects[j][k].h = n_h * N_H