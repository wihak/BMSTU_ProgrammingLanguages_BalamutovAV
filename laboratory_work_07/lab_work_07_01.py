import turtle as tr
from math import sqrt

def compute_func_y(val_x):

    if val_x < -4:
        return None
    elif -4 <= val_x <= -2:
        val_y = val_x + 3
    elif -2 < val_x <= 4:
        val_y = -val_x / 2
    elif 4 < val_x <= 6:
        val_y = -2
    elif 6 < val_x <= 10:
        val_y = sqrt(4 - (val_x - 8) ** 2) - 2
    else:
        return None
    return val_y

def draw_axis_line(axis_limits, axis_name='X'):
    start_limit = axis_limits[0]
    end_limit = axis_limits[1]
    
    tr.up()
    if axis_name == 'X':
        point_b = [start_limit, 0]
        point_e = [end_limit, 0]
    else:
        point_b = [0, start_limit]
        point_e = [0, end_limit]
        
    tr.goto(point_b)
    tr.down()
    tr.goto(point_e)

def draw_axis_marks(axis_limits, axis_name='X'):
    start_limit = axis_limits[0]
    end_limit = axis_limits[1]
    
    tr.up()
    for t in range(start_limit, end_limit):
        if axis_name == 'X':
            point_b = [t, 0]
            point_e = [t, 0.2]
            point_w = [t, -0.5]
        else:
            point_b = [0, t]
            point_e = [0.2, t]
            point_w = [0.2, t]
            
        tr.goto(point_b)
        tr.down()
        tr.goto(point_e)
        tr.up()
        tr.goto(point_w)
        tr.write(str(t))

def draw_axis_arrow(axis_limits, axis_name='X'):
    arr_x = [0.1, 0, -0.1]
    arr_y = [-0.1, 0.3, -0.1]
    
    tr.up()
    tr.goto(0, 0)
    tr.begin_poly()

    for i in range(3):
        tr.goto(arr_x[i], arr_y[i])
    tr.end_poly()
    
    poly_shape = tr.get_poly()
    tr.register_shape("customArrow", poly_shape)
    tr.resizemode("customArrow")
    tr.shapesize(1, 2, 1)
    
    if axis_name == 'X':
        tr.tiltangle(0)
        tr.goto(axis_limits[1] + 0.2, 0)
        point_w = [int(axis_limits[1]), -1.0]
    else:
        tr.tiltangle(90)
        tr.goto(0, axis_limits[1] + 0.2)
        point_w = [0.2, int(axis_limits[1])]
        
    tr.stamp()
    tr.goto(point_w)
    tr.write(axis_name, font=("Arial", 14, "bold"))

def main():
    lims_x = [-6, 12]
    lims_y = [-4, 4]
    
    screen_width = 800
    screen_height = screen_width / ((lims_x[1] - lims_x[0]) / (lims_y[1] - lims_y[0]))
    
    tr.setup(screen_width, screen_height)
    tr.reset()
    
    total_iters = 1000
    tr.setworldcoordinates(lims_x[0], lims_y[0], lims_x[1], lims_y[1])
    tr.title("Лабораторная 7 - Задание 1 (Вариант 5)")
    tr.width(2)
    tr.color("blue", "blue")
    tr.ht()
    tr.tracer(0, 0)
    
    draw_axis_line(lims_x, 'X')
    draw_axis_marks(lims_x, 'X')
    draw_axis_arrow(lims_x, 'X')
    
    draw_axis_line(lims_y, 'Y')
    draw_axis_marks(lims_y, 'Y')
    draw_axis_arrow(lims_y, 'Y')
    
    tr.color("green")
    tr.width(3)
    step_val = (lims_x[1] - lims_x[0]) / total_iters
    
    current_x = lims_x[0]
    current_y = compute_func_y(current_x)
    
    if current_y is None:
        tr.up()
        tr.goto(current_x, 0)
    else:
        tr.goto(current_x, current_y)
        tr.down()
        
    while current_x <= lims_x[1]:
        current_x = current_x + step_val
        current_y = compute_func_y(current_x)
        if current_y is None:
            tr.up()
            continue
        else:
            tr.goto(current_x, current_y)
            tr.down()
            
    tr.update()
    tr.mainloop()

if __name__ == "__main__":
    main()