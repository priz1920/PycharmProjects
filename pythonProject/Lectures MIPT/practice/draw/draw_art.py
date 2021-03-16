import graphics as gr

window = gr.GraphWin("KubaLibra", 900, 700)

sky = gr.Rectangle(gr.Point(000, 500), gr.Point(900, 100))
sky.setFill("blue")


sky.draw(window)
window.getMouse()
window.close()