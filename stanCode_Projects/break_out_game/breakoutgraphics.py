"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    A window contains bricks, a paddle, and a ball for animation use.
    """
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        """
        Create animation settings, including a window, bricks, a paddle, and a ball

        :param ball_radius: The radius of the ball
        :param paddle_width: The width of the paddle
        :param paddle_height: The height of the paddle
        :param paddle_offset: The space between the bottom of the window and the paddle
        :param brick_rows: The number of the rows with bricks
        :param brick_cols: The number of the columns with bricks
        :param brick_width: The width of any of the bricks
        :param brick_height: The height of any of the bricks
        :param brick_offset: The space between the top of the window and any of the bricks on first row
        :param brick_spacing: The space between any two of the bricks
        :param title: The title of the window
        """

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle,
                        (self.window_width-self.paddle.width)/2,
                        self.window_height-self.paddle_offset-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(2*self.ball_radius, 2*self.ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window_width-self.ball.width)/2, (self.window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_initial_speed()

        # Initialize our mouse listeners
        self.animation_start = False
        onmouseclicked(self.click)
        onmousemoved(self.control_paddle)

        # Draw bricks
        self.brick_offset = brick_offset
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        two_rows = (self.brick_height+self.brick_spacing)*self.brick_rows//(self.brick_rows//2)
        for i in range(0, (self.brick_width+self.brick_spacing)*self.brick_cols,
                       self.brick_width+self.brick_spacing):
            for j in range(0, two_rows,
                           self.brick_height+self.brick_spacing):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.window.add(self.brick, i, j+self.brick_offset)
        for i in range(0, (self.brick_width+self.brick_spacing)*self.brick_cols,
                       self.brick_width+self.brick_spacing):
            for j in range(0, two_rows,
                           self.brick_height+self.brick_spacing):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'orange'
                self.window.add(self.brick, i, j+self.brick_offset+two_rows)
        for i in range(0, (self.brick_width+self.brick_spacing)*self.brick_cols,
                       self.brick_width+self.brick_spacing):
            for j in range(0, two_rows,
                           self.brick_height+self.brick_spacing):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                self.window.add(self.brick, i, j+self.brick_offset+two_rows*2)
        for i in range(0, (self.brick_width+self.brick_spacing)*self.brick_cols,
                       self.brick_width+self.brick_spacing):
            for j in range(0, two_rows,
                           self.brick_height+self.brick_spacing):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'green'
                self.window.add(self.brick, i, j+self.brick_offset+two_rows*3)
        for i in range(0, (self.brick_width+self.brick_spacing)*self.brick_cols,
                       self.brick_width+self.brick_spacing):
            for j in range(0, two_rows,
                           self.brick_height+self.brick_spacing):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                self.window.add(self.brick, i, j+self.brick_offset+two_rows*4)

        # Count how many bricks have been cleared through getting hit by the ball
        self.bricks_cleared_count = 0

        # Count how many bricks have been cleared
        self.__bc = GLabel('Bricks Cleared: ' + str(self.bricks_cleared_count))
        self.window.add(self.__bc, 5, self.window_height-5)

    def click(self, event):
        """
        Start the animation of the bouncing ball
        """
        self.animation_start = True

    def control_paddle(self, mouse):
        """
        Control the movement of the paddle with our mouse
        """
        if self.window.width > mouse.x + self.paddle.width/2 > self.paddle.width:
            self.window.add(self.paddle, mouse.x - self.paddle.width / 2,
                            self.window.height - self.paddle_offset
                            - self.paddle.height)

    def ball_initial_speed(self):
        """
        Assign a random speed for the bouncing ball
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        # Avoid same, boring moving speed
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def ball_x_speed(self):
        """
        Get x speed of ball
        :return: int, x speed
        """
        return self.__dx

    def ball_y_speed(self):
        """
        Get y speed of ball
        :return: int, y speed
        """
        return self.__dy

    def ball_from_paddle(self):
        """
        Position the bouncing ball right on the paddle
        """
        self.ball.y = self.paddle.y - self.ball_radius*2

    def ball_clear_brick(self, object_in_window):
        """
        Remove only bricks from the window (not the paddle)
        :param object_in_window: an GObject, any of the bricks, the paddle, or anything the ball touch
        """
        if self.ball.y < self.brick_offset + (self.brick_height + self.brick_spacing) * self.brick_rows:
            self.window.remove(object_in_window)
            self.bricks_cleared_count += 1
            # (Alternative of avoiding lower speed: use + 0.01 to increase speed every time it clears a brick)
            self.__dy = - self.__dy
        elif self.ball.y > self.paddle.y + self.paddle.height:
            self.__dy = self.__dy
        else:
            self.__dy = - self.__dy
        self.__bc.text = 'Bricks Cleared: ' + str(self.bricks_cleared_count)

    def reset(self):
        """
        Reset the settings of the ball before it starts to bounce
        """
        self.window.add(self.ball, (self.window_width-self.ball.width)/2, (self.window_height-self.ball.height)/2)
        self.animation_start = False
        self.ball_initial_speed()
