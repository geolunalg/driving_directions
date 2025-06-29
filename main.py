from src.trip_directions import TripDirections


def main():
    print("directions app!!")
    app = TripDirections()
    app.display()
    app.geometry("600x700")
    app.mainloop()


if __name__ == "__main__":
    main()
