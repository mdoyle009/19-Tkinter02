import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()

frame1 = tk.Frame(bg="yellow", relief="raised", borderwidth=5)
frame1.pack()
label1 = tk.Label(master=frame1, text="Wahahaha! I'm in Frame 1!", bg="#FDFDAA")
label1.pack()
button = tk.Button(master=frame1, text="Click if Frame 1 is superior", bg="#FDFDAA")
button.pack()
entry = tk.Entry(master=frame1, width=25, bg="#FDFDAA")
entry.insert("0", "Frame 1 is better because...")
entry.pack()

frame2 = tk.Frame(bg="blue", relief="sunken", borderwidth=5)
frame2.pack()
label2 = tk.Label(master=frame2, text="Sadly this is Frame 2 :(", bg="#9DD9F3")
label2.pack()
text = tk.Text(master=frame2, bg="#9DD9F3")
text.insert("1.0", "I have a lot to say about Frame 2. It's sad. Lonely.")
text.insert("2.0", "\nMaybe one day I'll have a shot at Frame 0. But for now, I sit here.")
text.pack()

window.mainloop()
