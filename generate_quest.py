import random as rand


class Example:
    def __init__(self, result=None, answer=None, change=None):
        self.solve = 'Решите уравнение'
        self.result = result
        self.answer = answer
        self.str_example = None
        self.change = change
        self.score = 1

    def generate_5_1(self):
        gen_type = rand.randint(1, 2)
        ready = False
        self.score = 1
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(10, 50)
            numb_two = rand.randint(10, 50)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(10, 50)
                numb_two = rand.randint(10, 50)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generate_5_2(self):
        self.score = 3
        gen_type = rand.randint(1, 4)
        ready = False
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(50, 200)
            numb_two = rand.randint(50, 200)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(50, 100)
                numb_two = rand.randint(50, 100)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            numb_one = rand.randint(2, 10)
            numb_two = rand.randint(2, 10)
            self.result = numb_one * numb_two
            self.str_example = str(numb_one) + ' X ' + str(numb_two) + ' ='
        elif gen_type == 4:
            ready = True
            while ready:
                self.result = rand.randint(2, 10)
                numb_one = rand.randint(2, 10)
                numb_two = numb_one * self.result
                her = numb_two % numb_one
                if her == 0:
                    ready = False
            self.str_example = str(numb_two) + ' : ' + str(numb_one) + ' ='

    def generate_5_3(self):
        self.score = 5
        gen_type = rand.randint(1, 4)
        ready = False
        # Сложение вычитание нат. чисел
        if gen_type == 1:
            numb_one = rand.randint(100, 300)
            numb_two = rand.randint(100, 200)
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            while not ready:
                numb_one = rand.randint(100, 200)
                numb_two = rand.randint(90, 130)
                if numb_one - numb_two > 0:
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            numb_one = rand.randint(5, 20)
            numb_two = rand.randint(2, 10)
            self.result = numb_one * numb_two
            self.str_example = str(numb_one) + ' X ' + str(numb_two) + ' ='
        elif gen_type == 4:
            ready = True
            while ready:
                self.result = rand.randint(5, 15)
                numb_one = rand.randint(3, 10)
                numb_two = numb_one * self.result
                her = numb_two % numb_one
                if her == 0:
                    ready = False
            self.str_example = str(numb_two) + ' : ' + str(numb_one) + ' ='

    def generate_6_1(self):
        self.score = 1
        gen_type = rand.randint(1, 2)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one + numb_two < 10 and len(str(numb_one + numb_two)) < 10:
                    ready = True
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t_1 = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(1, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 10 and float(numb_one_t_1) > float(
                        numb_one_t):
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generate_6_2(self):
        self.score = 3
        gen_type = rand.randint(1, 2)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(4, 10))
                numb_one_t = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(1, 10))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one + numb_two < 10 and len(str(numb_one + numb_two)) < 10:
                    ready = True
            self.result = numb_one + numb_two
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(4, 20))
                numb_one_t_1 = str(rand.randint(1, 10))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(10, 100))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 10 and float(numb_one_t_1 * 10) > float(
                        numb_one_t):
                    ready = True
            self.result = numb_one - numb_two
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='

    def generate_6_3(self):
        self.score = 5
        gen_type = rand.randint(1, 10)
        if gen_type == 1:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(10, 30))
                numb_one_t = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t_1 = str(rand.randint(100, 1000))
                numb_two = float(numb_one_o + '.' + numb_one_t_1)
                if numb_one + numb_two < 100 and len(str(numb_one + numb_two)) < 1000 and int(numb_one_t) * 10 + int(
                        numb_one_t_1) < 1000:
                    ready = True
            self.result = numb_one + numb_two
            if len(str(self.result)) > 8:
                self.result = float(format(self.result, '.3f'))
            self.str_example = str(numb_one) + ' + ' + str(numb_two) + ' ='
        elif gen_type == 2:
            ready = False
            while not ready:
                numb_one_o = str(rand.randint(10, 30))
                numb_one_t_1 = str(rand.randint(10, 100))
                numb_one = float(numb_one_o + '.' + numb_one_t_1)
                numb_one_o = str(rand.randint(2, 10))
                numb_one_t = str(rand.randint(100, 1000))
                numb_two = float(numb_one_o + '.' + numb_one_t)
                if numb_one - numb_two > 0 and len(str(numb_one - numb_two)) < 1000 and float(
                        numb_one_t_1) / 10 > float(
                    numb_one_t) / 100:
                    ready = True
            self.result = numb_one - numb_two
            if len(str(self.result)) > 5:
                self.result = float(format(self.result, '.3f'))
            self.str_example = str(numb_one) + ' - ' + str(numb_two) + ' ='
        elif gen_type == 3:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a + b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' + ' + str(b) + ' = ' + str(c)
        elif gen_type == 4:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a - b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' - ' + str(b) + ' = ' + str(c)
        elif gen_type == 5:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * (a * (-1)) + b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' + ' + str(b) + ' = ' + str(c)
        elif gen_type == 6:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 20)
            b = rand.randint(20, 50)
            c = x * a * (-1) + b * (-1)
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' - ' + str(b) + ' = ' + str(c)
        elif gen_type == 7:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a - b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)
        elif gen_type == 8:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 25)
            b = rand.randint(20, 50)
            c = x * a + b
            self.str_example = self.solve + ' ' + str(a) + 'x' + ' = ' + str(c) + ' - ' + str(b)
        elif gen_type == 9:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 15)
            b = rand.randint(20, 40)
            c = x * a * (-1) - b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)
        elif gen_type == 10:
            x = rand.randint(1, 10)
            self.result = x
            a = rand.randint(2, 15)
            b = rand.randint(20, 40)
            c = x * a * (-1) + b
            self.str_example = self.solve + ' -' + str(a) + 'x' + ' = ' + str(c) + ' + ' + str(b)

    def bool_pr(self, answer):
        if self.result == float(answer):
            return True
        else:
            return False

    def gen_ex(self):
        if self.change[0] == 5:
            if self.change[1] == 1:
                self.generate_5_1()
            elif self.change[1] == 2:
                self.generate_5_2()
            elif self.change[1] == 3:
                self.generate_5_3()
        elif self.change[0] == 6:
            if self.change[1] == 1:
                self.generate_6_1()
            elif self.change[1] == 2:
                self.generate_6_2()
            elif self.change[1] == 3:
                self.generate_6_3()
