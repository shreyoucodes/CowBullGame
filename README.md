# 🎮 CowBull Colour Game

A fun and interactive **colour-based guessing game** built with **Python's Tkinter GUI toolkit**. Inspired by the classic *Bulls and Cows* game, this version uses colours instead of numbers or words, making it intuitive and visually engaging.

---

## 🧠 Game Concept

The computer randomly selects a sequence of **4 colours** from a predefined set:

```bash
["Red", "Blue", "Yellow", "Green"]
```


Your task is to **guess the correct sequence** in the correct order within a limited number of tries depending on the difficulty level.

---

## 🎯 Features

- ✅ **Three difficulty levels**: Easy (10 tries), Medium (5 tries), Hard (3 tries)
- 🎨 **Intuitive GUI** using `Tkinter`
- 🧩 **Visual feedback** for each guess:
  - Correct colour and correct position ✅
  - Correct colour but wrong position ⚠️
  - Incorrect colour ❌
- 🧠 **Dynamic reasoning** like "Bulls and Cows" logic
- 🎉 **Win or lose screen** with custom messages and images

---

## 🛠 Technologies Used

- **Python 3.x**
- **Tkinter** – for GUI elements
- **tkinter.font.Font** – for custom fonts
- **random** – to generate the secret colour sequence

---

## 🖼 Image Assets

This game uses two images:

- ✔️ Correct guess image (`corr.png`)
- ❌ Partial or incorrect guess image (`coww.png`)

> 📁 Make sure these image files exist at the specified paths:

```bash
C:\CowBullGame\coww.png
C:\CowBullGame\corr.png
```

Or adjust the `PhotoImage(file=...)` paths in the code accordingly.

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Place the game script in a `.py` file (e.g., `cowbull_game.py`).
3. Ensure the images (`coww.png` and `corr.png`) are correctly located or update the paths.
4. Run the game:

```bash
python cowbull_game.py
```
