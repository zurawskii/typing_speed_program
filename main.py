# TYPING PROGRAM
import tkinter.scrolledtext
from tkinter import Tk, Label, Text, Button
import random

ARTICLES = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sed accumsan ex, mattis maximus augue. Nullam lobortis in metus quis fermentum. Sed a tellus dui. Aenean suscipit sem faucibus, lacinia neque sit amet, porttitor urna. Donec a quam nisl. Donec sed erat nec justo convallis ullamcorper. Vivamus in ex id metus vestibulum efficitur vel ut mi. Morbi sit amet ligula consequat, luctus metus eu, pulvinar neque. Integer maximus turpis in diam aliquet, luctus viverra ligula condimentum. Vestibulum eu congue arcu. Praesent vestibulum mauris a sem pellentesque ornare. Nulla in iaculis leo. Sed nec tellus elementum, mollis felis at, interdum orci. Suspendisse iaculis efficitur viverra. Nullam maximus facilisis massa efficitur pharetra. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce vehicula sodales varius. Quisque et ex sit amet nulla commodo placerat in sed enim. Vivamus vulputate sagittis nibh, nec fermentum enim dignissim aliquet. Aenean finibus sem.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In finibus venenatis bibendum. Aenean sit amet interdum orci. Nullam vehicula semper erat sed tincidunt. Vivamus placerat, felis sed fermentum luctus, ligula lacus blandit lectus, in pretium velit lacus vitae nibh. Donec eu sem iaculis eros lobortis consectetur vitae ac magna. Maecenas justo neque, faucibus id lobortis non, faucibus vel leo. Suspendisse quis lacus eget massa sollicitudin varius eget in sapien. Sed malesuada faucibus magna, eget tristique orci consequat nec. Aliquam sed nisl est. In enim arcu, sollicitudin vel lacinia non, commodo id enim. Suspendisse potenti. Sed nec metus posuere, auctor quam sed, semper lorem. Curabitur ut nibh sem. Duis ullamcorper metus lacinia elit ultricies accumsan. Vestibulum nisi elit, maximus eu ultrices ullamcorper, varius sit amet nibh. Pellentesque faucibus faucibus nisi, id rhoncus turpis eleifend non. Duis ut facilisis magna. Integer malesuada dictum sapien, eu mollis tellus pharetra nec. Nam ac consectetur.",
    "Aliquam sed nisl est. In enim arcu, sollicitudin vel lacinia non, commodo id enim. Suspendisse potenti. Sed nec metus posuere, auctor quam sed, semper lorem. Curabitur ut nibh sem. Duis ullamcorper metus lacinia elit ultricies accumsan. Vestibulum nisi elit, maximus eu ultrices ullamcorper, varius sit amet nibh. Pellentesque faucibus faucibus nisi, id rhoncus turpis eleifend non. Duis ut facilisis magna. Integer malesuada dictum sapien, eu mollis tellus pharetra nec. Nam ac consectetur. Donec viverra tristique augue, eu placerat elit tempus sit amet. Aenean metus felis, congue id magna quis, tincidunt sagittis libero. Ut eget commodo quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur id nisi a augue interdum fermentum eget nec nunc. Aenean porttitor nisl dictum ipsum vehicula, sed aliquet sem sollicitudin. Suspendisse non mollis nibh. Vestibulum at lorem magna. Maecenas non feugiat purus. Cras nec placerat urna. Praesent tincidunt ipsum felis, nec volutpat odio elementum a. Sed rutrum, velit in eleifend posuere, nisi orci consectetur mi, sit amet iaculis nibh arcu nec orci. Nunc purus dui, hendrerit quis tempor sit amet, tempor et dolor. Fusce tempus ultricies nulla, id elementum elit vestibulum molestie. Sed a molestie mauris. Nam non mi sit amet metus elementum condimentum in eu quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at pretium risus. In tincidunt urna ac est rutrum, non hendrerit ipsum eleifend. Sed dictum feugiat felis eget molestie. Curabitur et eros sed libero mattis tincidunt eu sed lectus. Class aptent taciti sociosqu ad litora torquent.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at convallis turpis. Cras lacinia quis tortor vitae convallis. Suspendisse quis augue fermentum, dapibus ligula non, hendrerit ex. In placerat lacinia tortor, sed accumsan justo ultricies sed. Pellentesque eu dui neque. Vestibulum ullamcorper interdum elementum. Phasellus tempus sapien sed lobortis condimentum. Proin fringilla lorem quis consectetur tincidunt. Quisque tristique nunc sapien, tristique venenatis leo pharetra sed. Curabitur vitae augue libero. Nullam porttitor sapien vehicula sapien aliquam, ac consectetur elit pulvinar. Donec lectus ligula, aliquet ut sem in, hendrerit sodales tellus. Nulla et mi sed arcu aliquet vehicula. Quisque non eleifend orci, vel condimentum elit. Pellentesque aliquet varius augue, sit amet faucibus neque fringilla et. Nullam lacinia arcu eu enim facilisis accumsan. Aliquam erat volutpat. Aliquam erat volutpat. Proin varius nunc sem, vel pretium est molestie in. Fusce interdum purus et congue sagittis. Sed auctor commodo mauris. Vivamus eget mauris fringilla, feugiat.",
    "Vestibulum ultrices bibendum nisi, et imperdiet odio facilisis non. Praesent sit amet neque a nunc mattis placerat. Etiam et augue risus. Maecenas justo augue, aliquam nec vehicula sit amet, imperdiet non sapien. Nam sed mi eget est efficitur malesuada. Cras eget ex tortor. Mauris at ex bibendum, laoreet ligula ultricies, ultrices est. Donec pellentesque venenatis lacus et placerat. Donec odio diam, vulputate vitae varius et, egestas vitae nulla. Nunc euismod elit in condimentum maximus. Curabitur vel justo ut tortor cursus pulvinar nec nec justo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut quis porttitor quam. Nam dapibus massa eget massa consectetur ullamcorper. Pellentesque nunc tortor, porta nec est non, euismod luctus ipsum. Aenean tempus dignissim urna, at porta sem cursus sollicitudin. Nulla luctus convallis nisi id efficitur. Nam feugiat luctus porttitor. Sed libero tortor, fermentum sed sollicitudin ac, malesuada malesuada est. Mauris dignissim risus sed."]

random_article = random.choice(ARTICLES)
word_from_article = random_article.split(" ")
counter = 0
milliseconds = 0
SCORE = 0
game = 1


def retrieve_input():
    global SCORE
    inputValue = str(user_entry.get("1.0", "end-1c"))
    print("The input value:", inputValue)
    split_input = inputValue.split(" ")
    correct_word_counter = 0
    for i in range(0, len(split_input)):
        if word_from_article[i] == split_input[i]:
            correct_word_counter += 1
    SCORE = correct_word_counter
    print("Your score is equal:", correct_word_counter)
    correct_words = Label(text=f"Score: {SCORE}".upper(), fg='#fffcf2', font=("Arial", 14, 'bold'), bg='#eb5e28',
                          border=0)
    correct_words.grid(column=0, row=4, pady=30, columnspan=2, ipady=5, ipadx=15)


def start_timer():
    global counter
    global milliseconds
    if user_entry.get("1.0", "end-1c") != '':
        user_entry.delete(0, 'end')
        SCORE = 0
        global game
        game += 1
    counter = 0
    milliseconds = 0
    update_counter_label()


def update_counter_label():
    global counter, milliseconds

    if counter >= 60:
        retrieve_input()
        return

    if milliseconds % 100 == 0:
        counter += int(milliseconds / 100)
        milliseconds = 0
    time_counter.config(text=f"Time elapsed: {counter}:{milliseconds}".upper(), fg='#fffcf2', bg='#eb5e28', border=0,
                        font=("Arial", 14, 'bold'), padx=7, pady=5)

    milliseconds += 1
    if counter <= 60000:
        window.after(10, update_counter_label)


window = Tk()
window.config(bg='#403d39')
window.geometry("800x1000")
window.title("Typing Speed Test Program")
Label(text="Check your typing speed".upper(), font=('Arial', 24, 'bold'), pady=10, fg='#fffcf2', bg='#403d39').grid(
    column=0,
    row=0, columnspan=2)

text = tkinter.scrolledtext.ScrolledText(window,
                                         wrap=tkinter.WORD,
                                         width=65,
                                         height=20,
                                         font=("Arial", 15),
                                         bg='#343a40',
                                         fg='white',
                                         border=0,
                                         padx=6,
                                         pady=6
                                         )

text.grid(column=0, row=1, pady=10, padx=10, columnspan=2)
text.insert("end", random_article)

# Ukrycie paska przewijania pionowego
text['yscrollcommand'] = lambda *args: None

# Ukrycie paska przewijania poziomego
text['xscrollcommand'] = lambda *args: None

text.config(state='disabled')

user_entry = Text(window, width=70, height=15)
user_entry.grid(column=0, row=2, columnspan=2)

start_time_button = Button(text="Start time".upper(), fg='#fffcf2', font=("Arial", 14, 'bold'), bg='#eb5e28', border=0,
                           command=start_timer)
start_time_button.grid(column=0, row=3, pady=15, ipady=5, ipadx=15)

time_counter = Label(text=f"Time elapsed: {counter}".upper(), fg='#fffcf2', bg='#eb5e28', border=0,
                     font=("Arial", 14, 'bold'), padx=7, pady=5)
time_counter.grid(column=1, row=3)

window.mainloop()
