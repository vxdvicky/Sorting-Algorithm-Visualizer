import tkinter as tk
from tkinter import ttk
import random
import time

# ---------------- ROOT WINDOW ----------------
root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("1000x550")
root.config(bg="#1e1e2f")

# ---------------- VARIABLES ----------------
array = []
array_size = tk.IntVar(value=40)
speed = tk.DoubleVar(value=0.05)
algo = tk.StringVar(value="Bubble Sort")

# ---------------- CANVAS ----------------
canvas = tk.Canvas(
    root,
    width=900,
    height=380,
    bg="#2a2a3d",
    highlightthickness=0
)
canvas.pack(pady=20)

# ---------------- FUNCTIONS ----------------
def generate_array():
    global array
    array = [random.randint(20, 350) for _ in range(array_size.get())]
    draw_array(array, ["#4fc3f7"] * len(array))


def draw_array(arr, color):
    canvas.delete("all")
    bar_width = 900 / len(arr)

    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = 380 - val
        x1 = (i + 1) * bar_width
        y1 = 380

        canvas.create_rectangle(
            x0, y0, x1, y1,
            fill=color[i],
            outline=""
        )

    root.update_idletasks()

# ---------------- SORTING ALGORITHMS ----------------
def bubble_sort():
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            draw_array(
                array,
                ["yellow" if x == j or x == j + 1 else "#4fc3f7" for x in range(n)]
            )
            time.sleep(speed.get())

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                draw_array(
                    array,
                    ["red" if x == j or x == j + 1 else "#4fc3f7" for x in range(n)]
                )
                time.sleep(speed.get())

        draw_array(
            array,
            ["green" if x >= n - i - 1 else "#4fc3f7" for x in range(n)]
        )

    draw_array(array, ["green"] * n)


def quick_sort(start, end):
    if start >= end:
        return

    pivot = array[end]
    p = start

    for i in range(start, end):
        draw_array(
            array,
            ["orange" if x == i or x == end else "#4fc3f7" for x in range(len(array))]
        )
        time.sleep(speed.get())

        if array[i] < pivot:
            array[i], array[p] = array[p], array[i]
            p += 1

    array[p], array[end] = array[end], array[p]

    quick_sort(start, p - 1)
    quick_sort(p + 1, end)


def merge_sort(arr, l, r):
    if l >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        draw_array(
            arr,
            ["purple" if x == k else "#4fc3f7" for x in range(len(arr))]
        )
        time.sleep(speed.get())

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    draw_array(
        arr,
        ["green" if l <= x <= r else "#4fc3f7" for x in range(len(arr))]
    )


def start_sort():
    if algo.get() == "Bubble Sort":
        bubble_sort()

    elif algo.get() == "Quick Sort":
        quick_sort(0, len(array) - 1)
        draw_array(array, ["green"] * len(array))

    elif algo.get() == "Merge Sort":
        merge_sort(array, 0, len(array) - 1)
        draw_array(array, ["green"] * len(array))

# ---------------- CONTROLS ----------------
control_frame = tk.Frame(root, bg="#1e1e2f")
control_frame.pack()

ttk.Style().theme_use("clam")

ttk.Button(
    control_frame,
    text="Generate Array",
    command=generate_array
).grid(row=0, column=0, padx=8)

ttk.Button(
    control_frame,
    text="Start Sorting",
    command=start_sort
).grid(row=0, column=1, padx=8)

ttk.Combobox(
    control_frame,
    textvariable=algo,
    values=["Bubble Sort", "Quick Sort", "Merge Sort"],
    state="readonly",
    width=15
).grid(row=0, column=2, padx=8)

tk.Label(
    control_frame,
    text="Size",
    bg="#1e1e2f",
    fg="white"
).grid(row=0, column=3)

tk.Scale(
    control_frame,
    from_=10,
    to=100,
    orient=tk.HORIZONTAL,
    variable=array_size,
    bg="#1e1e2f",
    fg="white"
).grid(row=0, column=4)

tk.Label(
    control_frame,
    text="Speed",
    bg="#1e1e2f",
    fg="white"
).grid(row=0, column=5)

tk.Scale(
    control_frame,
    from_=0.01,
    to=0.3,
    resolution=0.01,
    orient=tk.HORIZONTAL,
    variable=speed,
    bg="#1e1e2f",
    fg="white"
).grid(row=0, column=6)

# ---------------- START APP ----------------
generate_array()
root.mainloop()
