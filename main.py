from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/sequence")


def main():
    # click start button
    start_btn = driver.find_elements(By.TAG_NAME, "button")[1]
    start_btn.click()

    while True:
        # watch
        sequence = watch_sequence()

        # click squares in sequence
        while sequence:
            square = sequence.pop()
            square.click()


def watch_sequence() -> list:
    sequence = []
    tol_start = time()
    squares = driver.find_element(By.CLASS_NAME, "squares")

    while time() - tol_start < 3:
        active_squares = squares.find_elements(By.CLASS_NAME, "active")
        if active_squares:
            active_square = active_squares[0]
            if len(sequence) and (sequence[-1] == active_square):
                continue
            else:
                sequence.append(active_square)
                tol_start = time()

    sequence.reverse()
    return sequence


# begin test
if __name__ == '__main__':
    main()
