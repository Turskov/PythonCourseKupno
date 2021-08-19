class Tank:

    color = 0
    speed = 0
    armor = 0

    def config_tank(self):
        self.color = input('Введите цвет танка: ')
        self.speed = input('Введите значение скорости танка: ')
        self.armor = input('Введите значение брони танка: ')
        return [self.color, self.speed, self.armor]

    def re_color_green(self):
        if self.color == 'green':
            print('Покраска танка в зеленый не требуется')
        else:
            self.color = 'green'
            print('Покраска танка в зеленый завершена')
            return self.color
        #х = input('Хотите покрасить танк в зеленый? y/n ')
        #if x == 'y':
            #if self.color == 'green':
                #print('Покраска танка не требуется')
            #else:
                #self.color = 'green'
                #print('Покраска танка в зеленый завершена')
                #return self.color
        #elif x == 'n':
            #print('Ну как хотите!')
        #else:
            #t_34.re_color()


t_34 = Tank()
t_34.config_tank()
t_34.re_color_green()
print(f'Цвет танка Т-34 {t_34.color}')