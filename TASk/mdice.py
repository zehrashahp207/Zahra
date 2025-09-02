from random import randint
def roll_dice():
    return randint(1, 6), randint(1, 6)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1453)