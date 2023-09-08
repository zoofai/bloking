import turtle

# Fungsi untuk menggambar bentuk dasar logo Instagram
def draw_instagram_logo():
    # Membuat objek turtle
    t = turtle.Turtle()
    t.speed(2)

    # Menggambar lingkaran
    t.color("#E4405F")  # Warna Instagram
    t.pensize(5)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Menggambar lensa kamera
    t.penup()
    t.goto(-35, 0)
    t.pendown()
    t.color("#ffffff")  # Warna putih
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    # Menggambar lensa kamera (bagian dalam)
    t.penup()
    t.goto(-20, 0)
    t.pendown()
    t.color("#E4405F")  # Warna Instagram
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # Menggambar lensa kamera (titik)
    t.penup()
    t.goto(10, -10)
    t.pendown()
    t.color("#ffffff")  # Warna putih
    t.begin_fill()
    t.circle(7)
    t.end_fill()

    # Menggambar logo Instagram
    t.penup()
    t.goto(-20, -130)
    t.pendown()
    t.color("#E4405F")  # Warna Instagram
    t.write("GATAU", align="center", font=("Arial", 12, "normal"))

    t.hideturtle()

    # Menutup jendela ketika di-klik
    turtle.exitonclick()

# Memanggil fungsi untuk menggambar logo Instagram
draw_instagram_logo()
