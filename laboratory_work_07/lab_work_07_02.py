import turtle as tr
from random import uniform
from math import pi

def is_point_inside(val_x, val_y, rad):

    status_flag = 0
    if (((val_x >= 0 and val_y >= 0) or (val_x <= 0 and val_y <= 0)) and (val_x ** 2 + val_y ** 2 <= rad ** 2)) or (val_x <= 0 and val_y >= 0 and (val_y <= val_x + rad)):
        status_flag = 1
    return status_flag

def main():
    rad = float(input("Введите радиус R для фигуры: "))
    
    lims_x = [int(-rad) - 2, int(rad) + 3]
    lims_y = [int(-rad) - 2, int(rad) + 3]
    
    screen_w = 600
    screen_h = screen_w / ((lims_x[1] - lims_x[0]) / (lims_y[1] - lims_y[0]))
    
    tr.setup(screen_w, screen_h, 200, 200)
    tr.reset()
    
    max_trials = 10000
    tr.setworldcoordinates(lims_x[0], lims_y[0], lims_x[1], lims_y[1])
    tr.title("Лабораторная 7 - Задание 2 (Монте-Карло)")
    tr.width(2)
    tr.ht()
    tr.tracer(0, 0)
    
    tr.up()
    hits_count = 0
    
    # Метод Монте-Карло[cite: 48]
    for n in range(max_trials):
        rand_x = uniform(lims_x[0], lims_x[1])
        rand_y = uniform(lims_y[0], lims_y[1])
        tr.goto(rand_x, rand_y)
        
        if is_point_inside(rand_x, rand_y, rad) != 0:
            tr.dot(3, "green")
            hits_count += 1
        else:
            tr.dot(3, "#ffccff")
            
    tr.color("blue", "blue")
    
    tr.up()
    tr.goto(lims_x[0], 0)
    tr.down()
    tr.goto(lims_x[1], 0)
    
    tr.up()
    tr.goto(0, lims_y[1])
    tr.down()
    tr.goto(0, lims_y[0])
    
    tr.up()
    for cur_x in range(lims_x[0], lims_x[1]):
        tr.goto(cur_x, 0.1)
        tr.down()
        tr.goto(cur_x, 0)
        tr.up()
        tr.sety(-0.4)
        tr.write(str(cur_x))
        
    for cur_y in range(lims_y[0], lims_y[1]):
        tr.goto(0, cur_y)
        tr.down()
        tr.goto(0.1, cur_y)
        tr.up()
        tr.setx(0.2)
        tr.write(str(cur_y))
        

    poly_base_y = [0, 0.1, 0, -0.1, 0]
    arrow_start = int(lims_x[1])
    poly_arr_x = [arrow_start, arrow_start - 0.1, arrow_start + 0.3, arrow_start - 0.1, arrow_start]
    
    tr.goto(poly_arr_x[0], poly_base_y[0])
    tr.begin_fill()
    tr.down()
    for i in range(1, 5):
        tr.goto(poly_arr_x[i], poly_base_y[i])
    tr.end_fill()
    
    tr.up()
    tr.goto(arrow_start, -0.7)
    tr.write("X", font=("Arial", 14, "bold"))
    
    arrow_start_y = int(lims_y[1])
    poly_arr_y = [arrow_start_y, arrow_start_y - 0.1, arrow_start_y + 0.3, arrow_start_y - 0.1, arrow_start_y]
    
    tr.up()
    tr.goto(poly_base_y[0], poly_arr_y[0])
    tr.begin_fill()
    tr.down()
    for i in range(1, 5):
        tr.goto(poly_base_y[i], poly_arr_y[i])
    tr.end_fill()
    
    tr.up()
    tr.goto(0.2, arrow_start_y)
    tr.write("Y", font=("Arial", 14, "bold"))
    
    monte_carlo_area = (lims_x[1] - lims_x[0]) * (lims_y[1] - lims_y[0]) * hits_count / max_trials
    
    real_area = (rad ** 2 / 2) * (pi + 1)
    error_perc = (monte_carlo_area / real_area) * 100
    
    tr.goto(rad / 2, rad + 1) # Размещение текста
    fstr = "N={0:8d}\nNf={1:8d}\nSf={2:8.2f}\nEr={3:8.2f}%"
    msg = fstr.format(max_trials, hits_count, monte_carlo_area, error_perc)
    tr.write(msg, font=("Arial", 12, "bold"))
    print(msg)
    
    tr.update()
    tr.mainloop()

if __name__ == "__main__":
    main()