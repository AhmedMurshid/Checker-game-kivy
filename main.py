from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pathlib import Path
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout



from kivy.uix.tabbedpanel import TabbedPanel

Window.size = (800,800)

kv = ('''
<MenuScreen>:
    
    canvas.before:
        Rectangle:
    
            pos: self.pos
            size: self.size
    GridLayout:
        rows:2
        pos_hint: {'center_x': .5, 'center_y': .5}
        Label:
            font_size: 78
            font_name: 'fonts/blocky'
            color: (3,2,0)
            text:
                """Grade This!"""
                
        GridLayout:
            cols: 3
            padding:dp(100) # padding: [dp(20),dp(10),dp(20),dp(10)]
            size_hint: 1,.51
            Button:
                text: 'Checker game!'
                on_press: root.manager.current = 'play_game' #; app.on_pre_enter()
            
            Button:
                text: 'How to use'
                on_press: root.manager.current = 'howto'
            
            Button:
                text: 'About'
                on_press: root.manager.current = 'about'

<Button@Button>: 
    size_hint: .1, .1

<Main_game_area>:
    canvas:
        Color:
            rgba: (1, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size           
    grid: grid
    button2: 
        button2
    GridLayout:
        rows:2
        GridLayout:
            cols:2
            size_hint: .1,.1
            id: button2
            Label:
                font_size: 88
                font_name: 'fonts/blocky'
                text: "its players 1 turn."
                #pos_hint: {0, 100}
            
        GridLayout:
            rows: 8
            cols: 8
            padding:dp(0) # padding: [dp(20),dp(10),dp(20),dp(10)]
            #size_hint: 1,1
            pos_hint: {'center_x': 0, 'center_y': 0}
            id: grid

        
    
<About>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'img/words.jpg'

    GridLayout:
        rows:2
        AsyncImage:
            
            source: 'img/me.jpg'
            size_hint: .5,.2
        GridLayout:
            rows:2
            Label:
                text:
                    """Created - May 31,2022\n
                    -\n
                    -\n
                    Links:\n
                    https://github.com/AhmedMurshid \n
                    -\n
                    hwww.linkedin.com/in/ahmed001a"""
    
            Button:
                size_hint: .1,.1
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            
        
''')


class MenuScreen(Screen):
    pass
class How_to_play(Screen):
    pass
class About(Screen):
    pass

class Main_game_area(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.click_counts = {}
        self.moves = []
        self.squares = []
        self.piece_image = Image(source='black.png')


        startB = Button(text='<-')
        #button3 = self.on_pre_enter()
        self.button2.add_widget(startB)

        #startB.bind(on_press=lambda : self.on_start(button3))
    def handle_piece_movement(self, box):
        # Determine which square was clicked and handle the piece movement accordingly
        square_id = box
        print(f'Square {square_id.text} was clicked!')
    
    #box = ObjectProperty(None)
    def on_start(self, button):
        #button = self.on_pre_enter()
        piece = Image(source='black.png')
        print("clicked")
        
        # Add the piece widget as a child of the button widget
        if button.text == '1,2':
            button.add_widget(piece,index=0)
            print(button.text)
        if button.text == '1,4':
            button.add_widget(piece,index=0)
        if button.text == '1,6':
            button.add_widget(piece,index=0)
        if button.text == '1,8':
            button.add_widget(piece,index=0)



    def on_pre_enter(self):
        grid = GridLayout()

        for row in range(8):
            for col in range(8):
                coord = f'{row+1},{col+1}'
                square = Button(text=coord)
                self.squares.append(square)

                #row, col = coord.split(',')

                square.id = f'square_{row}_{col}'


                # Set the button's background color to red if the row and column indices are both odd or both even, otherwise set it to white
                if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                    square.background_color = (1, 0, 0, 1)
                elif row < 3:
                    square.background_color = (1, 1, 1, 1)
                self.click_counts[square] = 0
               
            
                square.bind(on_press=self.button_pressed)
                self.grid.add_widget(square)
                piece = Image(source='black.png')
        
        
        return square
                
                # print(self.grid.ids)
                # print(square.text)

        
                
    # def add_pieces(self, button):
    #     piece = Image(source='black.png')
    #     button.add_widget(piece)
    # def button_pressed(self, button):
    #     # Print the text of the button that was pressed
    #     self.click_counts[button] += 1
    #     print(f'Button {button.text} was pressed {self.click_counts[button]} time')
    #     piece = Image(source='black.png')
    #     button.add_widget(piece)

    #     if button.text == '7,7':
    #         #piece.size_hint = (.1, .1)
    #         piece.pos = button.pos
    #         #int(str(row,col)) = button.text.split(',')
    #         row_str, col_str = button.text.split(',')
    #         row = int(row_str)
    #         col = int(col_str)
    #         button.text = f'{row,col}'
    #         print(row,"and",col)
    #     elif button.text == '8,8':
    #         #button.text = '7,7'
    #         piece.pos = button.pos
    def button_pressed(self, square):
        # Print the text of the square that was pressed
        print(f'square {square.text} was pressed')

        # Create a new piece widget        
        # Add the piece widget as a child of the button widget
        # button.add_widget(piece)

        # # Set the position of the piece widget to the position of the button widget
        # piece.pos = button.pos
        # self.moves.append(button)
        # print(self.moves)
        for i in range(len(self.squares)):
            if square.text == '1,2':
                self.piece_image.pos = square.pos
                square.add_widget(self.piece_image)
                print(square.text)
            if square.text == '1,4':
                self.piece_image.pos = square.pos
                square.add_widget(self.piece_image)
            if square.text == '1,6':
                self.piece_image.pos = square.pos
                square.add_widget(self.piece_image)
            if square.text == '1,8':
                self.piece_image.pos = square.pos
                square.add_widget(self.piece_image)
        

    def move_piece(self, from_button, to_button):
        # Find the image widget that is a child of the from_button
        from_image = None
        for child in from_button.children:
            if isinstance(child, Image):
                from_image = child
                break

        # Remove the image widget from the from_button
        from_button.remove_widget(from_image)

        # Add the image widget to the to_button
        to_button.add_widget(from_image)

        # Update the position of the image widget to match the position of the to_button
        from_image.pos = to_button.pos


        
    # def nextMove(self, self.button_pressed(button),button):
    #     if self.click_counts[button] == 1:



        
           # self.box.add_widget(button) #added to the grid
        # Check if the square is occupied by a piece
        # new_var = if square_id in pieces:
        # if square_id in pieces:
        #     print(f'Square {square_id} is occupied by a {pieces[square_id]}')
        # else:
        #     print(f'Square {square_id} is not occupied')






#df = pd.DataFrame(index=['row 1','row 2']col_names = ['Names', 'weights'])

class MyApp(App):
    #avg_num = StringProperty()
    
    def build(self):
        
        Builder.load_string(kv)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Main_game_area(name='play_game'))
        sm.add_widget(How_to_play(name='howto'))
        sm.add_widget(About(name='about'))
    
        return sm
if __name__ == '__main__':
    MyApp().run()
