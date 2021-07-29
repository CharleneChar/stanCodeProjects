"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1200 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    Execute a game of clearing bricks with a bouncing ball in a window
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.ball_x_speed()
    vy = graphics.ball_y_speed()
    # Animate the bouncing ball
    while True:
        # Check to see whether the game should exit
        if graphics.bricks_cleared_count == graphics.brick_rows*graphics.brick_cols:
            break
        if graphics.ball.y > graphics.window.height:
            lives -= 1
            if 0 < lives <= 3:
                graphics.reset()
                vx = graphics.ball_x_speed()
                vy = graphics.ball_y_speed()
            else:
                break
        if graphics.animation_start:
            graphics.ball.move(vx, vy)
        # Check for ball collision with object in window (SOS: Can this be more efficient @@? )
        top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        top_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y)
        bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius * 2)
        bottom_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                                     graphics.ball.y + graphics.ball_radius * 2)
        if top_left is not None:
            graphics.ball_clear_brick(top_left)
            vy = graphics.ball_y_speed()
        elif top_right is not None:
            graphics.ball_clear_brick(top_right)
            vy = graphics.ball_y_speed()
        elif bottom_left is not None:
            graphics.ball_clear_brick(bottom_left)
            vy = graphics.ball_y_speed()
        elif bottom_right is not None:
            graphics.ball_clear_brick(bottom_right)
            vy = graphics.ball_y_speed()
        # Limit the boundaries where the bouncing ball can go
        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            vx = -vx
        if graphics.ball.y < 0:
            vy = -vy
        # Make sure the ball would bounce back when hitting the paddle instead of getting stuck on the paddle
        if graphics.window.height - graphics.paddle_offset > graphics.ball.y \
                > graphics.paddle.y - graphics.ball_radius*2 \
                and graphics.paddle.x - graphics.ball_radius*2 < graphics.ball.x \
                < graphics.paddle.x + graphics.paddle.width:
            graphics.ball_from_paddle()
        # Avoid gradually lower speed of the bouncing process (caused by the above collision check process)
        if graphics.bricks_cleared_count <= 20:
            pause(FRAME_RATE)
        elif 20 < graphics.bricks_cleared_count <= 50:
            pause(FRAME_RATE // 4)
        else:
            pause(FRAME_RATE // 8)


if __name__ == '__main__':
    main()
