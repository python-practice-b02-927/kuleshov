import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def add(point_1, point_2):
    """Return the sum of point_1 and point_2"""
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    """Return the result of subtracting point_2 from point_1"""
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return new_point


def absolute(v):
    """Return the magnitude of vector 'v'"""
    ab = (v.x**2 + v.y**2)**0.5
    return ab


def move_ball(ball, vel):
    """Move the ball according to its velocity"""
    ball.move(vel.x, vel.y)


def update_coords(coords, velocity):
    """Update coordinates according to velocity"""
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    """Update velocity according to acceleration"""
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords, velocity, I, m1, m2):
    """Update acceleration of the selected ball according to the conditions of the system"""
    diff = sub(ball_coords, center_coords)
    distance = absolute(diff)
    g = 1
    vel = absolute(velocity)
    beta = g * (m1 * distance - m2 * distance / 2) * diff.x / distance / I
    an = gr.Point((-1) * diff.x * vel**2 / distance**2, (-1) * diff.y * vel**2 / distance**2)
    at = gr.Point(beta * (-1) * diff.y, beta * diff.x)
    return add(an, at)


def velocity2(vel1):
    """Return the velocity of the second ball depending on the velocity of the first one"""
    vel2 = gr.Point((-1)*vel1.x*1/2, (-1)*vel1.y*1/2)
    return vel2


def main():
    coords1 = gr.Point(400, 600)
    coords2 = gr.Point(400, 300)
    center = gr.Point(400, 400)
    velocity1 = gr.Point(5, 0)
    r1 = 20
    r2 = 10
    r = 5
    m1 = 400
    m2 = 50

    I = m1 * absolute(sub(coords1, center)) ** 2 + m2 * absolute(sub(coords2, center)) ** 2

    connecting_line = gr.Line(coords1, coords2)
    connecting_line.setFill('black')
    connecting_line.setWidth(2)
    connecting_line.draw(window)

    ball1 = gr.Circle(coords1, r1)
    ball1.setFill('black')
    ball1.draw(window)

    ball2 = gr.Circle(coords2, r2)
    ball2.setFill('black')
    ball2.draw(window)

    center_ball = gr.Circle(center, r)
    center_ball.setFill('black')
    center_ball.draw(window)

    while True:
        coords1 = update_coords(coords1, velocity1)
        coords2 = update_coords(coords2, velocity2(velocity1))
        connecting_line.undraw()
        connecting_line = gr.Line(coords1, coords2)
        connecting_line.setFill('black')
        connecting_line.setWidth(2)
        connecting_line.draw(window)

        move_ball(ball1, velocity1)
        move_ball(ball2, velocity2(velocity1))
        acceleration = update_acceleration(coords1, center, velocity1, I, m1, m2)
        velocity1 = update_velocity(velocity1, acceleration)

        gr.time.sleep(0.02)


main()



